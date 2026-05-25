from django.contrib import admin
from .models import Notificacion

@admin.register(Notificacion)
class NotificacionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'usuario', 'tipo', 'leida', 'fecha_creacion')
    list_filter = ('leida', 'tipo', 'fecha_creacion')
    search_fields = ('titulo', 'mensaje', 'usuario__username')
    ordering = ('-fecha_creacion',)
    actions = ['marcar_como_leidas']

    def marcar_como_leidas(self, request, queryset):
        queryset.update(leida=True)
    marcar_como_leidas.short_description = "Marcar notificaciones seleccionadas como leídas"
