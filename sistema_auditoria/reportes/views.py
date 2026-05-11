from django.views.generic import TemplateView, View
from django.shortcuts import get_object_or_404
from auditorias.models import Auditoria
from .utils import render_to_pdf
from django.http import HttpResponse

class ReportesListView(TemplateView):
    # ... (keeps existing static reports for UI demo) ...
    template_name = 'reportes/lista.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # We can add dynamic audit list here too
        context['auditorias'] = Auditoria.objects.all()
        return context

class GenerarReporteAuditoriaPDF(View):
    def get(self, request, *args, **kwargs):
        auditoria_id = self.kwargs.get('pk')
        auditoria = get_object_or_404(Auditoria, pk=auditoria_id)
        
        # Obtenemos datos relacionados para el reporte completo
        hallazgos = auditoria.hallazgos.all()
        
        context = {
            'auditoria': auditoria,
            'hallazgos': hallazgos,
            'pagesize': 'A4',
        }
        
        pdf = render_to_pdf('reportes/auditoria_pdf.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = f"Reporte_Auditoria_{auditoria.folio}.pdf"
            content = f"inline; filename={filename}"
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Error al generar PDF", status=400)

