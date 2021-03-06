from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext, gettext_lazy as _


User = get_user_model()

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'country', 'favorite_category')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'first_name', 'last_name', 'country', 'favorite_category'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'country', 'favorite_category', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'favorite_category')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'country', 'favorite_category')