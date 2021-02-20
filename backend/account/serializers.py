from djoser.serializers import UserSerializer
from rest_framework.serializers import ModelSerializer

from .models import User, Teacher, TeacherSubjectCourse


class UserInfoSerializer(UserSerializer):
    class Meta(UserSerializer):
        model = User
        fields = ('email', 'admission_year')


class TeacherInfoSerializer(UserSerializer):
    class Meta(UserSerializer):
        model = Teacher
        fields = ('id', 'surname', 'name', 'patronymic', 'photo_url', 'rating')


class TeacherSubjectCourseInfoSerializer(ModelSerializer):
    class Meta:
        model = TeacherSubjectCourse
        fields = ('teacher', 'subject', 'semester')
