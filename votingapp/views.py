from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError, ImproperlyConfigured
from django.http import HttpResponseRedirect, request
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils.encoding import force_text
from django.views import View
from django.views.generic import ListView
from django.views.generic.base import ContextMixin, TemplateResponseMixin
from django.views.generic.edit import ProcessFormView, CreateView

from votingapp.forms import RateForm, StudentForm
from django.contrib.auth import authenticate, login, logout

from votingapp.mixins import AjaxFormMixin
from votingapp.models import Student, Teacher


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {})


def logout_view(request):
    logout(request)
    return redirect('votingapp:index')


def error_500(request):
    return render(request, '500.html', {})


class RegisterView(View):
    def get(self, request):
        return render(request, 'voting/registration.html', {'form': StudentForm()})

    def post(self, request):
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(True)
            form.save_m2m()
            return redirect(reverse('votingapp:login'))

        return render(request, 'voting/registration.html', {'form': form})


class LoginView(View):
    def get(self, request):
        return render(request, 'voting/login.html', {'form': AuthenticationForm})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )

            if user is None:
                return render(
                    request,
                    'voting/login.html',
                    {'form': form, 'invalid_creds': True}
                )

            try:
                form.confirm_login_allowed(user)
            except ValidationError:
                return render(
                    request,
                    'voting/login.html',
                    {'form': form, 'invalid_creds': True}
                )
            login(request, user)

            return redirect(reverse('votingapp:profile'))


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'voting/profile.html', {})


class TeachersList(LoginRequiredMixin, View):
    def get(self, request):
        teachers = Teacher.objects.filter(teachersubjectcourse__semester=int(request.user.semesters[-1]) + 1)
        return render(request, 'voting/teachers_list.html', {'teachers': teachers})


# class VoteView(CreateView):
#     pass


def vote_page(request):
    return render(request, 'voting/voteTest.html')
