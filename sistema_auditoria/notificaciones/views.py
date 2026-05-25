from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Notificacion

@login_required
def lista_notificaciones(request):
    notificaciones = request.user.notificaciones.all()
    return render(request, 'notificaciones/lista.html', {
        'notificaciones': notificaciones
    })

@login_required
def marcar_leida(request, notificacion_id):
    notificacion = get_object_or_404(Notificacion, id=notificacion_id, usuario=request.user)
    notificacion.leida = True
    notificacion.save()
    
    if notificacion.enlace:
        return redirect(notificacion.enlace)
    return redirect('lista_notificaciones')

@login_required
def marcar_todas_leidas(request):
    request.user.notificaciones.filter(leida=False).update(leida=True)
    messages.success(request, 'Todas las notificaciones han sido marcadas como leídas.')
    return redirect('lista_notificaciones')
