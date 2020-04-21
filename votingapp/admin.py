from django.contrib import admin
from votingapp.models import Teacher, Subject, CourseSubject, Rate

# Register your models here.
admin.site.register(Subject)
admin.site.register(Rate)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    empty_value_display = 'it is empty'
    fields = ('surname', 'name')
    ordering = ['surname']
    search_fields = ['surname']


@admin.register(CourseSubject)
class CourseSubjectAdmin(admin.ModelAdmin):
    filter_vertical = ['teacher']
