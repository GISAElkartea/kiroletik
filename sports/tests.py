from datetime import timedelta

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.utils.timezone import now

from model_mommy import mommy

from .models import News, Sport


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


class SportDetailTestCase(TestCase):
    def setUp(self):
        self.sport = mommy.make(Sport)
        self.url = self.sport.get_absolute_url()

    def test_ok(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_context(self):
        ctx = self.client.get(self.url).context
        self.assertIn('sport', ctx)
        self.assertEqual(ctx['sport'], self.sport)
