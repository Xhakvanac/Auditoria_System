from django.db import models
from django.conf import settings

class Notificacion(models.Model):
    TIPO_CHOICES = [
        ('info', 'Información'),
        ('success', 'Éxito'),
        ('warning', 'Advertencia'),
        ('error', 'Error'),
    ]

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notificaciones')
    titulo = models.CharField(max_length=200)
    mensaje = models.TextField()
    leida = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='info')
    enlace = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ['-fecha_creacion']
        verbose_name = 'Notificación'
        verbose_name_plural = 'Notificaciones'

    def __str__(self):
        return f"{self.titulo} - {self.usuario.username}"
