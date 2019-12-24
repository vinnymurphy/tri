from django.contrib import admin

from .models import Day, Workout

admin.site.register(Day)

@admin.register(Workout)
class DayAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
