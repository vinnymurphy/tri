from django.urls import path

from .views import WorkoutList, DayList

urlpatterns = [
    path('', WorkoutList.as_view()),
    path('days/', DayList.as_view()),
]
