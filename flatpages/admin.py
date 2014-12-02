from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Flatpage


class FlatpageAdmin(admin.ModelAdmin):
    readonly_fields = ('absolute_url',)
    fields = ('published', ('name', 'absolute_url'), 'content')
    list_display = ('name', 'absolute_url')

    def absolute_url(self, obj):
        return obj.get_absolute_url()
    absolute_url.short_description = _('Absolute URL')


admin.site.register(Flatpage, FlatpageAdmin)
