# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-08 18:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_auto_20180108_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='operlogs',
            name='pars',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='参数'),
        ),
    ]
