from django import forms
from .models import Hallazgo

class HallazgoForm(forms.ModelForm):
    class Meta:
        model = Hallazgo
        fields = ['auditoria', 'descripcion', 'area', 'criticidad', 'estado']
        widgets = {
            'auditoria': forms.Select(attrs={'class': 'glass-input'}),
            'descripcion': forms.Textarea(attrs={'class': 'glass-input', 'rows': 4, 'placeholder': 'Describa la desviación detectada...'}),
            'area': forms.TextInput(attrs={'class': 'glass-input', 'placeholder': 'Ej. Planta de Producción'}),
            'criticidad': forms.Select(attrs={'class': 'glass-input'}),
            'estado': forms.Select(attrs={'class': 'glass-input'}),
        }
