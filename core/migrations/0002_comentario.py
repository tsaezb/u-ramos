# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-18 22:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=200)),
                ('profe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Profe')),
                ('ramo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Ramo')),
            ],
        ),
    ]
