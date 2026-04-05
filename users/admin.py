
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'role', 'is_active'),
        }),
    )

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('email',)}),
        ('Role Info', {'fields': ('role',)}),
        ('Status', {'fields': ('is_active',)}),
    )

    list_display = ('username', 'role', 'is_active')
    exclude = ('groups', 'user_permissions', 'last_login', 'date_joined')

admin.site.register(User, CustomUserAdmin)
