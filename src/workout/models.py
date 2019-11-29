from django.db.models import (
    CharField,
    IntegerField,
    Model,
    SlugField,
    TextField,
    ManyToManyField,
)


class Workout(Model):
    EXERCISE = (('S', 'Swim'), ('B', 'Bike'), ('R', 'Run'), ('O', 'Other'))
    INTESITY = (
        ('E', 'EASY'),
        ('M', 'MODERATE'),
        ('T', 'MODERATE2HIGH'),
        ('H', 'HIGH'),
    )
    name = CharField(max_length=31, help_text='Name of the workout')
    slug = SlugField(max_length=31)
    exercise = CharField(max_length=1, choices=EXERCISE)
    duration = IntegerField(help_text='How many minutes to complete')
    intensity = CharField(max_length=1, choices=INTESITY)
    description = TextField()


class DailyWorkout(Model):
    SEASON = (
        ('P', 'Pre-season'),
        ('O', 'Orientation'),
        ('C', 'Competitive'),
        ('T', 'Taper'),
    )
    sequence = IntegerField(help_text='The cycle number for the season')
    week = IntegerField(help_text='The Week number in the Cycle')
    season = CharField(max_length=1, choices=SEASON)
    workout = ManyToManyField(Workout)
    description = TextField()
