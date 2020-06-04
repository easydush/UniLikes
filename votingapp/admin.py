from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from votingapp.forms import StudentForm
from votingapp.models import Teacher, Subject, TeacherSubjectCourse, Rate, Student, StudTeachRateFact, UserToken

# Register your models here.
admin.site.register(Subject)
admin.site.register(Rate)
admin.site.register(Student)
admin.site.register(TeacherSubjectCourse)
admin.site.register(StudTeachRateFact)

admin.site.register(UserToken)

class StudentAdmin(UserAdmin):
    add_form = StudentForm
    form = StudentForm
    model = Student
    list_display = ['email', 'username', 'admission_year', 'semesters']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    empty_value_display = 'no one'
    ordering = ['surname']
    search_fields = ['surname']
