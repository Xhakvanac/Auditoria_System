from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import PreferenciasUsuario

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def crear_preferencias_usuario(sender, instance, created, **kwargs):
    if created:
        PreferenciasUsuario.objects.create(usuario=instance)
