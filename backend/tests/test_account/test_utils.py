import pytest
import datetime as dt

from account.models import User

from account.utils import get_semester


@pytest.mark.django_db
def test_semester_calculating(authenticated_user):
    """
        Testing that semester is calculating correctly. In test: abstract 1 year bachelor student.
        :param authenticated_user: user authorized by factory (look for the FactoryBoy)
    """
    test_year = dt.datetime.today().year - 1
    test_user = User.objects.create(email='student@stud.kpfu.ru', password='password', admission_year=test_year)
    assert 1 <= get_semester(test_user.admission_year) <= 2
