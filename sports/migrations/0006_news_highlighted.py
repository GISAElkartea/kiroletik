# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0005_auto_20141229_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='highlighted',
            field=models.BooleanField(default=False, verbose_name='highlighted'),
            preserve_default=True,
        ),
    ]
