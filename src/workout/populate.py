#!/usr/bin/env python

from argparse import ArgumentParser
import inflect

from models import Day


def parse_args():
    """Create command line parser
    :return: the arguments
    :rtype: parser.parse_args()
    """
    parser = ArgumentParser(description='populate the database')
    parser.add_argument(
        '-v', '--verbose', action='store_true', default=True, help='Verbose'
    )
    return parser.parse_args()


"""
35     description = TextField(help_text='describe the day', blank=True)
 36     day = CharField(max_length=3, choices=WEEK_DAY)
 37     week_number = IntegerField(help_text='The week number in the season')
 38     slug = AutoSlugField(populate_from=('day', 'week_number'))
 """


def populate(verbose=False):
    import inflect
    p = inflect.engine()
    week = range(1, 37)
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    day_dict = dict(zip(days, ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                               'Friday', 'Saturday', 'Sunday']))
    for w in week:
        for day in days:
            week_describe = p.number_to_words(w)
            description = f'{day_dict[day]} of week {week_describe}'
            d = Day(week_number=w, day=day, description=description)
            d.save()
    for mon in Day.objects.filter(day='Mon', week_number__gt=25, week_number__lt=34):
        mon.description = '''Total day off -- relax and allow your body to rebuild.
Remember, rest with as much intensity as you train!'''
        mon.save()
    for fri in Day.objects.filter(day='Fri', week_number__gt=25, week_number__lt=34):
        fri.description = ''
        fri.save()
        


if __name__ == '__main__':
    args = parse_args()
