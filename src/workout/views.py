from django.shortcuts import render
from django.views.generic import ListView

from .models import Workout, Day


class WorkoutList(ListView):
    model = Workout

class DayList(ListView):
    model = Day
