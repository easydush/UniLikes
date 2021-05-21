import pytest
import environ
import sys

from ..UniLikes import settings

env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env()
from .factories import UserFactory, TeacherFactory
from rest_framework.test import APIClient

@pytest.fixture
def user():
    return UserFactory()


@pytest.fixture
def teacher():
    return TeacherFactory()


@pytest.fixture
def authenticated_user(user):
    api_client = APIClient()
    api_client.force_authenticate(user=user)
    return api_client


@pytest.fixture(scope='session')
def django_db_setup():
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
