from django.contrib import admin
from .models import Teacher


@admin.register(Teacher)
class Teacher(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',) 
    search_fields = ['name',]
