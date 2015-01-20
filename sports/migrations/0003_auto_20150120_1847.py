# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import positions.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0002_auto_20150120_0920'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teamclassification',
            options={'ordering': ['position', '-points'], 'verbose_name': 'Team classification', 'verbose_name_plural': 'Team classifications'},
        ),
        migrations.AlterModelOptions(
            name='teamresult',
            options={'ordering': ['position', '-points'], 'verbose_name': 'Team result', 'verbose_name_plural': 'Team results'},
        ),
        migrations.AddField(
            model_name='match',
            name='name',
            field=models.CharField(max_length=150, verbose_name='name', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teamclassification',
            name='position',
            field=positions.fields.PositionField(default=-1, verbose_name='position'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teamresult',
            name='position',
            field=positions.fields.PositionField(default=-1, verbose_name='position'),
            preserve_default=True,
        ),
    ]
