from django.db import models
from django.conf import settings
from auditorias.models import Auditoria

class Hallazgo(models.Model):
    CRITICIDAD_CHOICES = [
        ('Alta', 'Alta'),
        ('Media', 'Media'),
        ('Baja', 'Baja'),
    ]
    ESTADO_CHOICES = [
        ('Abierto', 'Abierto'),
        ('En Revisión (Evidencia)', 'En Revisión (Evidencia)'),
        ('Cerrado', 'Cerrado'),
    ]

    auditoria = models.ForeignKey(
        Auditoria, 
        on_delete=models.CASCADE, 
        related_name='hallazgos',
        verbose_name='Auditoría Relacionada'
    )
    descripcion = models.TextField(verbose_name='Descripción del Hallazgo')
    area = models.CharField(max_length=150, verbose_name='Área / Departamento')
    criticidad = models.CharField(
        max_length=10, 
        choices=CRITICIDAD_CHOICES, 
        verbose_name='Criticidad'
    )
    estado = models.CharField(
        max_length=30, 
        choices=ESTADO_CHOICES, 
        default='Abierto',
        verbose_name='Estado'
    )
    fecha_reporte = models.DateField(auto_now_add=True, verbose_name='Fecha de Reporte')
    reportado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True,
        verbose_name='Reportado Por'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Hallazgo'
        verbose_name_plural = 'Hallazgos'
        ordering = ['-fecha_reporte']

    def __str__(self):
        return f"HLZ-{self.id:03d}: {self.descripcion[:30]}..."
