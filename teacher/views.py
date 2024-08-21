from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TeacherSerializer
from .models import Teacher


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    