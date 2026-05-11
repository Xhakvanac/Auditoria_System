from django.db import models
from django.conf import settings
from django.utils.text import slugify

class Auditoria(models.Model):
    ESTADO_CHOICES = [
        ('Planeada', 'Planeada'),
        ('En Progreso', 'En Progreso'),
        ('Completada', 'Completada'),
        ('Finalizada', 'Finalizada'),
    ]
    CRITICIDAD_CHOICES = [
        ('Alta', 'Alta'),
        ('Media', 'Media'),
        ('Baja', 'Baja'),
        ('N/A', 'N/A'),
    ]
    
    titulo = models.CharField(max_length=200, verbose_name='Título')
    folio = models.CharField(max_length=100, unique=True, verbose_name='Folio', null=True, blank=True)
    area = models.CharField(max_length=100, verbose_name='Área / Departamento', default='General')
    norma = models.CharField(max_length=100, blank=True, null=True, verbose_name='Norma de Referencia')
    auditor_lider = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='auditorias_lideradas',
        verbose_name='Auditor Líder'
    )
    fecha_inicio = models.DateField(verbose_name='Fecha de Inicio')
    fecha_fin = models.DateField(null=True, blank=True, verbose_name='Fecha de Fin')
    estado = models.CharField(
        max_length=20, 
        choices=ESTADO_CHOICES, 
        default='Planeada',
        verbose_name='Estado'
    )
    criticidad = models.CharField(
        max_length=10, 
        choices=CRITICIDAD_CHOICES, 
        default='N/A',
        verbose_name='Criticidad'
    )
    descripcion = models.TextField(blank=True, verbose_name='Descripción / Objetivo')
    alcance = models.TextField(blank=True, verbose_name='Alcance')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Auditoría'
        verbose_name_plural = 'Auditorías'
        ordering = ['-fecha_inicio']

    def save(self, *args, **kwargs):
        if not self.folio:
            # Asegurar que tenemos fecha_inicio (debería ser obligatoria)
            fecha_str = self.fecha_inicio.strftime('%Y%m%d') if self.fecha_inicio else '00000000'
            
            # Slugificar el título y limpiar
            titulo_slug = slugify(self.titulo)
            if not titulo_slug:
                titulo_slug = "AUDITORIA"
            
            # Generar folio base: AUD-TITULO-FECHA
            # Limitamos el título a 50 caracteres para no exceder los 100 del campo
            base_folio = f"AUD-{titulo_slug[:50]}-{fecha_str}"
            self.folio = base_folio.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.titulo} ({self.estado})"
