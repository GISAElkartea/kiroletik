from django.contrib import admin

from adminsortable.admin import SortableAdminMixin

from .models import Widget


class WidgetAdmin(SortableAdminMixin, admin.ModelAdmin):
    fields = (('name', 'active'), 'content')
    list_display = ('name', 'active')


admin.site.register(Widget, WidgetAdmin)
