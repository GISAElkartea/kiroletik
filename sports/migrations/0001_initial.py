# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import ckeditor.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('description', ckeditor.fields.RichTextField(verbose_name='description', blank=True)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
            ],
            options={
                'verbose_name': 'Competition',
                'verbose_name_plural': 'Competitions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MatchResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('foo_points', models.PositiveIntegerField(verbose_name='Points for first team')),
                ('bar_points', models.PositiveIntegerField(verbose_name='Points for second team')),
            ],
            options={
                'verbose_name': 'Match result',
                'verbose_name_plural': 'Match results',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('content', ckeditor.fields.RichTextField(verbose_name='content', blank=True)),
                ('image', models.ImageField(upload_to=b'images/news', verbose_name='image', blank=True)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
                ('match', models.ForeignKey(verbose_name='match', blank=True, to='sports.MatchResult', null=True)),
            ],
            options={
                'ordering': ['-published'],
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='date')),
                ('name', models.CharField(max_length=150, verbose_name='name', blank=True)),
                ('competition', models.ForeignKey(verbose_name='competition', to='sports.Competition')),
            ],
            options={
                'verbose_name': 'Season',
                'verbose_name_plural': 'Seasons',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100, verbose_name='name')),
                ('image', models.ImageField(upload_to=b'images/sports', verbose_name='image', blank=True)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
            ],
            options={
                'verbose_name': 'Sport',
                'verbose_name_plural': 'Sports',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('description', ckeditor.fields.RichTextField(verbose_name='description', blank=True)),
                ('image', models.ImageField(upload_to=b'images/teams', verbose_name='image', blank=True)),
                ('sport', models.ForeignKey(verbose_name='sport', to='sports.Sport')),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Teams',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeamClassification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('points', models.PositiveIntegerField(verbose_name='points')),
                ('season', models.ForeignKey(verbose_name='season', to='sports.Season')),
                ('team', models.ForeignKey(verbose_name='team', to='sports.Team')),
            ],
            options={
                'ordering': ['points'],
                'verbose_name': 'Team classification',
                'verbose_name_plural': 'Team classifications',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50, verbose_name='town')),
            ],
            options={
                'verbose_name': 'Town',
                'verbose_name_plural': 'Towns',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='team',
            name='town',
            field=models.ForeignKey(blank=True, to='sports.Town', help_text='Local team if town filled in', null=True, verbose_name='town'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='team',
            unique_together=set([('sport', 'name')]),
        ),
        migrations.AddField(
            model_name='news',
            name='sport',
            field=models.ForeignKey(verbose_name='sport', blank=True, to='sports.Sport', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='matchresult',
            name='season',
            field=models.ForeignKey(verbose_name='season', blank=True, to='sports.Season', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='matchresult',
            name='team_bar',
            field=models.ForeignKey(related_name=b'+', verbose_name='Second team', to='sports.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='matchresult',
            name='team_foo',
            field=models.ForeignKey(related_name=b'+', verbose_name='First team', to='sports.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='competition',
            name='sport',
            field=models.ForeignKey(verbose_name='sport', to='sports.Sport'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='competition',
            unique_together=set([('name', 'sport')]),
        ),
    ]
