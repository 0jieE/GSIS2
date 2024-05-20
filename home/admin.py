from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Administrator_user, Staff_user, Student_user

class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('username', 'first_name','last_name')
    list_filter = ('username', 'first_name', 'administrator','staff','student',)
    ordering = ('username',)
    list_display = ('username', 'first_name','middle_name','last_name',
                    'is_superuser','is_active', 'is_staff','administrator','staff','student')
    fieldsets = (
        (None, {'fields': ('id_no','email', 'username', 'first_name','middle_name','last_name',)}),
        ('Permissions', {'fields': ('is_superuser','is_staff', 'is_active','administrator','staff','student')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name','middle_name','last_name', 'password1', 'password2',)}),
    )

class Administrator_user_config(UserAdmin):
    model = User
    list_display = ('user',)
    fieldsets = (
        (None, {'fields': ('id_no','email', 'username', 'first_name','middle_name','last_name',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('id_no','username', 'first_name','middle_name','last_name', 'password1', 'password2',)}
         ),
    )

admin.site.register(User,UserAdminConfig)

admin.site.register(Administrator_user, Administrator_user_config)