#!/usr/bin/env python2.7

# coding: utf-8

import requests
import re

from bs4 import BeautifulSoup
from collections import defaultdict

def capture_data(url):
    """grab the data from the url"""

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
                             ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                             '50.0.2661.102 Safari/537.36'}

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup.tr.text


def get_minutes(time_string):
    """get the number of minutes the exercise should take"""

    h, m = map(int, time_string.split(':'))
    return h * 60 + m


def workouts(txt):
    """capture the workout and break up into pieces"""

    l = ['SWIM', 'BIKE', 'RUN']
    dd = defaultdict(dict)
    sbr_re = re.compile(r'(%s)\s+(\d+:\d+)' % r'|'.join(l))
    sport = None
    for line in [t for t in txt.splitlines() if t]:
        mo = sbr_re.match(line)
        if mo:
            sport, hmm = mo.groups()
            dd[sport]['minutes'] = get_minutes(hmm)
        if not sport:
            dd['OTHER'].setdefault('workout', []).append(line)
        else:
            dd[sport].setdefault('workout', []).append(line)

    return dd


def capture_day(data, day):
    """capture the workout and break up into pieces"""

    end_tokens = ('^DAILY TOTAL', '^Monday$', '^Tuesday$',
                  '^Wednesday$', '^Thursday$', '^Friday$',
                  '^Saturday$', '^Sunday$')
    end_re = r'(?:%s)' % r'|'.join(end_tokens)
    token = r'%s(.*?)%s' % (day, end_re)
    workout_re = re.compile(token, re.DOTALL | re.MULTILINE)
    mo = workout_re.search(data)
    if mo:
        text = mo.group(1)
    else:
        text = ''
    return text

url = 'http://www.trifuel.com/triathlon/ironman-workouts/weekp05.htm'
data = capture_data(url)
txt = capture_day(data, 'Tuesday')
dd = workouts(txt)