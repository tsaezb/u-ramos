# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-18 22:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 6, 18, 22, 10, 49, 41609, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
