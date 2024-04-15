from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user_panel.models import CustomUser, Profile


# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff')
    search_fields = ('username', 'email')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_full_name')  # Customize displayed fields
    search_fields = ('user__username', 'user__first_name', 'user__last_name')  # Search by user fields

    def get_full_name(self, obj):
        return obj.user.get_full_name()  # Example custom method for full name
