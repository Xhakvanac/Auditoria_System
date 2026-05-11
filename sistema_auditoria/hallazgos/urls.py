from django.urls import path
from .views import HallazgosListView, HallazgoCreateView, HallazgoUpdateView, HallazgoDeleteView

urlpatterns = [
    path('', HallazgosListView.as_view(), name='lista_hallazgos'),
    path('nuevo/', HallazgoCreateView.as_view(), name='crear_hallazgo'),
    path('editar/<int:pk>/', HallazgoUpdateView.as_view(), name='editar_hallazgo'),
    path('eliminar/<int:pk>/', HallazgoDeleteView.as_view(), name='eliminar_hallazgo'),
]
