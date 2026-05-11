from django.contrib import admin
from .models import Auditoria

@admin.register(Auditoria)
class AuditoriaAdmin(admin.ModelAdmin):
    list_display = ('folio', 'titulo', 'area', 'estado', 'fecha_inicio')
    list_filter = ('estado', 'area', 'criticidad')
    search_fields = ('titulo', 'folio', 'area')
