from django.db import models
from django.conf import settings
from acciones_correctivas.models import AccionCorrectiva

def evidencia_upload_path(instance, filename):
    # Organiza por ID de acción para evitar colisiones
    return f'evidencias/accion_{instance.accion.id}/{filename}'

class Evidencia(models.Model):
    accion = models.ForeignKey(
        AccionCorrectiva, 
        on_delete=models.CASCADE, 
        related_name='evidencias',
        verbose_name='Acción Correctiva'
    )
    archivo = models.FileField(upload_to=evidencia_upload_path, verbose_name='Archivo de Evidencia')
    descripcion = models.CharField(max_length=255, blank=True, verbose_name='Descripción / Comentario')
    subido_por = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True,
        verbose_name='Subido Por'
    )
    fecha_subida = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Evidencia'
        verbose_name_plural = 'Evidencias'

    def __str__(self):
        return f"Evidencia para ACC-{self.accion.id:03d}"
