# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0004_auto_20141225_2317'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sport',
            options={'ordering': ['name'], 'verbose_name': 'Sport', 'verbose_name_plural': 'Sports'},
        ),
        migrations.AddField(
            model_name='sport',
            name='on_menu',
            field=models.BooleanField(default=False, verbose_name='on menu'),
            preserve_default=True,
        ),
    ]
