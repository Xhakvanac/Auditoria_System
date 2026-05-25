from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_notificaciones, name='lista_notificaciones'),
    path('marcar-leida/<int:notificacion_id>/', views.marcar_leida, name='marcar_leida_notificacion'),
    path('marcar-todas-leidas/', views.marcar_todas_leidas, name='marcar_todas_notificaciones_leidas'),
]
