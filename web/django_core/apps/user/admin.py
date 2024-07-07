from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, { "fields": ("username", "password") }),
        ("Personal Info", {"fields": ("first_name", "last_name", "email", "bio")}),
        ("Date and time", {"fields": ("last_login", "date_joined")})
    )

    readonly_fields = ("last_login", "date_joined")

# admin.site.register(CustomUser, UserAdmin)
# Unregister Group model since not using permissions
admin.site.unregister(Group)
