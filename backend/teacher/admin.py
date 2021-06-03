from django.contrib import admin

from .models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    """
        Teacher administration settings.
    """
    model = Teacher
    list_display = ('surname', 'name', 'patronymic', 'photo_url', 'rating')
    list_filter = ('surname', 'name', 'patronymic')
    ordering = ('surname', 'name', 'rating')


admin.site.register(Teacher, TeacherAdmin)
