# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0003_auto_20141225_1220'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='matchresult',
            options={'ordering': ('-date',), 'verbose_name': 'Match result', 'verbose_name_plural': 'Match results'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-published', 'pk'], 'verbose_name': 'News', 'verbose_name_plural': 'News'},
        ),
        migrations.AlterModelOptions(
            name='season',
            options={'ordering': ['-date'], 'verbose_name': 'Season', 'verbose_name_plural': 'Seasons'},
        ),
        migrations.AddField(
            model_name='matchresult',
            name='date',
            field=models.DateField(default=datetime.date(2014, 12, 25), verbose_name='date'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='matchresult',
            unique_together=set([('team_foo', 'team_bar', 'date')]),
        ),
    ]
