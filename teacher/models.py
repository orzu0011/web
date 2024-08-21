from django.db import models


class Teacher(models.Model):
    GENDER = (
        ("Male", "Male"),
        ("Female", "Female"),
    )
    name = models.CharField(max_length=256)
    phone = models.CharField(max_length=256)
    birthday = models.DateField()
    gender = models.CharField(max_length=256, choices=GENDER, blank=True, null=True)
    photo = models.ImageField()
    
