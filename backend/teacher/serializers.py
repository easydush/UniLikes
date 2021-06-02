import logging

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Teacher


class TeacherSerializer(ModelSerializer):
    subjects = serializers.SerializerMethodField('get_subjects')
    rating = serializers.SerializerMethodField('get_rating')

    def get_rating(self, obj):
        logging.info(obj.rating * 100)
        return obj.rating * 100

    def get_subjects(self, obj):
        data = set(obj.subjects_semesters.values_list('subject', flat=True))
        return data

    class Meta:
        model = Teacher
        fields = '__all__'
        include = ['subjects']
