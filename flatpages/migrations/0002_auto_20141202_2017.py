# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flatpages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flatpage',
            name='name',
        ),
        migrations.AddField(
            model_name='flatpage',
            name='title',
            field=models.CharField(default='', max_length=100, verbose_name='title'),
            preserve_default=False,
        ),
    ]
