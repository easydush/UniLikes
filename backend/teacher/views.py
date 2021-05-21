from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import Teacher
from .serializers import TeacherSerializer


class TeacherViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing teachers.
    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer