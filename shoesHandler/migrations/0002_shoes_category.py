# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoesHandler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoes',
            name='category',
            field=models.CharField(max_length=100, default='none'),
            preserve_default=False,
        ),
    ]
