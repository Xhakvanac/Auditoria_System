from django import forms
from django.contrib.auth import get_user_model
from .models import PreferenciasUsuario

Usuario = get_user_model()

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'email']

class PreferenciasForm(forms.ModelForm):
    class Meta:
        model = PreferenciasUsuario
        fields = ['recibir_correos', 'tema_oscuro']
