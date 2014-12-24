# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teamclassification',
            options={'ordering': ['-points'], 'verbose_name': 'Team classification', 'verbose_name_plural': 'Team classifications'},
        ),
        migrations.AlterUniqueTogether(
            name='teamclassification',
            unique_together=set([('team', 'season')]),
        ),
    ]
