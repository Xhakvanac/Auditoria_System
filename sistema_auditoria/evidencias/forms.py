from django import forms
from .models import Evidencia

class EvidenciaForm(forms.ModelForm):
    class Meta:
        model = Evidencia
        fields = ['accion', 'archivo', 'descripcion']
        widgets = {
            'accion': forms.Select(attrs={'class': 'glass-input'}),
            'archivo': forms.FileInput(attrs={'class': 'glass-input'}),
            'descripcion': forms.TextInput(attrs={'class': 'glass-input', 'placeholder': 'Ej. Foto del nuevo extintor'}),
        }
