import random

import pytest

from teacher.models import Teacher


@pytest.mark.django_db
def test_voting(authenticated_user):
    teacher = Teacher.objects.last()
    rate = random.choice([0, 1])
    response = authenticated_user.post('http://localhost:8000/api/voting/', {'teacher_id': teacher.id, 'rate': rate},
                                       format='json')
    updated_teacher = Teacher.objects.last()
    assert teacher.vote_counts != updated_teacher.vote_counts
