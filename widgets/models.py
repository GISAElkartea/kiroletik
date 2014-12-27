from django.db import models
from django.utils.translation import ugettext_lazy as _

from ckeditor.fields import RichTextField
from positions.fields import PositionField


class WidgetQuerySet(models.QuerySet):
    def active(self):
        return self.filter(active=True)

    def inactive(self):
        return self.filter(active=False)


class Widget(models.Model):
    objects = WidgetQuerySet.as_manager()

    class Meta:
        ordering = ('-position', '-pk')
        verbose_name = _('Widget')
        verbose_name_plural = _('Widgets')

    name = models.CharField(max_length=100, verbose_name=_('name'))
    position = PositionField(default=0, verbose_name=_('position'))
    active = models.BooleanField(default=True, verbose_name=_('active'))
    content = RichTextField(verbose_name=_('content'))

    def __unicode__(self):
        return self.name
