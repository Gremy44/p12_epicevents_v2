from django import forms
from .models import User, Role


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63,
                               label="Nom d'utilisateur",
                               widget=forms.TextInput(attrs={"class":"form-control", 
                                                             "id": "floatingInput",
                                                             "placeholder": "Username"})
                               )
    password = forms.CharField(max_length=63,
                               label='Mot de passe',
                               widget=forms.PasswordInput(attrs={"class":"form-control", 
                                                             "id": "floatingPassword",
                                                             "placeholder": "Password"})
                               )

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'role']
        widgets = {
            'role': forms.Select(attrs={'class': 'form-select'})
        }

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['role']