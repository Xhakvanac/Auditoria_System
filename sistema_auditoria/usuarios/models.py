from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ROL_CHOICES = [
        ('administrador', 'Administrador'),
        ('auditor_lider', 'Auditor Líder'),
        ('auditor', 'Auditor'),
        ('auditado', 'Auditado'),
    ]
    rol = models.CharField(
        max_length=20,
        choices=ROL_CHOICES,
        default='auditado',
        verbose_name='Rol'
    )
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    def get_rol_display_icon(self):
        icons = {
            'administrador': 'bx-shield-alt-2',
            'auditor_lider': 'bx-star',
            'auditor': 'bx-search-alt',
            'auditado': 'bx-user',
        }
        return icons.get(self.rol, 'bx-user')
    def __str__(self):
        return f"{self.get_full_name() or self.username} ({self.get_rol_display()})"
