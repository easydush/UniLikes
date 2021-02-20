from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, Teacher, TeacherSubjectCourse


class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('email', 'admission_year', 'is_staff', 'is_active',)
    list_filter = ('email', 'admission_year', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'admission_year')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'admission_year', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


class TeacherAdmin(admin.ModelAdmin):
    model = Teacher
    list_display = ('surname', 'name', 'patronymic', 'photo_url', 'rating')
    list_filter = ('surname', 'name', 'patronymic')
    ordering = ('surname', 'name', 'rating')


admin.site.register(User, UserAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(TeacherSubjectCourse)
