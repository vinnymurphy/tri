#!/usr/bin/env python

from argparse import ArgumentParser
import inflect
<<<<<<< HEAD

from models import Day
=======
import re
import requests

from bs4 import BeautifulSoup
# from models import Day
>>>>>>> 7de5fc4


def parse_args():
    """Create command line parser
    :return: the arguments
    :rtype: parser.parse_args()
    """
    parser = ArgumentParser(description='populate the database')
    parser.add_argument(
<<<<<<< HEAD
=======
        '-u', '--url', type=str, required=True, help='The url from trifuel'
    )
    parser.add_argument(
>>>>>>> 7de5fc4
        '-v', '--verbose', action='store_true', default=True, help='Verbose'
    )
    return parser.parse_args()


<<<<<<< HEAD
"""
35     description = TextField(help_text='describe the day', blank=True)
 36     day = CharField(max_length=3, choices=WEEK_DAY)
 37     week_number = IntegerField(help_text='The week number in the season')
 38     slug = AutoSlugField(populate_from=('day', 'week_number'))
 """


def populate(verbose=False):
=======
def populate(verbose=False):
    import inflect
>>>>>>> 7de5fc4
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
<<<<<<< HEAD
=======
    for mon in Day.objects.filter(day='Mon', week_number__gt=25, week_number__lt=34):
        mon.description = '''Total day off -- relax and allow your body to rebuild.
Remember, rest with as much intensity as you train!'''
        mon.save()
    for fri in Day.objects.filter(day='Fri', week_number__gt=25, week_number__lt=34):
        fri.description = ''
        fri.save()
        

def get_duration(txt):
    mo = re.match('^.*?(\d+:\d+)\s*$', txt)
    duration = 0
    if mo:
        hour, minute = map(int, mo.group(1).split(':'))
        duration = hour * 60 + minute
    return duration
    
def parse_trifuel(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, features="lxml")
    lines = [t for t in soup.text.splitlines() if t]
    exercise_re = re.compile(r'^(SWIM|BIKE|RUN).*')
    terminators = ('DAILY TOTAL:', 'WEEK-TO-DATE')
    from collections import defaultdict
    dd = defaultdict(list)
    in_workout, day, exercise = False, '', ''
    workout = list()
    for line in lines:
        if line.strip().startswith(days):
            if ',' in line.strip():
                day = line.strip().split(',')[0].strip()
            else:
                day = line.strip()
            
            workout = []
            continue
        if line.startswith(terminators):
            in_workout = False
            if workout:
                dd[day].append({exercise: workout, 'duration': duration})
            duration = 0
            workout = []
            continue
    
        mo = exercise_re.match(line)
        if mo:
            if exercise:
                if workout:
                    dd[day].append({exercise: workout, 'duration': duration})
                    workout = []
            exercise = mo.group(1)
            duration = get_duration(line)
            in_workout = True
            continue
        if in_workout:
            workout.append(line)
    return dd

    
days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')


def workout(week_num, text, event):
    pass
>>>>>>> 7de5fc4


if __name__ == '__main__':
    args = parse_args()
<<<<<<< HEAD
=======
    week = parse_trifuel(args.url)
    from pprint import pprint
    for day in days:
        print(f'{day}')
        try:
            for d in week[day]:
                exercise = [k for k in d.keys() if k != 'duration'].pop()
                print(f'Duration {d["duration"]} minutes for {exercise}')
                print('{0}'.format('\n'.join(d[exercise])))
        except KeyError:
            pass


#    fifteen = parse_trifuel('http://www.trifuel.com/triathlon/ironman-workouts/weekp15.htm')
>>>>>>> 7de5fc4
