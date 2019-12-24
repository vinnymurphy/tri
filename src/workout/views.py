from django.views.generic import DetailView, ListView

from .models import Workout


class WorkoutDetail(DetailView):
    model = Workout


class WorkoutList(ListView):
    model = Workout
