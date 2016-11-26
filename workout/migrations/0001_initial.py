# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-25 18:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cycle', models.CharField(choices=[('0', 'Orientation'), ('P', 'Pre-season'), ('C', 'Competitive Season'), ('T', 'Taper')], default='P', max_length=1)),
                ('description', models.TextField(help_text='what are we going to accomplish')),
                ('day', models.DateField()),
                ('url', models.URLField()),
                ('week_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(help_text='describe the workout')),
                ('duration', models.IntegerField(help_text='duration in minutes')),
                ('sport', models.CharField(choices=[('S', 'Swim'), ('B', 'Bike'), ('R', 'Run'), ('O', 'Other')], default='O', max_length=1)),
                ('week', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workout.Week')),
            ],
        ),
    ]
