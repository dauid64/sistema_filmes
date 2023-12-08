from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        labels = {
            'username': 'Usuário',
            'password': 'Senha',
            'email': 'E-mail'
        }
        widgets = {
            'username': forms.TextInput(
            attrs={
                'class': 'form-control'
                }
            ),
            'password': forms.PasswordInput(
            attrs={
                'class': 'form-control'
                }
            ),
            'email': forms.EmailInput(
            attrs={
                'class': 'form-control'
                }
            ),
        }