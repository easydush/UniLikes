from django.contrib import admin

# Register your models here.
from .models import Teacher, TeacherSubjectSemester


class TeacherAdmin(admin.ModelAdmin):
    model = Teacher
    list_display = ('surname', 'name', 'patronymic', 'photo_url', 'rating')
    list_filter = ('surname', 'name', 'patronymic')
    ordering = ('surname', 'name', 'rating')


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(TeacherSubjectSemester)
