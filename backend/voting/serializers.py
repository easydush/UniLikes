from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import TeacherSubjectSemester, RateFact


class TeacherSubjectSemesterInfoSerializer(ModelSerializer):
    class Meta:
        model = TeacherSubjectSemester
        fields = ('teacher', 'subject', 'semester')


class RateFactSerializer(ModelSerializer):
    class Meta:
        model = RateFact
        fields = '__all__'


class NewRateFactSerializer(ModelSerializer):
    teacher_id = serializers.IntegerField()
    rate = serializers.IntegerField()

    class Meta:
        model = RateFact
        fields = ['teacher_id', 'rate']
