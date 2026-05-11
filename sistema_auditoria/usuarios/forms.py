from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario

class UsuarioCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ('username', 'email', 'first_name', 'last_name', 'rol')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'glass-input'}),
            'email': forms.EmailInput(attrs={'class': 'glass-input'}),
            'first_name': forms.TextInput(attrs={'class': 'glass-input'}),
            'last_name': forms.TextInput(attrs={'class': 'glass-input'}),
            'rol': forms.Select(attrs={'class': 'glass-input'}),
        }

class UsuarioEditForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'first_name', 'last_name', 'rol', 'is_active')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'glass-input'}),
            'email': forms.EmailInput(attrs={'class': 'glass-input'}),
            'first_name': forms.TextInput(attrs={'class': 'glass-input'}),
            'last_name': forms.TextInput(attrs={'class': 'glass-input'}),
            'rol': forms.Select(attrs={'class': 'glass-input'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'glass-checkbox'}),
        }
