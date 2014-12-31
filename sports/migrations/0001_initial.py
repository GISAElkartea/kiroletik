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
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='date')),
            ],
            options={
                'ordering': ('-date',),
                'verbose_name': 'Match',
                'verbose_name_plural': 'Match',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('highlighted', models.BooleanField(default=False, verbose_name='highlighted')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('content', ckeditor.fields.RichTextField(verbose_name='content', blank=True)),
                ('image', models.ImageField(upload_to=b'images/news', verbose_name='image', blank=True)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
                ('match', models.ForeignKey(verbose_name='match', blank=True, to='sports.Match', null=True)),
            ],
            options={
                'ordering': ['-highlighted', '-published', 'pk'],
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
                'ordering': ['-date'],
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
                ('on_menu', models.BooleanField(default=False, verbose_name='on menu')),
                ('image', models.ImageField(upload_to=b'images/sports', verbose_name='image', blank=True)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
            ],
            options={
                'ordering': ['name'],
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
                'ordering': ['-points'],
                'verbose_name': 'Team classification',
                'verbose_name_plural': 'Team classifications',
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
        migrations.AlterUniqueTogether(
            name='teamresult',
            unique_together=set([('team', 'match')]),
        ),
        migrations.AlterUniqueTogether(
            name='teamclassification',
            unique_together=set([('team', 'season')]),
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
        migrations.AlterUniqueTogether(
            name='season',
            unique_together=set([('competition', 'date')]),
        ),
        migrations.AddField(
            model_name='news',
            name='sport',
            field=models.ForeignKey(verbose_name='sport', blank=True, to='sports.Sport', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='match',
            name='season',
            field=models.ForeignKey(verbose_name='season', blank=True, to='sports.Season', null=True),
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
