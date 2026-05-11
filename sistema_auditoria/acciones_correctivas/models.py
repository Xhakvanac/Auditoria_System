from django.db import models
from django.conf import settings
from hallazgos.models import Hallazgo

class AccionCorrectiva(models.Model):
    ESTADO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('En Proceso', 'En Proceso'),
        ('Completada', 'Completada'),
        ('Vencida', 'Vencida'),
    ]

    hallazgo = models.ForeignKey(
        Hallazgo, 
        on_delete=models.CASCADE, 
        related_name='acciones',
        verbose_name='Hallazgo Relacionado'
    )
    descripcion = models.TextField(verbose_name='Descripción de la Acción')
    responsable = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True,
        related_name='acciones_asignadas',
        verbose_name='Responsable'
    )
    fecha_compromiso = models.DateField(verbose_name='Fecha Compromiso')
    estado = models.CharField(
        max_length=20, 
        choices=ESTADO_CHOICES, 
        default='Pendiente',
        verbose_name='Estado'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Acción Correctiva'
        verbose_name_plural = 'Acciones Correctivas'
        ordering = ['fecha_compromiso']

    def __str__(self):
        return f"ACC-{self.id:03d}: {self.descripcion[:30]}..."
