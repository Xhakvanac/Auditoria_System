from django.db import models
from django.conf import settings

class EventoBitacora(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True,
        verbose_name='Usuario'
    )
    accion = models.CharField(max_length=100, verbose_name='Acción')
    modulo = models.CharField(max_length=50, verbose_name='Módulo')
    descripcion = models.TextField(verbose_name='Descripción Detallada')
    fecha_hora = models.DateTimeField(auto_now_add=True, verbose_name='Fecha y Hora')

    class Meta:
        verbose_name = 'Evento de Bitácora'
        verbose_name_plural = 'Eventos de Bitácora'
        ordering = ['-fecha_hora']

    def __str__(self):
        return f"{self.fecha_hora.strftime('%Y-%m-%d %H:%M')} - {self.usuario} - {self.accion}"
