from django.contrib import admin

from .models import Day, Workout


@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    exclude = ('slug',)


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name',)
    exclude = ('slug',)

