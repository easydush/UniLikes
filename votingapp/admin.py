from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from votingapp.forms import StudentForm
from votingapp.models import Teacher, Subject, TeacherSubjectCourse, Rate, Student, StudTeachRateFact, UserToken, \
    AdmissionYear

# Register your models here.
admin.site.register(Subject)
admin.site.register(Rate)
admin.site.register(Student)
admin.site.register(StudTeachRateFact)
admin.site.register(AdmissionYear)

admin.site.register(UserToken)


class StudentAdmin(UserAdmin):
    add_form = StudentForm
    form = StudentForm
    model = Student
    list_display = ['email', 'username', 'admission_year', 'semesters']
    ordering = ['surname']
    search_fields = ['surname']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    empty_value_display = 'no one'
    ordering = ['surname']
    search_fields = ['surname']


@admin.register(TeacherSubjectCourse)
class TeacherSubjectAdmin(admin.ModelAdmin):
    empty_value_display = 'no one'
    ordering = ['teacher__surname']
    search_fields = ['teacher__surname']
