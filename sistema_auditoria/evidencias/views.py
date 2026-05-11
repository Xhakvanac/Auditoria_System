from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Evidencia
from .forms import EvidenciaForm
from bitacora.utils import registrar_evento

class EvidenciasListView(LoginRequiredMixin, ListView):
    model = Evidencia
    template_name = 'evidencias/lista.html'
    context_object_name = 'lista_evidencias'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_evidencias'] = Evidencia.objects.count()
        return context

class EvidenciaCreateView(LoginRequiredMixin, CreateView):
    model = Evidencia
    form_class = EvidenciaForm
    template_name = 'evidencias/form.html'
    success_url = reverse_lazy('lista_evidencias')

    def form_valid(self, form):
        form.instance.subido_por = self.request.user
        response = super().form_valid(form)
        registrar_evento(
            usuario=self.request.user,
            accion='Carga',
            modulo='Evidencias',
            descripcion=f'Se subió evidencia para la acción ACC-{self.object.accion.id:03d}'
        )
        return response

class EvidenciaDeleteView(LoginRequiredMixin, DeleteView):
    model = Evidencia
    template_name = 'evidencias/confirm_delete.html'
    success_url = reverse_lazy('lista_evidencias')

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        registrar_evento(
            usuario=self.request.user,
            accion='Eliminación',
            modulo='Evidencias',
            descripcion=f'Se eliminó evidencia de la acción ACC-{obj.accion.id:03d}'
        )
        return super().delete(request, *args, **kwargs)
