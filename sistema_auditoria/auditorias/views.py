from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Auditoria
from .forms import AuditoriaForm
from bitacora.utils import registrar_evento

class AuditoriasListView(LoginRequiredMixin, ListView):
    model = Auditoria
    template_name = 'auditorias/lista.html'
    context_object_name = 'lista_auditorias'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Podríamos agregar KPIs aquí
        context['total_auditorias'] = Auditoria.objects.count()
        context['en_progreso'] = Auditoria.objects.filter(estado='En Progreso').count()
        return context

class AuditoriaCreateView(LoginRequiredMixin, CreateView):
    model = Auditoria
    form_class = AuditoriaForm
    template_name = 'auditorias/form.html'
    success_url = reverse_lazy('lista_auditorias')

    def form_valid(self, form):
        response = super().form_valid(form)
        registrar_evento(
            usuario=self.request.user,
            accion='Creación',
            modulo='Auditorías',
            descripcion=f'Se creó la auditoría: {self.object.titulo}'
        )
        return response

class AuditoriaUpdateView(LoginRequiredMixin, UpdateView):
    model = Auditoria
    form_class = AuditoriaForm
    template_name = 'auditorias/form.html'
    success_url = reverse_lazy('lista_auditorias')

    def form_valid(self, form):
        response = super().form_valid(form)
        registrar_evento(
            usuario=self.request.user,
            accion='Actualización',
            modulo='Auditorías',
            descripcion=f'Se actualizó la auditoría: {self.object.titulo}'
        )
        return response

class AuditoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Auditoria
    template_name = 'auditorias/confirm_delete.html'
    success_url = reverse_lazy('lista_auditorias')

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        registrar_evento(
            usuario=self.request.user,
            accion='Eliminación',
            modulo='Auditorías',
            descripcion=f'Se eliminó la auditoría: {obj.titulo}'
        )
        return super().delete(request, *args, **kwargs)
