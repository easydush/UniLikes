from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Teacher


class TeacherSerializer(ModelSerializer):
    subjects = serializers.SerializerMethodField('get_subjects')

    def get_subjects(self, obj):
        data = set(obj.subjects_semesters.values_list('subject', flat=True))
        return data

    class Meta:
        model = Teacher
        fields = ('id', 'surname', 'name', 'patronymic', 'photo_url', 'rating', 'subjects')
