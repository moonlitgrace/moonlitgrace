from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import CustomUser, Profile

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, { "fields": ("username", "password") }),
        ("Personal Info", {"fields": ("first_name", "last_name", "email", "bio")}),
        ("Date and time", {"fields": ("last_login", "date_joined")})
    )

    readonly_fields = ("last_login", "date_joined")

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ("name", "aka", "email", "type", "active")
    list_filter = ("name", "active")
    search_fields = ["name"]

    fieldsets = (
        ("Profile Settings", {"fields": ("type", "active")}),
        ("Profile Info", {"fields": ("name", "aka", "email", "bio")}),
        ("Social Links", {"fields": ("github", "discord", "telegram", "twitter")})
    )

# admin.site.register(CustomUser, UserAdmin)
# Unregister Group model since not using permissions
admin.site.unregister(Group)
