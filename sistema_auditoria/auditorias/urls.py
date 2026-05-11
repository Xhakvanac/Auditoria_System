from django.urls import path
from .views import AuditoriasListView, AuditoriaCreateView, AuditoriaUpdateView, AuditoriaDeleteView

urlpatterns = [
    path('', AuditoriasListView.as_view(), name='lista_auditorias'),
    path('nueva/', AuditoriaCreateView.as_view(), name='crear_auditoria'),
    path('editar/<int:pk>/', AuditoriaUpdateView.as_view(), name='editar_auditoria'),
    path('eliminar/<int:pk>/', AuditoriaDeleteView.as_view(), name='eliminar_auditoria'),
]
