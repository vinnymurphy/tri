from django.db.models import (
    CharField,
    IntegerField,
    Model,
    SlugField,
    TextField,
)


class Workout(Model):
    EXERCISE = (('S', 'Swim'), ('B', 'Bike'), ('R', 'Run'), ('O', 'Other'))
    INTESITY = (
        ('E', 'EASY'),
        ('M', 'MODERATE'),
        ('T', 'MODERATE2HIGH'),
        ('H', 'HIGH'),
    )
    name = CharField(max_length=31)
    slug = SlugField(max_length=31)
    exercise = CharField(max_length=1, choices=EXERCISE)
    duration = IntegerField(max_length=60)
    intensity = CharField(max_length=1, choices=INTESITY)
    description = TextField()


class DailyWorkout(Model):
    description = TextField(max_length=80)
