# vim: sw=4 ai sm expandtab
from __future__ import unicode_literals

from django.db import models


class Week(models.Model):
    CYCLE = (
        ('0', 'Orientation'),
        ('P', 'Pre-season'),
        ('C', 'Competitive Season'),
        ('T', 'Taper'),
    )
    cycle = models.CharField(max_length=1, choices=CYCLE,
                             default="P")
    description = models.TextField(
        help_text="what are we going to accomplish")
    day = models.DateField()
    url = models.URLField()
    week_number = models.IntegerField()

    def __str__(self):
        return '%s Week %s' % (self.cycle, self.week_number)


class Workout(models.Model):
    SPORT = (
        ('S', 'Swim'),
        ('B', 'Bike'),
        ('R', 'Run'),
        ('O', 'Other'),
    )
    week = models.ForeignKey(Week)
    day_number = models.IntegerField(default=1)
    description = models.TextField(
        help_text="describe the workout")
    duration = models.IntegerField(
        help_text="duration in minutes")
    sport = models.CharField(max_length=1,
                             choices=SPORT,
                             default='O')
