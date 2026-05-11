# Fase 2: Backend y Lógica de Negocio — AuditFlow

Conectar la capa de datos real (ORM Django) con la interfaz Glassmorphism ya construida en la Fase 1. Al finalizar, el sistema tendrá usuarios con roles, formularios CRUD funcionales para todas las entidades, y la bitácora registrando cada operación crítica. El dummy data será sustituido completamente por registros reales de SQLite.

---

## Módulos a implementar (en orden de dependencia)

### 1. `usuarios` — Modelo de Usuario con Roles

#### [MODIFY] [models.py](file:///c:/Users/AVRB9/Downloads/django/auditoria/sistema_auditoria/usuarios/models.py)
Extender `AbstractUser` con campo `rol` usando `choices`:

```python
class Usuario(AbstractUser):
    ROL_CHOICES = [
        ('administrador', 'Administrador'),
        ('auditor_lider', 'Auditor Líder'),
        ('auditor', 'Auditor'),
        ('auditado', 'Auditado'),
    ]
    rol = models.CharField(max_length=20, choices=ROL_CHOICES, default='auditado')
```

#### [NEW] `usuarios/urls.py` + vistas de login/logout
- Login con template propio (fuera del sidebar, página completa)
- `LoginView`, `LogoutView` de Django adaptadas
- Redirección al dashboard tras login

#### [MODIFY] `templates/base.html`
- Mostrar `{{ request.user.get_full_name }}` y `{{ request.user.rol }}` en topbar
- Avatar dinámico con iniciales del usuario
- Enlace de logout

---

### 2. `auditorias` — Modelo y CRUD Completo

#### [MODIFY] [models.py](file:///c:/Users/AVRB9/Downloads/django/auditoria/sistema_auditoria/auditorias/models.py)
```python
class Auditoria(models.Model):
    ESTADO_CHOICES = [('Planeada','Planeada'),('En Progreso','En Progreso'),('Finalizada','Finalizada')]
    CRITICIDAD_CHOICES = [('Alta','Alta'),('Media','Media'),('Baja','Baja'),('N/A','N/A')]
    titulo = models.CharField(max_length=200)
    auditor_lider = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Planeada')
    criticidad = models.CharField(max_length=10, choices=CRITICIDAD_CHOICES, default='N/A')
    alcance = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
```

#### [MODIFY] `auditorias/views.py`
- `AuditoriasListView` → consulta `Auditoria.objects.all()`
- `AuditoriaCreateView` → `ModelForm` + redirección + bitácora
- `AuditoriaDetailView` → detalle con hallazgos relacionados
- `AuditoriaUpdateView` → edición con validación de estado

---

### 3. `hallazgos` — Modelo y CRUD

#### [MODIFY] `hallazgos/models.py`
```python
class Hallazgo(models.Model):
    CRITICIDAD = [('Alta','Alta'),('Media','Media'),('Baja','Baja')]
    ESTADO = [('Abierto','Abierto'),('En Revisión (Evidencia)','En Revisión'), ('Cerrado','Cerrado')]
    auditoria = models.ForeignKey(Auditoria, on_delete=models.CASCADE, related_name='hallazgos')
    descripcion = models.TextField()
    area = models.CharField(max_length=150)
    criticidad = models.CharField(max_length=10, choices=CRITICIDAD)
    estado = models.CharField(max_length=30, choices=ESTADO, default='Abierto')
    fecha_reporte = models.DateField(auto_now_add=True)
    reportado_por = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
```

---

### 4. `acciones_correctivas` — Modelo y CRUD

#### [MODIFY] `acciones_correctivas/models.py`
```python
class AccionCorrectiva(models.Model):
    ESTADO = [('En Proceso','En Proceso'),('Implementada','Implementada'),('Retrasada','Retrasada'),('Rechazada','Rechazada')]
    hallazgo = models.ForeignKey(Hallazgo, on_delete=models.CASCADE, related_name='acciones')
    responsable = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    descripcion = models.TextField()
    fecha_compromiso = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADO, default='En Proceso')
```

---

### 5. `evidencias` — Modelo y Subida de Archivos

#### [MODIFY] `evidencias/models.py`
```python
class Evidencia(models.Model):
    TIPO = [('Imagen','Imagen'),('Documento','Documento'),('Video','Video')]
    ESTADO = [('Pendiente','Pendiente'),('Aprobada','Aprobada'),('Rechazada','Rechazada')]
    hallazgo = models.ForeignKey(Hallazgo, on_delete=models.CASCADE, null=True, blank=True)
    accion_correctiva = models.ForeignKey(AccionCorrectiva, on_delete=models.CASCADE, null=True, blank=True)
    archivo = models.FileField(upload_to='evidencias/')
    nombre_archivo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=15, choices=TIPO)
    fecha_subida = models.DateTimeField(auto_now_add=True)
    subido_por = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    estado = models.CharField(max_length=15, choices=ESTADO, default='Pendiente')
```

---

### 6. `bitacora` — Registro Inmutable de Eventos

#### [NEW] `bitacora/models.py`
```python
class EntradaBitacora(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    accion = models.CharField(max_length=100)   # ej: "Creó Auditoría"
    objeto_tipo = models.CharField(max_length=50)  # ej: "Auditoria"
    objeto_id = models.PositiveIntegerField()
    descripcion = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
```

Se llamará `registrar_evento(request, accion, objeto)` desde cada vista CRUD.

---

### 7. Formularios (`forms.py`) en cada App

Cada app tendrá su `forms.py` usando `ModelForm` con widgets personalizados para la estética oscura del sistema:
- `AuditoriaForm`
- `HallazgoForm`
- `AccionCorrectivaForm`
- `EvidenciaForm`

Cada form incluirá clases CSS (`glass-input`) para integrarse con el diseño.

---

### 8. Templates de Creación/Edición

Se crearán templates para formularios en cada módulo:
- `auditorias/form.html`
- `hallazgos/form.html`
- `acciones_correctivas/form.html`
- `evidencias/form.html`

---

### 9. Datos Iniciales (seed)

Se creará un script de `management/commands/seed_data.py` en la app `usuarios` para cargar:
- 1 superusuario Administrador
- 2 Auditores Líderes
- 2 Auditores
- 1 Auditado
- Datos de prueba para todas las entidades

---

## Orden de Ejecución

```
1. usuarios/models.py  →  makemigrations usuarios
2. auditorias/models.py  →  makemigrations auditorias
3. hallazgos/models.py  →  makemigrations hallazgos
4. acciones_correctivas/models.py  →  makemigrations acciones_correctivas
5. evidencias/models.py  →  makemigrations evidencias
6. bitacora/models.py  →  makemigrations bitacora
7. migrate (aplica todo)
8. Crear forms.py en cada app
9. Actualizar views.py en cada app
10. Crear templates de formularios
11. Correr seed_data
12. Actualizar base.html con usuario real
```

---

## Verificación

### Automática
```powershell
python manage.py check          # Sin errores de configuración
python manage.py migrate        # Todas las migraciones aplicadas
python manage.py seed_data      # Datos cargados correctamente
python manage.py runserver      # Servidor arranca en http://127.0.0.1:8000
```

### Manual (Browser)
- Login con usuario semilla → redirección al dashboard
- Crear una auditoría → aparece en lista
- Agregar hallazgo a la auditoría → aparece en lista con semaforización
- Proponer acción correctiva → aparece vinculada al hallazgo
- Subir evidencia → aparece en repositorio
- Verificar bitácora → muestra todos los eventos registrados
