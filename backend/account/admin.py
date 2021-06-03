from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


class UserAdmin(BaseUserAdmin):
    """
        User administration settings.
    """
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


admin.site.register(User, UserAdmin)
