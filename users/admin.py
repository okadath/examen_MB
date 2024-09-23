from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ( 'age', 'phone')}),
    )
    list_display = ['username', 'first_name', 'last_name',  'email', 'age', 'phone']

admin.site.register(CustomUser, CustomUserAdmin)
