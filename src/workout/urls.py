from django.urls import path

from .views import WorkoutDetail, WorkoutList

urlpatterns = [
    path('<slug:slug>/', WorkoutDetail.as_view(), name='workout_detail'),
    path('', WorkoutList.as_view(), name='workout_list'),
]
