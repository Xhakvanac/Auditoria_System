from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import AccionCorrectiva
from .forms import AccionCorrectivaForm
from bitacora.utils import registrar_evento

class AccionesListView(LoginRequiredMixin, ListView):
    model = AccionCorrectiva
    template_name = 'acciones_correctivas/lista.html'
    context_object_name = 'lista_acciones'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_acciones'] = AccionCorrectiva.objects.count()
        context['pendientes'] = AccionCorrectiva.objects.filter(estado='Pendiente').count()
        return context

class AccionCreateView(LoginRequiredMixin, CreateView):
    model = AccionCorrectiva
    form_class = AccionCorrectivaForm
    template_name = 'acciones_correctivas/form.html'
    success_url = reverse_lazy('lista_acciones')

    def form_valid(self, form):
        response = super().form_valid(form)
        registrar_evento(
            usuario=self.request.user,
            accion='Propuesta',
            modulo='Acciones Correctivas',
            descripcion=f'Se propuso una acción para el hallazgo HLZ-{self.object.hallazgo.id:03d}'
        )
        return response

class AccionUpdateView(LoginRequiredMixin, UpdateView):
    model = AccionCorrectiva
    form_class = AccionCorrectivaForm
    template_name = 'acciones_correctivas/form.html'
    success_url = reverse_lazy('lista_acciones')

    def form_valid(self, form):
        response = super().form_valid(form)
        registrar_evento(
            usuario=self.request.user,
            accion='Actualización',
            modulo='Acciones Correctivas',
            descripcion=f'Se actualizó la acción ACC-{self.object.id:03d}'
        )
        return response

class AccionDeleteView(LoginRequiredMixin, DeleteView):
    model = AccionCorrectiva
    template_name = 'acciones_correctivas/confirm_delete.html'
    success_url = reverse_lazy('lista_acciones')

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        registrar_evento(
            usuario=self.request.user,
            accion='Eliminación',
            modulo='Acciones Correctivas',
            descripcion=f'Se eliminó la acción ACC-{obj.id:03d}'
        )
        return super().delete(request, *args, **kwargs)
