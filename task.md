# Fase 2 — AuditFlow Task List

## Módulo 1: `usuarios`
- [/] Extender `models.py` con campo `rol` + choices
- [ ] Crear `usuarios/urls.py` con rutas login/logout
- [ ] Crear `usuarios/views.py` con LoginView/LogoutView
- [ ] Crear template `templates/usuarios/login.html`
- [ ] Actualizar `sistema_auditoria/urls.py` con rutas de auth
- [ ] Actualizar `settings.py` (LOGIN_URL, LOGIN_REDIRECT_URL, LOGOUT_REDIRECT_URL)
- [ ] Actualizar `templates/base.html` con usuario real + logout
- [ ] Crear `management/commands/seed_data.py`
- [ ] `makemigrations usuarios` + `migrate`
- [ ] Correr seed y verificar login

## Módulo 2: `auditorias`
- [ ] Escribir `auditorias/models.py`
- [ ] Crear `auditorias/forms.py`
- [ ] Actualizar `auditorias/views.py` con CRUD real
- [ ] Crear templates: `auditorias/form.html`, actualizar `lista.html`
- [ ] `makemigrations auditorias` + `migrate`

## Módulo 3: `hallazgos`
- [ ] Escribir `hallazgos/models.py`
- [ ] Crear `hallazgos/forms.py`
- [ ] Actualizar `hallazgos/views.py` con CRUD real
- [ ] Crear templates: `hallazgos/form.html`, actualizar `lista.html`
- [ ] `makemigrations hallazgos` + `migrate`

## Módulo 4: `acciones_correctivas`
- [ ] Escribir `acciones_correctivas/models.py`
- [ ] Crear `acciones_correctivas/forms.py`
- [ ] Actualizar `acciones_correctivas/views.py` con CRUD real
- [ ] Crear templates + `makemigrations` + `migrate`

## Módulo 5: `evidencias`
- [ ] Escribir `evidencias/models.py`
- [ ] Crear `evidencias/forms.py`
- [ ] Actualizar `evidencias/views.py` + subida de archivos
- [ ] Crear templates + `makemigrations` + `migrate`

## Módulo 6: `bitacora`
- [ ] Escribir `bitacora/models.py`
- [ ] Crear helper `bitacora/utils.py` con `registrar_evento()`
- [ ] Integrar bitácora en todas las vistas CRUD
- [ ] `makemigrations bitacora` + `migrate`

## Verificación Final
- [ ] `python manage.py check` sin errores
- [ ] Login → Dashboard funcional
- [ ] CRUD completo: crear auditoría → hallazgo → acción → evidencia
- [ ] Bitácora refleja todos los eventos
