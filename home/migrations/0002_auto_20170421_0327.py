# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-21 09:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acerca',
            name='actualizacion',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 21, 9, 27, 35, 542118, tzinfo=utc), verbose_name='Ultima actualizacion'),
        ),
    ]
