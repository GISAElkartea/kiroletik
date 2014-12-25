from django.conf.urls import patterns, url


year = r'(?P<year>\d{4})'
month = r'(?P<month>\d{2})'
day = r'(?P<day>\d{2})'
slug = r'(?P<slug>(\w|-)+)'


urlpatterns = patterns(
    'sports.views',

    url(r'^news/$',
        'news_list',
        name='news-list'),

    url(r'^news/{}/{}/{}/{}$'.format(year, month, day, slug),
        'news_detail',
        name='news-detail'),

    url(r'^sport/{}/$'.format(slug),
        'sport_detail',
        name='sport-detail'),

    url(r'^matches/$',
        'match_list',
        name='match-list'),

    url(r'^season/{}/{}/{}/$'.format(year, month, day),
        'season_detail',
        name='season-detail'),
)
