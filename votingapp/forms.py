from django import forms
from django.contrib.auth.forms import UserCreationForm

from votingapp.models import Student, Rate, Teacher
from votingapp.validators import validate_email


class StudentForm(UserCreationForm):
    email = forms.EmailField(validators=[validate_email])

    class Meta:
        model = Student
        fields = ('username', 'email', 'course')


''' password changing is available via celery from email
there are no other changes, that's why there is no need in user change form'''


class RateForm(forms.ModelForm):
    # is it better to use signals?

    class Meta:
        model = Rate
        fields = ('teacher', 'rate')
