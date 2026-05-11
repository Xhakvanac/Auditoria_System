from django import forms
from .models import Auditoria

class AuditoriaForm(forms.ModelForm):
    class Meta:
        model = Auditoria
        fields = ['folio', 'titulo', 'area', 'norma', 'auditor_lider', 'fecha_inicio', 'fecha_fin', 'estado', 'criticidad', 'descripcion', 'alcance']
        widgets = {
            'folio': forms.TextInput(attrs={'class': 'glass-input', 'placeholder': 'Opcional: Se generará automáticamente si se deja vacío'}),
            'titulo': forms.TextInput(attrs={'class': 'glass-input', 'placeholder': 'Ej. Certificación ISO 9001'}),
            'area': forms.TextInput(attrs={'class': 'glass-input', 'placeholder': 'Área auditada'}),
            'norma': forms.TextInput(attrs={'class': 'glass-input', 'placeholder': 'Ej. ISO 9001:2015'}),
            'auditor_lider': forms.Select(attrs={'class': 'glass-input'}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'glass-input', 'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'class': 'glass-input', 'type': 'date'}),
            'estado': forms.Select(attrs={'class': 'glass-input'}),
            'criticidad': forms.Select(attrs={'class': 'glass-input'}),
            'descripcion': forms.Textarea(attrs={'class': 'glass-input', 'rows': 3, 'placeholder': 'Objetivo y descripción de la auditoría...'}),
            'alcance': forms.Textarea(attrs={'class': 'glass-input', 'rows': 3, 'placeholder': 'Describa el alcance de la auditoría...'}),
        }
