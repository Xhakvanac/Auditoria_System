from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Usuario
from .forms import UsuarioCreationForm, UsuarioEditForm
from bitacora.utils import registrar_evento

class AuditLoginView(LoginView):
    """Vista de login con template personalizado glassmorphism."""
    template_name = 'usuarios/login.html'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('dashboard')

class AuditLogoutView(LogoutView):
    """Cierra la sesión y redirige al login."""
    next_page = reverse_lazy('login')

# --- Gestión de Usuarios (Solo Admin) ---

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.rol == 'administrador' or self.request.user.is_superuser

class UsuarioListView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    model = Usuario
    template_name = 'usuarios/lista.html'
    context_object_name = 'lista_usuarios'

class UsuarioCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = Usuario
    form_class = UsuarioCreationForm
    template_name = 'usuarios/form.html'
    success_url = reverse_lazy('lista_usuarios')

    def form_valid(self, form):
        response = super().form_valid(form)
        registrar_evento(
            usuario=self.request.user,
            accion='Creación de Usuario',
            modulo='Usuarios',
            descripcion=f'Se creó el usuario: {self.object.username} con rol {self.object.rol}'
        )
        return response

class UsuarioUpdateView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    model = Usuario
    form_class = UsuarioEditForm
    template_name = 'usuarios/form.html'
    success_url = reverse_lazy('lista_usuarios')

    def form_valid(self, form):
        response = super().form_valid(form)
        registrar_evento(
            usuario=self.request.user,
            accion='Actualización de Usuario',
            modulo='Usuarios',
            descripcion=f'Se actualizó la información del usuario: {self.object.username}'
        )
        return response

class UsuarioDeleteView(LoginRequiredMixin, AdminRequiredMixin, DeleteView):
    model = Usuario
    template_name = 'usuarios/confirm_delete.html'
    success_url = reverse_lazy('lista_usuarios')

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        registrar_evento(
            usuario=self.request.user,
            accion='Eliminación de Usuario',
            modulo='Usuarios',
            descripcion=f'Se eliminó al usuario: {obj.username}'
        )
        return super().delete(request, *args, **kwargs)