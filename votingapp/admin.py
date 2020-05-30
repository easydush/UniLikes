from django.contrib import admin
from votingapp.models import Teacher, Subject, TeacherSubjectCourse, Rate, Student, StudTeachRateFact

# Register your models here.
admin.site.register(Subject)
admin.site.register(Rate)
admin.site.register(Student)
admin.site.register(TeacherSubjectCourse)
admin.site.register(StudTeachRateFact)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    empty_value_display = 'no one'
    ordering = ['surname']
    search_fields = ['surname']
