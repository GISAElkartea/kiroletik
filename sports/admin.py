from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import (Sport, Town, Competition, Season, Team, TeamClassification,
                     MatchResult, News)


admin.site.register(Town)


class SportAdmin(admin.ModelAdmin):
    fields = (('name', 'on_menu'), 'image')
    list_display = ('name', 'on_menu')
    list_filter = ('on_menu',)
    actions = ('put_on_menu', 'remove_from_menu')

    def put_on_menu(self, request, queryset):
        queryset.update(on_menu=True)
    put_on_menu.short_description = _('Put on menu')

    def remove_from_menu(self, request, queryset):
        queryset.update(on_menu=False)
    remove_from_menu.short_description = _('Remove from menu')

admin.site.register(Sport, SportAdmin)


class CompetitionAdmin(admin.ModelAdmin):
    fields = ('name', 'sport', 'description')
admin.site.register(Competition, CompetitionAdmin)


class TeamClassificationInline(admin.TabularInline):
    model = TeamClassification
    fields = ('team', 'points')
    extra = 1


class SeasonAdmin(admin.ModelAdmin):
    inlines = [TeamClassificationInline]
    fields = ('competition', 'date', 'name')
    list_display = ('date', 'competition', 'name')
    list_filter = ('competition', 'date')
    date_hierarchy = 'date'
    search_fields = ('name',)
admin.site.register(Season, SeasonAdmin)


class TeamAdmin(admin.ModelAdmin):
    fields = (('sport', 'name'), 'town', 'description', 'image')
    list_display = ('name', 'sport', 'town')
    list_filter = ('sport', 'town')
    search_fields = ('name',)
admin.site.register(Team, TeamAdmin)


class MatchResultAdmin(admin.ModelAdmin):
    fields = (('date', 'season'), ('team_foo', 'foo_points'),
              ('team_bar', 'bar_points'))
    list_display = ('__str__', 'date', 'season')
    list_filter = ('season', 'date')
    date_hierarchy = 'date'
admin.site.register(MatchResult, MatchResultAdmin)


class NewsAdmin(admin.ModelAdmin):
    fields = ('title', 'published', ('sport', 'match'), 'content', 'image')
    list_display = ('__str__', 'sport', 'published', 'is_published')
    list_filter = ('sport', 'published',)
    search_fields = ('title', 'content')
    date_hierarchy = 'published'

    def is_published(self, obj):
        return obj.is_published
    is_published.boolean = True
admin.site.register(News, NewsAdmin)
