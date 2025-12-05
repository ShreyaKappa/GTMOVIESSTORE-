from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Profile

# Create inline admin for Profile
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'

# Extend the existing User admin
class CustomUserAdmin(UserAdmin):
    inlines = [ProfileInline]

# Unregister old User admin, register new one
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
