# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-26 22:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='day_number',
            field=models.IntegerField(default=1),
        ),
    ]
