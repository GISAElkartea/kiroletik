# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import positions.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teamclassification',
            options={'ordering': ['-position', '-points'], 'verbose_name': 'Team classification', 'verbose_name_plural': 'Team classifications'},
        ),
        migrations.AlterModelOptions(
            name='teamresult',
            options={'ordering': ['-position', '-points'], 'verbose_name': 'Team result', 'verbose_name_plural': 'Team results'},
        ),
        migrations.AddField(
            model_name='teamclassification',
            name='position',
            field=positions.fields.PositionField(default=0, verbose_name='position'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='teamresult',
            name='position',
            field=positions.fields.PositionField(default=0, verbose_name='position'),
            preserve_default=True,
        ),
    ]
