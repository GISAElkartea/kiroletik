# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields
import positions.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Widget',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('position', positions.fields.PositionField(default=0, verbose_name='position')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('content', ckeditor.fields.RichTextField(verbose_name='content')),
            ],
            options={
                'ordering': ('-position', '-pk'),
                'verbose_name': 'Widget',
                'verbose_name_plural': 'Widgets',
            },
            bases=(models.Model,),
        ),
    ]
