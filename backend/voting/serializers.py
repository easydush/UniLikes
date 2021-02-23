from rest_framework.serializers import ModelSerializer

from .models import Teacher, TeacherSubjectSemester, RateFact


class TeacherInfoSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'surname', 'name', 'patronymic', 'photo_url', 'rating')


class TeacherSubjectSemesterInfoSerializer(ModelSerializer):
    class Meta:
        model = TeacherSubjectSemester
        fields = ('teacher', 'subject', 'semester')


class RateFactSerializer(ModelSerializer):
    class Meta:
        model = RateFact
        fields = '__all__'
