from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.db.models import Q, F
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView
from django.views.decorators.csrf import csrf_exempt

from votingapp.forms import RateForm, StudentForm
from django.contrib.auth import authenticate, login, logout
from votingapp.models import Student, Teacher, TeacherSubjectCourse, Rate, StudTeachRateFact, Subject


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


class TeachersList(View):
    # all teachers' page
    def get(self, request):
        teachers = Teacher.objects.order_by('surname').all()
        return render(request, 'voting/teachers_list.html', {'teachers': teachers})


class TeacherView(DetailView):
    model = Teacher
    template_name = 'voting/teacher_view.html'


# class VoteView(CreateView):
#     pass

@login_required
def vote_page(request):
    student = Student.objects.get(username=request.user.username)
    curr_sem = int(student.semesters[-1]) + 1

    # teachers = TeacherSubjectCourse.objects.all(
        # Q(semester=curr_sem) & ~Q(studteachratefact__student=student)
        # & ~Q(studteachratefact__semester=curr_sem))
    # )
    # if not teachers:
    #     student.update(semesters=F('semesters') + str(curr_sem))
    #     student.save()
    teacher1 = Teacher(surname="Абрамский", name="Михаил", second_name="Михайлович",
                       photo_url="https://kpfu.ru/portal/docs/F926856215/mYnexRLID9o.jpg")
    teacher2 = Teacher(surname="Ференец", name="Александр", second_name="Андреевич",
                       photo_url="https://shelly.kpfu.ru/e-ksu/docs/F921457479/avatar001.png?rnd=8105")
    subject = Subject(title="Информатика")
    teacher_subject1 = TeacherSubjectCourse(teacher=teacher1, subject=subject)
    teacher_subject2 = TeacherSubjectCourse(teacher=teacher2, subject=subject)
    teachers = []
    for i in range(5):
        teachers.append(teacher_subject1)
        teachers.append(teacher_subject2)
    return render(request, 'voting/voteTest.html', {'teachers': teachers})


def vote_result(request):
    # result handler for AJAX in voting
    rate = request.POST.get('rate')
    print(request.POST)
    if rate != -1:
        teacher_id = request.POST.get('teacher_id')
        # teacher = Teacher.objects.get(id=request.POST.get('teacher_id'))
        print(teacher_id, rate)
        # r = Rate(teacher=teacher, rate=rate)
        # r.save()
        # rate_fact = StudTeachRateFact(student=request.user, teacher=teacher)
        # rate_fact.save()

# def top_teachers(request):
#     teachers = Teacher.objects.ge
