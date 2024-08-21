from django.db import models
import random


class Lesson_duration(models.Model):
    duration= models.CharField(max_length=256)
    
    class Meta:
        verbose_name = ('Dars davomiyligi')
        
        
class Course(models.Model):
    name = models.CharField(max_length=256)
    course_code = models.CharField(default=str(random.randint(10000, 99999)), max_length=150, unique=True)
    lesson_duration = models.ForeignKey(Lesson_duration, on_delete=models.PROTECT)
    course_duration = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    
    class Meta:
        verbose_name = ('Kurs')
        verbose_name_plural = ('Kurslar')
    
    def __str__(self) -> str:
        return self.name