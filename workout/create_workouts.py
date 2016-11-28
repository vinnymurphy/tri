#!/usr/bin/env python2.7

# coding: utf-8
# vim: sw=4 ai sm expandtab

import django
import os
import re
import requests
import sys

proj_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tri.settings")
sys.path.append(proj_path)
# This is so my local_settings.py gets loaded.
os.chdir(proj_path)

# This is so models get loaded.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from bs4 import BeautifulSoup
from collections import defaultdict

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from django.conf import settings

def weekly_urls():
    'get all the urls'

    url = 'http://www.trifuel.com/triathlon/ironman-workouts/'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
                             ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                             '50.0.2661.102 Safari/537.36'}
    r = requests.get(url, headers=headers)
    url_re = re.compile(r'(?:week\w?|taper)\d+\.htm')
    base_url = r.url
    soup = BeautifulSoup(r.content, 'html.parser')
    urls = [u['href'] for u in soup.find_all('a') if url_re.search(u['href'])]
    l = []
    l.extend(sorted([u for u in urls if re.search(r'week\d+.htm', u)]))
    l.extend(sorted([u for u in urls if re.search(r'weekp\d+.htm', u)]))
    l.extend(sorted([u for u in urls if re.search(r'weekc\d+.htm', u)]))
    l.extend(sorted([u for u in urls if re.search(r'taper\d+.htm', u)]))
    return l


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

if __name__ == '__main__':
    url = 'http://www.trifuel.com/triathlon/ironman-workouts/weekp05.htm'
    data = capture_data(url)
    txt = capture_day(data, 'Tuesday')
    dd = workouts(txt)
    print dd
