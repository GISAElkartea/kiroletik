# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def move_match(apps, schema_editor):
    News = apps.get_model('sports', 'News')
    for news in News.objects.all():
        if news.match:
            news.matches.add(news.match)


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0003_auto_20150120_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='matches',
            field=models.ManyToManyField(to='sports.Match', null=True, verbose_name='matches', blank=True),
            preserve_default=True,
        ),
        migrations.RunPython(move_match),
        migrations.RemoveField(
            model_name='news',
            name='match',
        ),
    ]
