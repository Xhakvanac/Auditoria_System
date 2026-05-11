from django.views.generic import TemplateView
from auditorias.models import Auditoria
from hallazgos.models import Hallazgo
from acciones_correctivas.models import AccionCorrectiva
from evidencias.models import Evidencia

class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Estadísticas básicas
        context['total_auditorias'] = Auditoria.objects.count()
        context['total_hallazgos'] = Hallazgo.objects.count()
        context['total_acciones'] = AccionCorrectiva.objects.count()
        context['total_evidencias'] = Evidencia.objects.count()
        
        # Datos para Gráfica de Estados (Hallazgos)
        context['hallazgos_abiertos'] = Hallazgo.objects.filter(estado='Abierto').count()
        context['hallazgos_revision'] = Hallazgo.objects.filter(estado__icontains='Revisión').count()
        context['hallazgos_cerrados'] = Hallazgo.objects.filter(estado='Cerrado').count()

        # Datos para Gráfica de Criticidad
        context['crit_alta'] = Hallazgo.objects.filter(criticidad='Alta').count()
        context['crit_media'] = Hallazgo.objects.filter(criticidad='Media').count()
        context['crit_baja'] = Hallazgo.objects.filter(criticidad='Baja').count()

        # Últimas auditorías para la vista rápida
        context['ultimas_auditorias'] = Auditoria.objects.all().order_by('-fecha_inicio')[:5]
        return context
