from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Hallazgo
from .forms import HallazgoForm
from bitacora.utils import registrar_evento

class HallazgosListView(LoginRequiredMixin, ListView):
    model = Hallazgo
    template_name = 'hallazgos/lista.html'
    context_object_name = 'lista_hallazgos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['abiertos'] = Hallazgo.objects.filter(estado='Abierto').count()
        context['en_revision'] = Hallazgo.objects.filter(estado__icontains='Revisión').count()
        return context

class HallazgoCreateView(LoginRequiredMixin, CreateView):
    model = Hallazgo
    form_class = HallazgoForm
    template_name = 'hallazgos/form.html'
    success_url = reverse_lazy('lista_hallazgos')

    def form_valid(self, form):
        form.instance.reportado_por = self.request.user
        response = super().form_valid(form)
        registrar_evento(
            usuario=self.request.user,
            accion='Reporte',
            modulo='Hallazgos',
            descripcion=f'Se reportó un nuevo hallazgo: {self.object.descripcion[:50]}...'
        )
        return response

class HallazgoUpdateView(LoginRequiredMixin, UpdateView):
    model = Hallazgo
    form_class = HallazgoForm
    template_name = 'hallazgos/form.html'
    success_url = reverse_lazy('lista_hallazgos')

    def form_valid(self, form):
        response = super().form_valid(form)
        registrar_evento(
            usuario=self.request.user,
            accion='Actualización',
            modulo='Hallazgos',
            descripcion=f'Se actualizó el hallazgo HLZ-{self.object.id:03d}'
        )
        return response

class HallazgoDeleteView(LoginRequiredMixin, DeleteView):
    model = Hallazgo
    template_name = 'hallazgos/confirm_delete.html'
    success_url = reverse_lazy('lista_hallazgos')

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        registrar_evento(
            usuario=self.request.user,
            accion='Eliminación',
            modulo='Hallazgos',
            descripcion=f'Se eliminó el hallazgo HLZ-{obj.id:03d}'
        )
        return super().delete(request, *args, **kwargs)
