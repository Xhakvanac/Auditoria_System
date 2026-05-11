from django.urls import path
from .views import AccionesListView, AccionCreateView, AccionUpdateView, AccionDeleteView

urlpatterns = [
    path('', AccionesListView.as_view(), name='lista_acciones'),
    path('nueva/', AccionCreateView.as_view(), name='crear_accion'),
    path('editar/<int:pk>/', AccionUpdateView.as_view(), name='editar_accion'),
    path('eliminar/<int:pk>/', AccionDeleteView.as_view(), name='eliminar_accion'),
]
