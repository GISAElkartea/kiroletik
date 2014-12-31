# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0006_news_highlighted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='date')),
                ('season', models.ForeignKey(verbose_name='season', blank=True, to='sports.Season', null=True)),
            ],
            options={
                'ordering': ('-date',),
                'verbose_name': 'Match',
                'verbose_name_plural': 'Match',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeamResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('points', models.PositiveIntegerField(verbose_name='points')),
                ('match', models.ForeignKey(verbose_name='match', to='sports.Match')),
                ('team', models.ForeignKey(verbose_name='team', to='sports.Team')),
            ],
            options={
                'ordering': ['-points'],
                'verbose_name': 'Team result',
                'verbose_name_plural': 'Team results',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='matchresult',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='matchresult',
            name='season',
        ),
        migrations.RemoveField(
            model_name='matchresult',
            name='team_bar',
        ),
        migrations.RemoveField(
            model_name='matchresult',
            name='team_foo',
        ),
        migrations.AlterUniqueTogether(
            name='teamresult',
            unique_together=set([('team', 'match')]),
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-highlighted', '-published', 'pk'], 'verbose_name': 'News', 'verbose_name_plural': 'News'},
        ),
        migrations.AlterField(
            model_name='news',
            name='match',
            field=models.ForeignKey(verbose_name='match', blank=True, to='sports.Match', null=True),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='MatchResult',
        ),
    ]
