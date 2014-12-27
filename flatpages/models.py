from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from autoslug import AutoSlugField
from ckeditor.fields import RichTextField


class FlatpageQueryset(models.QuerySet):
    def published(self):
        return self.filter(published=True)

    def unpublished(self):
        return self.filter(published=False)


class Flatpage(models.Model):
    objects = FlatpageQueryset.as_manager()

    class Meta:
        verbose_name = _('Flatpage')
        verbose_name_plural = _('Flatpages')

    title = models.CharField(max_length=100, verbose_name=_('title'))
    url = AutoSlugField(populate_from='title', unique=True,
                        verbose_name=_('URL'))

    published = models.BooleanField(default=True, verbose_name=_('published'))
    content = RichTextField(verbose_name=_('content'))

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('flatpage-detail', kwargs={'slug': self.url})
