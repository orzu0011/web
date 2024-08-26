from django.db import models 
from course.models import Course
from teacher.models import Teacher
from other.models import Room

class Groups(models.Model):
    DAYS = (
        ('mon_wed_fri', "Monday, Wednesday, Friday"),
        ('tue_thu_sat', "Tuesday, Thursday, Saturday"),
        ('everyday', "Everyday"),
    )
    name = models.CharField(max_length=256)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    days = models.CharField(max_length=256, choices=DAYS)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    time = models.TimeField()
    start_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Guruh"
        verbose_name_plural = "Guruhlar"
