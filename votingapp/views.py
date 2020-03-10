from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from votingapp.forms import UserForm, RateForm
from django.contrib.auth import authenticate, login
from votingapp.models import Student


# Create your views here.
def home(request):
    return redirect(voting_home)


@login_required(login_url='/voting/sign-in/')
def voting_home(request):
    rate_form = RateForm()
    return render(request, 'voting/home.html', {
        'rate_form': rate_form,
    })


def voting_sign_up(request):
    user_form = UserForm()

    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            new_user = Student.objects.create_user(**user_form.cleaned_data)

            login(request, authenticate(
                username=user_form.cleaned_data['username'],
                password=user_form.cleaned_data['password'],
                course=user_form.cleaned_data['course']
            ))

        return redirect(voting_home)

    return render(request, 'voting/sign_up.html', {
        'user_form': user_form,
    })


@login_required(login_url='/voting/sign-in/')
def teacher(request):
    render(request, 'voting/teacher.html')


@login_required(login_url='/voting/sign-in/')
def account(request):
    render(request, 'voting/account.html')
