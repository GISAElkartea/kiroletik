# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flatpage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('url', autoslug.fields.AutoSlugField(verbose_name='URL', unique=True, editable=False)),
                ('published', models.BooleanField(default=True, verbose_name='published')),
                ('content', ckeditor.fields.RichTextField(verbose_name='content')),
            ],
            options={
                'verbose_name': 'Flatpage',
                'verbose_name_plural': 'Flatpages',
            },
            bases=(models.Model,),
        ),
    ]
