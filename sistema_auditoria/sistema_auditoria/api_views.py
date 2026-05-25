from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from auditorias.models import Auditoria
from hallazgos.models import Hallazgo
from acciones_correctivas.models import AccionCorrectiva
from evidencias.models import Evidencia

class DashboardAPIView(APIView):
    """
    Endpoint para obtener métricas del dashboard en formato JSON.
    """
    def get(self, request):
        data = {
            'total_auditorias': Auditoria.objects.count(),
            'total_hallazgos': Hallazgo.objects.count(),
            'total_acciones': AccionCorrectiva.objects.count(),
            'total_evidencias': Evidencia.objects.count(),
            'hallazgos_abiertos': Hallazgo.objects.filter(estado='Abierto').count(),
            'hallazgos_revision': Hallazgo.objects.filter(estado__icontains='Revisión').count(),
            'hallazgos_cerrados': Hallazgo.objects.filter(estado='Cerrado').count(),
            'crit_alta': Hallazgo.objects.filter(criticidad='Alta').count(),
            'crit_media': Hallazgo.objects.filter(criticidad='Media').count(),
            'crit_baja': Hallazgo.objects.filter(criticidad='Baja').count(),
        }
        return Response(data, status=status.HTTP_200_OK)

class HallazgosAPIView(APIView):
    """
    Endpoint para obtener el listado de hallazgos.
    """
    def get(self, request):
        hallazgos = Hallazgo.objects.all().order_by('-fecha_reporte')
        data = [
            {
                'id': h.id,
                'descripcion': h.descripcion,
                'area': h.area,
                'criticidad': h.criticidad,
                'estado': h.estado,
                'fecha_reporte': h.fecha_reporte,
            }
            for h in hallazgos
        ]
        return Response(data, status=status.HTTP_200_OK)
