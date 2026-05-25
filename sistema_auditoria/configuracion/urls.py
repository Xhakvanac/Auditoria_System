from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='perfil/', permanent=False), name='panel_configuracion'),
    path('perfil/', views.perfil_view, name='panel_perfil'),
    path('notificaciones/', views.notificaciones_view, name='panel_notificaciones'),
    path('seguridad/', views.seguridad_view, name='panel_seguridad'),
    path('sistema/', views.sistema_view, name='panel_sistema'),
]
