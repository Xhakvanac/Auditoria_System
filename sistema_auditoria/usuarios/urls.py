from django.urls import path
from .views import (
    AuditLoginView, AuditLogoutView, 
    UsuarioListView, UsuarioCreateView, UsuarioUpdateView, UsuarioDeleteView
)

urlpatterns = [
    path('login/', AuditLoginView.as_view(), name='login'),
    path('logout/', AuditLogoutView.as_view(), name='logout'),
    
    # Gestión de Usuarios
    path('lista/', UsuarioListView.as_view(), name='lista_usuarios'),
    path('nuevo/', UsuarioCreateView.as_view(), name='crear_usuario'),
    path('editar/<int:pk>/', UsuarioUpdateView.as_view(), name='editar_usuario'),
    path('eliminar/<int:pk>/', UsuarioDeleteView.as_view(), name='eliminar_usuario'),
]
