from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser  # Import your custom user model
from .forms import CustomUserCreationForm, CustomUserChangeForm
# Register your models here.
class customModelAdmin(admin.ModelAdmin):
    from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser  # Import your custom user model
from .forms import CustomUserCreationForm, CustomUserChangeForm  # Import custom forms if you have them

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'date_of_birth', 'is_staff', 'is_active', 'username', 'role']
    list_filter = ['is_staff', 'is_active', 'role']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('date_of_birth', 'profile_photo', 'role')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'date_of_birth', 'password1', 'password2', 'is_staff', 'is_active', 'role', 'profile_photo'),
        }),
    )
    search_fields = ['email', 'date_of_birth']
    ordering = ['email']

    filter_horizontal = ('groups', 'user_permissions')

admin.site.register(CustomUser, CustomUserAdmin)