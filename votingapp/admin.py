from django.contrib import admin
from votingapp.models import Teacher, Subject, TeacherSubjectCourse, Rate, Student

# Register your models here.
admin.site.register(Subject)
admin.site.register(Rate)
admin.site.register(Student)
admin.site.register(TeacherSubjectCourse)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    empty_value_display = 'no one'
    ordering = ['surname']
    search_fields = ['surname']
