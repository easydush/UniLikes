from django.contrib.auth import get_user_model
from factory import Faker, post_generation
from factory.django import DjangoModelFactory

from teacher.models import Teacher


class UserFactory(DjangoModelFactory):
    email = Faker('email')
    is_superuser = False
    is_active = True
    is_staff = False

    @post_generation
    def password(self, create, extracted, **kwargs):
        password = (extracted
                    if extracted
                    else Faker('password',
                               length=10,
                               special_chars=True,
                               digits=True,
                               upper_case=True,
                               lower_case=True
                               ).evaluate(None, None, extra={'locale': None}))
        self.set_password(password)

    class Meta:
        model = get_user_model()
        django_get_or_create = ['email']


class TeacherFactory(DjangoModelFactory):
    name = Faker('name')
    surname = Faker('name')
    patronymic = Faker('name')

    class Meta:
        model = Teacher
