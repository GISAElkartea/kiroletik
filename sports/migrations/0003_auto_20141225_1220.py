# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0002_auto_20141224_2256'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='season',
            unique_together=set([('competition', 'date')]),
        ),
    ]
