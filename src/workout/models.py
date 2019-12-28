"""http://www.trifuel.com/triathlon/ironman-workouts/week01.htm."""

from django.db.models import (
    CharField,
    IntegerField,
    ManyToManyField,
    Model,
    TextField,
)
from django_extensions.db.fields import AutoSlugField


class Workout(Model):
    """This is our workout.  We have 0 to n workouts per day."""

    EXERCISE = (('S', 'Swim'), ('B', 'Bike'), ('R', 'Run'), ('O', 'Other'))
    INTESITY = (
        ('E', 'EASY'),
        ('M', 'MODERATE'),
        ('T', 'MODERATE2HIGH'),
        ('H', 'HIGH'),
    )
    name = CharField(max_length=31, help_text='Name of the workout')
    slug = AutoSlugField(populate_from=['name', 'exercise', 'duration'])
    exercise = CharField(max_length=1, choices=EXERCISE)
    duration = IntegerField(help_text='How many minutes to complete')
    intensity = CharField(max_length=1, choices=INTESITY)
    description = TextField()


class DailyWorkout(Model):
    """This is our daily workout.  We have 0 to n workouts per day."""

    SEASON = (
        ('P', 'Pre-season'),
        ('O', 'Orientation'),
        ('C', 'Competitive'),
        ('T', 'Taper'),
    )
    sequence = IntegerField()
    week = IntegerField(help_text='The Week number in the Cycle')
    season = CharField(max_length=1, choices=SEASON)
    workout = ManyToManyField(Workout)
    description = TextField()

    def __str__(self):
        return f'season {self.season}: week {self.week} id {self.id}'
