from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.timezone import now
from django.utils.translation import ugettext as _

from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from positions.fields import PositionField


class SportQuerySet(models.QuerySet):
    def on_menu(self):
        return self.filter(on_menu=True)

    def not_on_menu(self):
        return self.filter(on_menu=False)


class Sport(models.Model):
    objects = SportQuerySet.as_manager()

    class Meta:
        ordering = ['name']
        verbose_name = _('Sport')
        verbose_name_plural = _('Sports')

    name = models.CharField(max_length=100, unique=True, verbose_name=_('name'))
    on_menu = models.BooleanField(default=False, verbose_name=_('on menu'))
    image = models.ImageField(upload_to='images/sports', blank=True,
                              verbose_name=_('image'))

    slug = AutoSlugField(populate_from='name', unique=True, editable=False)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('sport-news-list', kwargs={'slug': self.slug})


class Town(models.Model):
    class Meta:
        verbose_name = _('Town')
        verbose_name_plural = _('Towns')

    name = models.CharField(max_length=50, unique=True, verbose_name=_('town'))

    def __unicode__(self):
        return self.name


class Championship(models.Model):
    class Meta:
        unique_together = ('name', 'sport')
        verbose_name = _('Championship')
        verbose_name_plural = _('Championships')

    name = models.CharField(max_length=150, verbose_name=_('name'))
    sport = models.ForeignKey(Sport, verbose_name=_('sport'))
    description = RichTextField(blank=True, verbose_name=_('description'))

    slug = AutoSlugField(populate_from='name', unique=True, editable=False)

    def __unicode__(self):
        return self.name

    def get_latest_season(self):
        return self.season_set.latest('date')

    def get_absolute_url(self):
        return self.get_latest_season().get_absolute_url()


class Season(models.Model):
    class Meta:
        ordering = ['-date']
        unique_together = ('championship', 'date')
        verbose_name = _('Season')
        verbose_name_plural = _('Seasons')

    championship = models.ForeignKey(Championship,
                                     verbose_name=_('championship'))
    date = models.DateField(verbose_name=_('date'))
    name = models.CharField(max_length=150, blank=True,
                            verbose_name=_('name'))

    def __unicode__(self):
        return self.name or str(self.date)

    def get_absolute_url(self):
        return reverse('season-detail', kwargs={
            'slug': self.championship.slug,
            'year': '{:04d}'.format(self.date.year),
            'month': '{:02d}'.format(self.date.month),
            'day': '{:02d}'.format(self.date.day)})

    def next(self):
        next = Season.objects.filter(championship=self.championship,
                                     date__gt=self.date)
        return next.last()

    def previous(self):
        previous = Season.objects.filter(championship=self.championship,
                                         date__lt=self.date)
        return previous.first()


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

    def __unicode__(self):
        return self.name

    @property
    def is_local(self):
        return self.town is not None


class TeamClassification(models.Model):
    class Meta:
        ordering = ['position', '-points']
        unique_together = ('team', 'season')
        verbose_name = _('Team classification')
        verbose_name_plural = _('Team classifications')

    team = models.ForeignKey(Team, verbose_name=_('team'))
    season = models.ForeignKey(Season, verbose_name=_('season'))
    points = models.PositiveIntegerField(verbose_name=_('points'))
    position = PositionField(default=-1, verbose_name=_('position'))

    def __unicode__(self):
        return '{s.team} {s.points} points at {s.season}'.format(s=self)


class Match(models.Model):
    class Meta:
        ordering = ('-date',)
        verbose_name = _('Match')
        verbose_name_plural = _('Match')

    date = models.DateField(verbose_name=_('date'))
    season = models.ForeignKey(Season, blank=True, null=True,
                               verbose_name=_('season'))

    def is_antagonistic(self):
        return self.teamresult_set.count() == 2

    def __unicode__(self):
        return str(self.date)


class TeamResult(models.Model):
    class Meta:
        ordering = ['position', '-points']
        unique_together = ('team', 'match')
        verbose_name = _('Team result')
        verbose_name_plural = _('Team results')

    team = models.ForeignKey(Team, verbose_name=_('team'))
    points = models.PositiveIntegerField(verbose_name=_('points'))
    match = models.ForeignKey(Match, verbose_name=_('match'))
    position = PositionField(default=-1, verbose_name=_('position'))

    def __unicode__(self):
        return '{s.team} {s.points} points at {s.match}'.format(s=self)


class NewsQuerySet(models.QuerySet):
    def published(self):
        return self.filter(published__lte=now())

    def unpublished(self):
        return self.filter(published__gt=now())


class News(models.Model):
    objects = NewsQuerySet.as_manager()

    class Meta:
        ordering = ['-highlighted', '-published', 'pk']
        verbose_name = _('News')
        verbose_name_plural = _('News')

    published = models.DateTimeField(default=now)
    highlighted = models.BooleanField(default=False,
                                      verbose_name=_('highlighted'))
    sport = models.ForeignKey(Sport, null=True, blank=True,
                              verbose_name=_('sport'))
    match = models.ForeignKey(Match, null=True, blank=True,
                              verbose_name=_('match'))

    title = models.CharField(max_length=200, verbose_name=_('title'))
    content = RichTextField(blank=True, verbose_name=_('content'))
    image = models.ImageField(upload_to='images/news', blank=True,
                              verbose_name=_('image'))

    slug = AutoSlugField(populate_from='title', unique=True, editable=False)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.highlighted:
            News.objects.update(highlighted=False)
        super(News, self).save(*args, **kwargs)

    @property
    def is_published(self):
        return now() > self.published

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={
            'year': '{:04d}'.format(self.published.year),
            'month': '{:02d}'.format(self.published.month),
            'day': '{:02d}'.format(self.published.day),
            'slug': self.slug})
