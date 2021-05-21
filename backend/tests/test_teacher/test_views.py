import os
#
# from requests.auth import HTTPBasicAuth
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "UniLikes.settings")
# from django.core.wsgi import get_wsgi_application
#
# application = get_wsgi_application()
import pytest

from teacher.models import Teacher


@pytest.mark.django_db
def test_create_teacher(teacher):
    Teacher.objects.create(name=teacher.name, surname=teacher.surname, patronymic=teacher.patronymic)
    created = Teacher.objects.last()
    assert teacher.name == created.name


@pytest.mark.django_db
def test_list_teacher(authenticated_user):
    teachers_count = authenticated_user.get("http://localhost:8000/api/teacher/").data.get('count')
    query_teachers_count = Teacher.objects.count()
    assert teachers_count == query_teachers_count
