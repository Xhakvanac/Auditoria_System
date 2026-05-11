# 🛡️ AuditFlow — Sistema de Gestión de Auditorías

AuditFlow es una plataforma web premium diseñada para centralizar, gestionar y dar seguimiento a procesos de auditoría interna. Con una interfaz moderna basada en **Glassmorphism**, permite a los auditores reportar hallazgos, proponer acciones correctivas y gestionar evidencias de manera eficiente y segura.

## 🚀 Características Principales

- **Dashboard Inteligente**: Visualización de métricas críticas y progreso en tiempo real con gráficas dinámicas.
- **Gestión de Usuarios**: Sistema de autenticación con roles (Administrador, Auditor Lider, Auditor, Auditado).
- **Módulo de Auditorías**: Ciclo de vida completo desde la planificación hasta el cierre.
- **Control de Hallazgos**: Clasificación por criticidad y seguimiento de estados.
- **Planes de Acción**: Asignación de responsabilidades y fechas compromiso para la mejora continua.
- **Repositorio de Evidencias**: Carga y gestión de archivos probatorios (PDF, Imágenes, etc.).
- **Trazabilidad Total**: Bitácora de sistema que registra cada evento para auditorías de cumplimiento.

## 🛠️ Stack Tecnológico

- **Backend**: Python 3.x / Django 6.x
- **Base de Datos**: SQLite (desarrollo) / Compatible con PostgreSQL (producción)
- **Frontend**: HTML5, Vanilla CSS (Design System propio), JavaScript
- **Gráficas**: Chart.js
- **Iconografía**: Boxicons

## 📦 Instalación y Configuración

1. **Clonar el repositorio**:
   ```bash
   git clone <url-del-repositorio>
   cd sistema_auditoria
   ```

2. **Crear y activar entorno virtual**:
   ```bash
   python -m venv venv
   # Windows:
   .\venv\Scripts\activate
   # Linux/Mac:
   source venv/bin/activate
   ```

3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Aplicar migraciones**:
   ```bash
   python manage.py migrate
   ```

5. **Poblar datos iniciales (Opcional)**:
   ```bash
   python manage.py seed_data
   ```

6. **Iniciar servidor**:
   ```bash
   python manage.py run dev
   ```

## 👥 Roles de Usuario Predeterminados

| Usuario | Contraseña | Rol |
| :--- | :--- | :--- |
| `admin` | `Admin123!` | Administrador |
| `auditor_lider` | `Lider123!` | Auditor Líder |
| `auditor1` | `Audit123!` | Auditor |
| `auditado1` | `Auditado123!` | Responsable / Auditado |

## 📂 Estructura del Proyecto

```text
├── sistema_auditoria/      # Configuración central del proyecto
├── usuarios/               # Gestión de perfiles y auth
├── auditorias/             # Módulo principal de auditorías
├── hallazgos/              # Gestión de no conformidades
├── acciones_correctivas/   # Seguimiento de mejoras
├── evidencias/             # Repositorio de archivos
├── bitacora/               # Registro de eventos (Audit Log)
├── templates/              # Interfaz de usuario (Base + Dashboard)
└── media/                  # Almacenamiento de archivos subidos
```

---
*Desarrollado con enfoque en Excelencia Visual y Trazabilidad.*
