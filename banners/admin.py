from django.contrib import admin

from .models import Banner


class BannerAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')
    fields = (('name', 'active'), 'image')


admin.site.register(Banner, BannerAdmin)
