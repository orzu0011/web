from django.contrib import admin
from .models import Course, Lesson_duration

@admin.register(Lesson_duration)
class Lesson_durationAdmin(admin.ModelAdmin):
    pass

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',) 
    search_fields = ['name', 'course_code']
