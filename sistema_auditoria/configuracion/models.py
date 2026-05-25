from django.db import models
from django.conf import settings

class PreferenciasUsuario(models.Model):
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='preferencias'
    )
    recibir_correos = models.BooleanField(default=True, verbose_name="Recibir Notificaciones por Email")
    tema_oscuro = models.BooleanField(default=True, verbose_name="Tema Oscuro Permanente")

    class Meta:
        verbose_name = 'Preferencia de Usuario'
        verbose_name_plural = 'Preferencias de Usuarios'

    def __str__(self):
        return f"Preferencias de {self.usuario.username}"
