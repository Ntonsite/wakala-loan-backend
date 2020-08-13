from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission

from .forms import UserCreationForm, UserChangeForm
from .models import User, Role


@admin.register(User)
class UserProfileAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ('username', 'email', 'first_name', 'middle_name', 'last_name', 'is_staff')
    readonly_fields = ('last_login', 'date_joined')
    search_fields = ('email', 'username', 'first_name', 'middle_name', 'last_name')
    fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('username', 'roles', 'password')
        }),
        ('Personal info', {
            'classes': ('wide', ),
            'fields': ('first_name', 'middle_name', 'last_name',
                       'email')
        }),
        ('Permissions', {
            'classes': ('wide', ),
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Important dates', {
            'classes': ('wide', ),
            'fields': ('last_login', 'date_joined')
        }),
    )

# Adding the Permissions models
admin.site.register(Permission)
admin.site.register(Role)
