from django.contrib import admin
from .models import User, Role
from django import forms

class UserAdminForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

class UserAdmin(admin.ModelAdmin):
    form = UserAdminForm  # Associer le formulaire personnalisé à UserAdmin
    list_display = ('username', 'first_name', 'last_name', 'email', 'role')
    list_filter = ('role',)
    search_fields = ('username', 'first_name', 'last_name', 'email')

class RoleAdmin(admin.ModelAdmin):
    list_display = ('role',)

admin.site.register(User, UserAdmin)
admin.site.register(Role, RoleAdmin)
