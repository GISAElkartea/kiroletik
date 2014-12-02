from django.conf.urls import patterns, url


slug = r'(?P<slug>(\w|-)+)'


urlpatterns = patterns(
    'flatpages.views',

    url(r'^{}/$'.format(slug),
        'flatpage_detail',
        name='flatpage-detail')
)
