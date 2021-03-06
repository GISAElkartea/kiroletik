from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from grappelli.forms import GrappelliSortableHiddenMixin

from .models import (Sport, Town, Championship, Season, Team,
                     TeamClassification, Match, TeamResult, News)
from .forms import TeamClassificationForm, TeamResultForm


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


class ChampionshipAdmin(admin.ModelAdmin):
    fields = ('name', 'sport', 'description')
admin.site.register(Championship, ChampionshipAdmin)


class TeamClassificationInline(GrappelliSortableHiddenMixin,
                               admin.TabularInline):
    model = TeamClassification
    form = TeamClassificationForm
    fields = ('position', 'team', 'points')
    sortable_field_name = 'position'
    extra = 1


class SeasonAdmin(admin.ModelAdmin):
    inlines = [TeamClassificationInline]
    fields = ('championship', 'date', 'name')
    list_display = ('date', 'championship', 'name')
    list_filter = ('championship', 'date')
    date_hierarchy = 'date'
    search_fields = ('name',)
admin.site.register(Season, SeasonAdmin)


class TeamAdmin(admin.ModelAdmin):
    fields = (('sport', 'name'), 'town', 'description', 'image')
    list_display = ('name', 'sport', 'town')
    list_filter = ('sport', 'town')
    search_fields = ('name',)
admin.site.register(Team, TeamAdmin)


class TeamResultInline(GrappelliSortableHiddenMixin, admin.TabularInline):
    model = TeamResult
    form = TeamResultForm
    fields = ('position', 'team', 'points')
    sortable_field_name = 'position'
    extra = 1


class MatchAdmin(admin.ModelAdmin):
    inlines = [TeamResultInline]
    fields = ('date', 'name', 'season')
    list_display = ('date', 'name', 'season')
    list_filter = ('season', 'date')
    search_fields = ('name',)
    date_hierarchy = 'date'
admin.site.register(Match, MatchAdmin)


class NewsAdmin(admin.ModelAdmin):
    fields = ('title', ('published', 'highlighted'), ('sport', 'matches'),
              'content', 'image')
    list_display = ('__str__', 'sport', 'published', 'is_published',
                    'highlighted')
    list_filter = ('sport', 'published',)
    search_fields = ('title', 'content')
    date_hierarchy = 'published'

    def is_published(self, obj):
        return obj.is_published
    is_published.boolean = True
admin.site.register(News, NewsAdmin)
