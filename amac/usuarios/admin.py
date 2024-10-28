from django.contrib import admin
from .models import Roles, User

class RolesAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    ordering = ('nombre',)

admin.site.register(Roles, RolesAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'rol')
    list_filter = ('is_staff', 'is_active', 'rol')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    readonly_fields = ('date_joined', 'last_login')

admin.site.register(User, UserAdmin)

# Register your models here.
