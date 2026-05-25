from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import PerfilForm, PreferenciasForm
from .models import PreferenciasUsuario

@login_required
def perfil_view(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu perfil ha sido actualizado.')
            return redirect('panel_perfil')
    else:
        form = PerfilForm(instance=request.user)
    
    return render(request, 'configuracion/perfil.html', {
        'form': form,
        'perfil': request.user
    })

@login_required
def notificaciones_view(request):
    preferencias, created = PreferenciasUsuario.objects.get_or_create(usuario=request.user)
    
    if request.method == 'POST':
        form = PreferenciasForm(request.POST, instance=preferencias)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tus preferencias de notificaciones han sido actualizadas.')
            return redirect('panel_notificaciones')
    else:
        form = PreferenciasForm(instance=preferencias)
    
    return render(request, 'configuracion/notificaciones.html', {
        'form': form
    })

@login_required
def seguridad_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Importante para que no cierre sesión
            messages.success(request, 'Tu contraseña ha sido cambiada exitosamente.')
            return redirect('panel_seguridad')
        else:
            messages.error(request, 'Por favor corrige los errores abajo.')
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'configuracion/seguridad.html', {
        'form': form
    })

@login_required
def sistema_view(request):
    # Por ahora es un placeholder, solo admins deberían editar esto o simplemente mostrar preferencias de lectura.
    return render(request, 'configuracion/sistema.html')
