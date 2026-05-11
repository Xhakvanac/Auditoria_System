from django.urls import path
from .views import EvidenciasListView, EvidenciaCreateView, EvidenciaDeleteView

urlpatterns = [
    path('', EvidenciasListView.as_view(), name='lista_evidencias'),
    path('subir/', EvidenciaCreateView.as_view(), name='subir_evidencia'),
    path('eliminar/<int:pk>/', EvidenciaDeleteView.as_view(), name='eliminar_evidencia'),
]
