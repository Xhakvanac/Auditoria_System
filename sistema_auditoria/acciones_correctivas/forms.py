from django import forms
from .models import AccionCorrectiva

class AccionCorrectivaForm(forms.ModelForm):
    class Meta:
        model = AccionCorrectiva
        fields = ['hallazgo', 'descripcion', 'responsable', 'fecha_compromiso', 'estado']
        widgets = {
            'hallazgo': forms.Select(attrs={'class': 'glass-input'}),
            'descripcion': forms.Textarea(attrs={'class': 'glass-input', 'rows': 4, 'placeholder': 'Describa la acción a realizar...'}),
            'responsable': forms.Select(attrs={'class': 'glass-input'}),
            'fecha_compromiso': forms.DateInput(attrs={'class': 'glass-input', 'type': 'date'}),
            'estado': forms.Select(attrs={'class': 'glass-input'}),
        }
