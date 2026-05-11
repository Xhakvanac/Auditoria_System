from django.views.generic import TemplateView

class ConfiguracionView(TemplateView):
    template_name = 'configuracion/panel.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['perfil'] = {
            'nombre': 'Administrador Principal',
            'email': 'admin@auditflow.com',
            'rol': 'SuperAdmin',
            'ultima_sesion': 'Hoy, 10:25 AM'
        }
        return context
