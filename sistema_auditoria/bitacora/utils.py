from .models import EventoBitacora

def registrar_evento(usuario, accion, modulo, descripcion):
    """
    Registra un evento en la bitácora del sistema.
    """
    EventoBitacora.objects.create(
        usuario=usuario,
        accion=accion,
        modulo=modulo,
        descripcion=descripcion
    )
