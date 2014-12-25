from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.dates import ArchiveIndexView, DateDetailView
from django.views.generic.dates import YearMixin, MonthMixin, DayMixin

from .models import News, Sport, MatchResult, Season


class NewsMixin(object):
    model = News
    allow_empty = True
    date_field = 'published'
    allow_future = False
    month_format = '%m'


class NewsList(NewsMixin, ArchiveIndexView):
    context_object_name = 'news_list'
    template_name = 'sports/news_list.html'


class NewsDetail(NewsMixin, DateDetailView):
    context_object_name = 'news'
    template_name = 'sports/news_detail.html'


class SportDetail(DetailView):
    model = Sport
    context_object_name = 'sport'
    template_name = 'sports/sport_detail.html'


class MatchList(ListView):
    model = MatchResult
    allow_empty = True
    context_object_name = 'matches'
    template_name = 'sports/match_list.html'


class SeasonDetail(DetailView, YearMixin, MonthMixin, DayMixin):
    model = Season
    slug_field = 'competition__slug'
    month_format = '%m'
    context_object_name = 'season'
    template_name = 'sports/season_detail.html'

    def get_queryset(self):
        return Season.objects.filter(date__year=self.get_year(),
                                     date__month=self.get_month(),
                                     date__day=self.get_day())


news_list = NewsList.as_view()
news_detail = NewsDetail.as_view()
sport_detail = SportDetail.as_view()
match_list = MatchList.as_view()
season_detail = SeasonDetail.as_view()
