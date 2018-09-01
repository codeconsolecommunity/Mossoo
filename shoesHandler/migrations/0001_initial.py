# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('price', models.IntegerField()),
                ('img', models.ImageField(upload_to='')),
                ('model', models.TextField()),
                ('mark', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=3)),
                ('numberOfItem', models.IntegerField()),
            ],
        ),
    ]
