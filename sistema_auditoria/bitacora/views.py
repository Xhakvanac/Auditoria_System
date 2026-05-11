from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import EventoBitacora

class BitacoraListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = EventoBitacora
    template_name = 'bitacora/lista.html'
    context_object_name = 'eventos'
    paginate_by = 20

    def test_func(self):
        # Solo administradores pueden ver la bitácora completa
        return self.request.user.rol == 'administrador' or self.request.user.is_superuser
