import random

import pytest

from teacher.models import Teacher


@pytest.mark.django_db
def test_voting_counts_incrementing(authenticated_user):
    """
    Testing method to vote and check that teacher's votes count is changing.
    :param authenticated_user: user authorized by factory (look for the FactoryBoy)
    """
    teacher = Teacher.objects.last()
    rate = random.choice([0, 1])
    response = authenticated_user.post('http://localhost:8000/api/voting/', {'teacher_id': teacher.id, 'rate': rate},
                                       format='json')
    updated_teacher = Teacher.objects.last()
    assert teacher.vote_counts != updated_teacher.vote_counts


@pytest.mark.django_db
def test_voting_rating_changing(authenticated_user):
    """
Testing method to vote and check that teacher's votes rating is changing.
    :param authenticated_user: user authorized by factory (look for the FactoryBoy)
    """
    teacher = Teacher.objects.last()
    for i in range(3):
        rate = i % 2
        response = authenticated_user.post('http://localhost:8000/api/voting/',
                                           {'teacher_id': teacher.id, 'rate': rate},
                                           format='json')
    updated_teacher = Teacher.objects.last()
    assert teacher.rating != updated_teacher.rating
