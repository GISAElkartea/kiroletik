from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Flatpage


class FlatpageAdmin(admin.ModelAdmin):
    readonly_fields = ('absolute_url',)
    fields = ('published', ('name', 'absolute_url'), 'content')
    list_display = ('title', 'absolute_url')

    def absolute_url(self, obj):
        url = obj.get_absolute_url()
        return '<a href="{link}">{link}</a>'.format(link=url)
    absolute_url.short_description = _('Absolute URL')
    absolute_url.allow_tags = True


admin.site.register(Flatpage, FlatpageAdmin)
