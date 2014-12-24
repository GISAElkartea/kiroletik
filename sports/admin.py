from django.contrib import admin

from .models import (Sport, Town, Competition, Season, Team, TeamClassification,
                     MatchResult, News)


admin.site.register(Town)


class SportAdmin(admin.ModelAdmin):
    fields = ('name', 'image')
admin.site.register(Sport)


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
    fields = ('season', ('team_foo', 'foo_points'), ('team_bar', 'bar_points'))
    list_display = ('__str__', 'season')
    list_filter = ('season',)
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
