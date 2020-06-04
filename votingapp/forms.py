from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, Form, EmailField, CharField, PasswordInput

from votingapp.models import Student, Rate, Teacher
from votingapp.validators import validate_email


class StudentForm(UserCreationForm):
    email = forms.EmailField(validators=[validate_email])

    class Meta:
        model = Student
        fields = ('username', 'password1', 'password2', 'email', 'admission')

    def save(self, commit=True):
        user = super(StudentForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class LoginForm(ModelForm):
    class Meta:
        model = Student
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Login'))
        self.helper.form_method = 'post'


class PasswordResetRequestForm(Form):
    email = EmailField(label="Email", max_length=254, validators=[validate_email])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Send email'))
        self.helper.form_method = 'post'


class PasswordResetForm(Form):
    password = CharField(label="New Password", max_length=254, widget=PasswordInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Save'))
        self.helper.form_method = 'post'


''' password changing is available via celery from email
there are no other changes, that's why there is no need in user change form'''


class RateForm(forms.ModelForm):
    # is it better to use signals?

    class Meta:
        model = Rate
        fields = ('teacher', 'rate')
