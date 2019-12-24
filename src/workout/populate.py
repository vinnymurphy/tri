#!/usr/bin/env python

from argparse import ArgumentParser

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


def populate(verbose=False):
    week = range(1, 37)
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    for w in week:
        for day in days:
            d = Day(week_number=w, day=day)
            d.save()


if __name__ == '__main__':
    args = parse_args()
