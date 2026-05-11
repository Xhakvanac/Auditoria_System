from django.urls import path
from .views import ReportesListView, GenerarReporteAuditoriaPDF

urlpatterns = [
    path('', ReportesListView.as_view(), name='lista_reportes'),
    path('auditoria/<int:pk>/pdf/', GenerarReporteAuditoriaPDF.as_view(), name='reporte_auditoria_pdf'),
]
