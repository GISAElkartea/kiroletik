from datetime import timedelta, date

from django.test import TestCase
from django.db import IntegrityError
from django.core.urlresolvers import reverse
from django.utils.timezone import now

from model_mommy import mommy

from .models import News, Sport, Match, Season, Competition


class SportTestCase(TestCase):
    def setUp(self):
        today = date.today()
        self.competition = mommy.make(Competition)
        self.alpha = mommy.make(Season, competition=self.competition,
                                date=(today + timedelta(days=1)))
        self.beta = mommy.make(Season, competition=self.competition,
                               date=(today + timedelta(days=2)))
        self.gamme = mommy.make(Season, competition=self.competition,
                                date=(today + timedelta(days=3)))
        self.delta = mommy.make(Season, competition=self.competition,
                                date=(today + timedelta(days=4)))
        self.epsilon = mommy.make(Season, competition=self.competition,
                                  date=(today + timedelta(days=5)))

    def test_not_same_date_and_competition(self):
        with self.assertRaises(IntegrityError):
            mommy.make(Season, competition=self.competition,
                       date=self.alpha.date)

    def test_next_present(self):
        self.assertEqual(self.alpha.next(), self.beta)

    def test_next_not_present(self):
        self.assertEqual(self.epsilon.next(), None)

    def test_previous_present(self):
        self.assertEqual(self.epsilon.previous(), self.delta)

    def test_previous_not_present(self):
        self.assertEqual(self.alpha.previous(), None)


class NewsListTestCase(TestCase):
    def setUp(self):
        past_date = now()
        future_date = now() + timedelta(days=1)
        self.past_news = mommy.make(News, published=past_date, _quantity=20)
        self.future_news = mommy.make(News, published=future_date, _quantity=5)
        self.url = reverse('news-list')

    def test_ok(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_empty(self):
        for news in self.past_news + self.future_news:
            news.delete()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_no_future_news(self):
        for news in self.past_news:
            news.delete()
        response = self.client.get(self.url)
        self.assertEqual(len(response.context['news_list']), 0)

    def test_news_in_context(self):
        response = self.client.get(self.url)
        self.assertIn('news_list', response.context)

    def test_order(self):
        alpha = mommy.make(News)
        beta = mommy.make(News)
        gamma = mommy.make(News)
        ctx = self.client.get(self.url).context
        self.assertEqual(ctx['news_list'][:3], [gamma, beta, alpha])

    def test_paginated(self):
        ctx = self.client.get(self.url).context
        self.assertTrue(ctx['is_paginated'])
        self.assertEqual(len(ctx['news_list']), 10)

    def test_pagination(self):
        page = self.client.get(self.url).context['page_obj']
        self.assertFalse(page.has_previous())
        self.assertEqual(page.number, 1)
        self.assertEqual(page.paginator.num_pages, 2)
        self.assertTrue(page.has_next())
        self.assertEqual(page.next_page_number(), 2)


class SportNewsList(NewsListTestCase):
    def setUp(self):
        self.sport = mommy.make(Sport)
        past_date = now()
        future_date = now() + timedelta(days=1)
        self.past_news = mommy.make(News, published=past_date, sport=self.sport,
                                    _quantity=20)
        self.future_news = mommy.make(News, published=future_date,
                                      sport=self.sport, _quantity=5)
        self.url = self.sport.get_absolute_url()

    def test_context(self):
        ctx = self.client.get(self.url).context
        self.assertIn('sport', ctx)
        self.assertEqual(ctx['sport'], self.sport)
        self.assertIn('news_list', ctx)

    def test_order(self):
        alpha = mommy.make(News, sport=self.sport)
        beta = mommy.make(News, sport=self.sport)
        gamma = mommy.make(News, sport=self.sport)
        ctx = self.client.get(self.url).context
        self.assertEqual(ctx['news_list'][:3], [gamma, beta, alpha])


class NewsDetailTestCase(TestCase):
    def setUp(self):
        past_date = now()
        future_date = now() + timedelta(days=1)
        self.past_news = mommy.make(News, published=past_date)
        self.future_news = mommy.make(News, published=future_date)

    def test_past_ok(self):
        url = self.past_news.get_absolute_url()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_future_not_found(self):
        url = self.future_news.get_absolute_url()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_news_in_context(self):
        url = self.past_news.get_absolute_url()
        ctx = self.client.get(url).context
        self.assertIn('news', ctx)
        self.assertEqual(ctx['news'], self.past_news)


class MatchListTestCase(TestCase):
    def setUp(self):
        self.matches = mommy.make(Match, _quantity=20)
        self.url = reverse('match-list')

    def test_ok(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_empty(self):
        for match in self.matches:
            match.delete()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_context(self):
        response = self.client.get(self.url)
        self.assertIn('matches', response.context)

    def test_order(self):
        matches = list(Match.objects.order_by('-date')[:10])
        ctx = self.client.get(self.url).context
        self.assertEqual(list(ctx['matches']), matches)

    def test_paginated(self):
        ctx = self.client.get(self.url).context
        self.assertTrue(ctx['is_paginated'])
        self.assertEqual(len(ctx['matches']), 10)

    def test_pagination(self):
        page = self.client.get(self.url).context['page_obj']
        self.assertFalse(page.has_previous())
        self.assertEqual(page.number, 1)
        self.assertEqual(page.paginator.num_pages, 2)
        self.assertTrue(page.has_next())
        self.assertEqual(page.next_page_number(), 2)


class SeasonDetailTestCase(TestCase):
    def setUp(self):
        self.season = mommy.make(Season)
        self.url = self.season.get_absolute_url()

    def test_ok(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_context(self):
        ctx = self.client.get(self.url).context
        self.assertIn('season', ctx)
        self.assertEqual(ctx['season'], self.season)
