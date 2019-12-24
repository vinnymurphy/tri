from django.db.models import (
    CharField,
    IntegerField,
    ManyToManyField,
    Model,
    TextField,
)
from django_extensions.db.fields import AutoSlugField

SEASON = (
    ('P', 'Pre-season'),
    ('O', 'Orientation'),
    ('C', 'Competitive'),
    ('T', 'Taper'),
)


class Day(Model):
    """The workout week.  It is broken up into pre-season, orientation,
    competitive and taper.
    """

    def __str__(self):
        return f'{self.day} {self.week_number}'

    WEEK_DAY = (
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday'),
    )
    description = TextField(help_text='describe the day', blank=True)
    day = CharField(max_length=3, choices=WEEK_DAY)
    week_number = IntegerField(help_text='The week number in the season')
    slug = AutoSlugField(populate_from=('day', 'week_number'))

    class Meta:
        ordering = ('week_number', 'day')


class Workout(Model):
    EXERCISE = (('S', 'Swim'), ('B', 'Bike'), ('R', 'Run'))
    name = CharField(max_length=31, help_text='Name of the workout')
    Day = ManyToManyField(Day)
    exercise = CharField(max_length=1, choices=EXERCISE)
    slug = AutoSlugField(populate_from=['exercise', 'name'])
    duration = IntegerField(help_text='How many minutes to complete')
    description = TextField()
