

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.contrib.auth.tokens import default_token_generator
from django.core.exceptions import ValidationError
from django.db.models import Q, Avg
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import DetailView, CreateView, TemplateView, FormView
from votingapp.tasks import send_email_task
from UniLikes import settings
from votingapp.forms import StudentForm, PasswordResetForm, PasswordResetRequestForm
from django.contrib.auth import authenticate, login, logout
from votingapp.models import Student, Teacher, TeacherSubjectCourse, Rate, StudTeachRateFact, Subject, UserToken


# Create your views here.
from votingapp.utils import get_semester


def index(request):
    teachers = list(Rate.objects.values('teacher').annotate(rating=Avg('rate') * 100)[:3])

    teachers = sorted(teachers, key=lambda x: x['rating'], reverse=True)
    teacher1 = Teacher.objects.get(id=teachers[0]['teacher'])
    rating1 = int(teachers[0]['rating'])
    teacher2 = Teacher.objects.get(id=teachers[1]['teacher'])
    rating2 = int(teachers[1]['rating'])
    teacher3 = Teacher.objects.get(id=teachers[2]['teacher'])
    rating3 = int(teachers[2]['rating'])
    print(rating2)

    return render(request, 'index.html', {'teacher1': teacher1,
                                          'rating1': rating1,
                                          'teacher2': teacher2,
                                          'rating2': rating2,
                                          'teacher3': teacher3,
                                          'rating3': rating3,
                                          })


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


class StudLoginView(View):
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


class ResetPasswordRequestView(FormView):
    template_name = 'voting/reset.html'
    form_class = PasswordResetRequestForm
    success_url = reverse_lazy('votingapp:reset_redirect_message')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data["email"]
            # find user
            user = Student.objects.get(email=data)
            token_raw = default_token_generator.make_token(user)
            UserToken.objects.create(user=user, token=token_raw)
            reset_password_link = str('http://localhost:8000') + reverse('votingapp:reset',
                                                                         kwargs={
                                                                             'username': user.username,
                                                                             'token': token_raw
                                                                         }
                                                                         )

            send_email_task.delay(
                subject='Reset password',
                to_email=user.email,
                from_email=settings.EMAIL_HOST_USER,
                template='votingapp/reset_message.html',
                args={'url': reset_password_link}
            )
        return self.form_valid(form)


class UserResetPasswordAccessMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        username = kwargs['username']
        user = Student.objects.get(username=username)
        token = kwargs['token']
        try:
            UserToken.objects.get(user=user, token=token)
        except UserToken.DoesNotExist:
            return self.handle_no_permission()

        return super().dispatch(request, *args, **kwargs)


class ResetPasswordView(UserResetPasswordAccessMixin, FormView):
    form_class = PasswordResetForm
    template_name = 'voting/reset_conf.html'
    success_url = reverse_lazy('votingapp:login')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data["password"]
            username = kwargs['username']
            token = kwargs['token']
            user_token = UserToken.objects.get(user__username=username, token=token)

            user = user_token.user
            user.set_password(data)
            user.save()

            user_token.delete()

        return self.form_valid(form)


class MessageSentView(TemplateView):
    template_name = 'voting/message_sent.html'


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'voting/profile.html', {})


class TeachersList(View):
    # all teachers' page
    def get(self, request):
        teachers = Teacher.objects.order_by('surname').all()
        teachers = [{'teacher': x, 'subjects': set(Subject.objects.filter(teachersubjectcourse__teacher=x))}
                    for x in teachers]
        return render(request, 'voting/teachers_list.html', {'teachers': teachers})


class TeacherView(DetailView):
    model = Teacher
    template_name = 'voting/teacher_view.html'


@login_required
def vote_page(request):
    student = Student.objects.get(username=request.user.username)
    curr_semester = get_semester(student.admission_year)
    print(curr_semester)
    voted_teachers = list(
        StudTeachRateFact.objects.filter(Q(semester=curr_semester) & Q(student=student)).only('teacher'))
    voted_teachers = [x.teacher for x in voted_teachers]
    teachers = set(Teacher.objects.filter(teachersubjectcourse__semester=curr_semester))
    teachers = [{'teacher': x, 'subjects': set(Subject.objects.filter(teachersubjectcourse__teacher=x))} for x in
                teachers if
                x not in voted_teachers]
    print(teachers)

    return render(request, 'voting/vote.html', {'teachers': teachers})


def vote_result(request):
    student = Student.objects.get(username=request.user.username)
    teacher = Teacher.objects.get(id=request.POST.get('teacher_id'))
    curr_semester = get_semester(student.admission_year)
    # result handler for AJAX in voting
    rate = request.POST.get('rate')
    print(request.content_params)
    print(teacher, rate)
    rate_fact = StudTeachRateFact(student=student, teacher=teacher, semester=curr_semester)
    rate_fact.save()
    print('saved')
    if rate != -1:
        r = Rate(teacher=teacher, rate=rate)
        r.save()
    return HttpResponse(status=200)
