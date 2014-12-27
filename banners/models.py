from django.db import models
from django.utils.translation import ugettext_lazy as _


class BannerQuerySet(models.QuerySet):
    def active(self):
        try:
            return self.get(active=True)
        except Banner.DoesNotExist:
            return None


class Banner(models.Model):
    objects = BannerQuerySet.as_manager()

    class Meta:
        ordering = ('-active', '-pk')
        verbose_name = _('Banner')
        verbose_name_plural = _('Banners')

    name = models.CharField(max_length=50, verbose_name=_('name'))
    active = models.BooleanField(default=True, verbose_name=_('active'))
    image = models.ImageField(upload_to='banners', verbose_name=_('image'))

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Banner, self).save(*args, **kwargs)
        if self.active:
            Banner.objects.exclude(pk=self.pk).update(active=False)
