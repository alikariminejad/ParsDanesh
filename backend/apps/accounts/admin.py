from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Department, User
from django.http import HttpRequest

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    search_fields = ["name", "slug"]

@admin.register(User)
class CustomeUserAdmin(UserAdmin):
    model = User
    list_display = ["email", "full_name", "role", "clearance_level", "primary_department", "is_staff"]
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('full_name','primary_department')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions', 'groups')}),)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'full_name'),}),)
    ordering = ('email',)
    def get_queryset(self, request: HttpRequest):
        return super().get_queryset(request).select_related('primary_department')