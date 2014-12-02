# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('banners', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'ordering': ('-active', '-pk'), 'verbose_name': 'Banner', 'verbose_name_plural': 'Banners'},
        ),
    ]
