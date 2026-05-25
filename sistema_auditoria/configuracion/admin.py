from django.contrib import admin
from .models import PreferenciasUsuario

@admin.register(PreferenciasUsuario)
class PreferenciasUsuarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'recibir_correos', 'tema_oscuro')
    search_fields = ('usuario__username', 'usuario__email')
    list_filter = ('recibir_correos', 'tema_oscuro')
