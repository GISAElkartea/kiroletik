from django.db import models
from django.utils.timezone import now
from django.utils.translation import ugettext as _

from autoslug import AutoSlugField
from ckeditor.fields import RichTextField


class Sport(models.Model):
    class Meta:
        verbose_name = _('Sport')
        verbose_name_plural = _('Sports')

    name = models.CharField(max_length=100, unique=True, verbose_name=_('name'))
    image = models.ImageField(upload_to='images/sports', blank=True,
                              verbose_name=_('image'))

    slug = AutoSlugField(populate_from='name', unique=True, editable=False)

    def __str__(self):
        return self.name


class Town(models.Model):
    class Meta:
        verbose_name = _('Town')
        verbose_name_plural = _('Towns')

    name = models.CharField(max_length=50, unique=True, verbose_name=_('town'))

    def __str__(self):
        return self.name


class Competition(models.Model):
    class Meta:
        unique_together = ('name', 'sport')
        verbose_name = _('Competition')
        verbose_name_plural = _('Competitions')

    name = models.CharField(max_length=150, verbose_name=_('name'))
    sport = models.ForeignKey(Sport, verbose_name=_('sport'))
    description = RichTextField(blank=True, verbose_name=_('description'))

    slug = AutoSlugField(populate_from='name', unique=True, editable=False)

    def __str__(self):
        return self.name


class Season(models.Model):
    class Meta:
        verbose_name = _('Season')
        verbose_name_plural = _('Seasons')

    competition = models.ForeignKey(Competition, verbose_name=_('competition'))
    date = models.DateField(verbose_name=_('date'))
    name = models.CharField(max_length=150, blank=True,
                            verbose_name=_('name'))

    def __str__(self):
        return str(self.date)


class Team(models.Model):
    class Meta:
        unique_together = ('sport', 'name')
        verbose_name = _('Team')
        verbose_name_plural = _('Teams')

    name = models.CharField(max_length=200, verbose_name=_('name'))
    sport = models.ForeignKey(Sport, verbose_name=_('sport'))
    description = RichTextField(blank=True, verbose_name=_('description'))
    town = models.ForeignKey(Town, null=True, blank=True,
                             verbose_name=_('town'),
                             help_text=_('Local team if town filled in'))
    image = models.ImageField(upload_to='images/teams', blank=True,
                              verbose_name=_('image'))

    def __str__(self):
        return self.name

    @property
    def is_local(self):
        return self.town is not None


class TeamClassification(models.Model):
    class Meta:
        ordering = ['points']
        verbose_name = _('Team classification')
        verbose_name_plural = _('Team classifications')

    team = models.ForeignKey(Team, verbose_name=_('team'))
    season = models.ForeignKey(Season, verbose_name=_('season'))
    points = models.PositiveIntegerField(verbose_name=_('points'))

    def __str__(self):
        return '{s.team} {s.points} points at {s.season}'.format(s=self)


class MatchResult(models.Model):
    class Meta:
        verbose_name = _('Match result')
        verbose_name_plural = _('Match results')

    team_foo = models.ForeignKey(Team, related_name='+',
                                 verbose_name=_('First team'))
    team_bar = models.ForeignKey(Team, related_name='+',
                                 verbose_name=_('Second team'))
    foo_points = models.PositiveIntegerField(
        verbose_name=_('Points for first team'))
    bar_points = models.PositiveIntegerField(
        verbose_name=_('Points for second team'))
    season = models.ForeignKey(Season, blank=True, null=True,
                               verbose_name=_('season'))

    def __str__(self):
        return ('{s.team_foo}: {s.foo_points} - '
                '{s.team_bar} {s.bar_points}').format(s=self)


class News(models.Model):
    class Meta:
        ordering = ['-published']
        verbose_name = _('News')
        verbose_name_plural = _('News')

    published = models.DateTimeField(default=now())
    sport = models.ForeignKey(Sport, null=True, blank=True,
                              verbose_name=_('sport'))
    match = models.ForeignKey(MatchResult, null=True, blank=True,
                              verbose_name=_('match'))

    title = models.CharField(max_length=200, verbose_name=_('title'))
    content = RichTextField(blank=True, verbose_name=_('content'))
    image = models.ImageField(upload_to='images/news', blank=True,
                              verbose_name=_('image'))

    slug = AutoSlugField(populate_from='title', unique=True, editable=False)

    def __str__(self):
        return self.title