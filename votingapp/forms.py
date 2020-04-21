from django import forms
from votingapp.models import Student, Rate, Teacher


class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Student
        fields = ('username', 'password', 'course')


class RateForm(forms.ModelForm):
    teacher = forms.ModelChoiceField(queryset=Teacher.objects.all(), widget=forms.HiddenInput)

    class Meta:
        model = Rate
        fields = ('teacher', 'rate')
