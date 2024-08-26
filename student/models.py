from random import choices
from django.db import models
from datetime import date
from django.utils import timezone
import random
# from django.db.models import Sum


class Student(models.Model):
    GENDER = (
        ("Male", "Male"),
        ("Female", "Female"),
    )
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=120)
    wallet = models.IntegerField(default=0)
    token_id = models.CharField(default=str(random.randint(10000000, 99999999)), max_length=150, unique=True)
    gender = models.CharField(max_length=256, choices=GENDER, blank=True, null=True)
    comment = models.TextField(null=True, blank=True)
    extra_phone = models.CharField(max_length=256, blank=True, null=True)
    email = models.EmailField(max_length=256, blank=True, null=True)
    telegram = models.CharField(max_length=256, blank=True, null=True)
    
    def str(self):
        return str(self.full_name)

    # @staticmethod
    # def get_wallet_sums():

    #     negative_wallet_sum = Student.objects.filter(wallet__lt=0).aggregate(Sum('wallet'))['wallet__sum'] or 0
    #     positive_wallet_sum = Student.objects.filter(wallet__gt=0).aggregate(Sum('wallet'))['wallet__sum'] or 0
    #     return negative_wallet_sum, positive_wallet_sum