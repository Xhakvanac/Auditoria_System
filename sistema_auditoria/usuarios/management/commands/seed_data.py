"""
Comando de gestión para poblar la base de datos con usuarios de prueba.
Uso: python manage.py seed_data
"""
import os
import django
from django.core.management.base import BaseCommand
from usuarios.models import Usuario
class Command(BaseCommand):
    help = 'Carga usuarios de prueba para el sistema AuditFlow'
    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.MIGRATE_HEADING('\n--- Iniciando seed de datos - AuditFlow ---\n'))
        usuarios_seed = [
            {
                'username': 'admin',
                'password': 'Admin123!',
                'first_name': 'Carlos',
                'last_name': 'Administrador',
                'email': 'admin@auditflow.com',
                'rol': 'administrador',
                'is_staff': True,
                'is_superuser': True,
            },
            {
                'username': 'lider1',
                'password': 'Lider123!',
                'first_name': 'Ana Sofía',
                'last_name': 'Ruiz',
                'email': 'aruiz@auditflow.com',
                'rol': 'auditor_lider',
                'is_staff': False,
                'is_superuser': False,
            },
            {
                'username': 'lider2',
                'password': 'Lider123!',
                'first_name': 'Roberto',
                'last_name': 'Sánchez',
                'email': 'rsanchez@auditflow.com',
                'rol': 'auditor_lider',
                'is_staff': False,
                'is_superuser': False,
            },
            {
                'username': 'auditor1',
                'password': 'Audit123!',
                'first_name': 'Mónica',
                'last_name': 'Gómez',
                'email': 'mgomez@auditflow.com',
                'rol': 'auditor',
                'is_staff': False,
                'is_superuser': False,
            },
            {
                'username': 'auditor2',
                'password': 'Audit123!',
                'first_name': 'Carlos',
                'last_name': 'Treviño',
                'email': 'ctrevino@auditflow.com',
                'rol': 'auditor',
                'is_staff': False,
                'is_superuser': False,
            },
            {
                'username': 'auditado1',
                'password': 'Auditado123!',
                'first_name': 'Marcos',
                'last_name': 'Torres',
                'email': 'mtorres@auditflow.com',
                'rol': 'auditado',
                'is_staff': False,
                'is_superuser': False,
            },
        ]
        creados = 0
        omitidos = 0
        for datos in usuarios_seed:
            username = datos.pop('username')
            password = datos.pop('password')
            if Usuario.objects.filter(username=username).exists():
                self.stdout.write(f'  [WARN] Usuario "{username}" ya existe - omitido.')
                omitidos += 1
                datos['username'] = username  # restaurar por si se reutiliza
                continue
            user = Usuario.objects.create_user(
                username=username,
                password=password,
                **datos
            )
            creados += 1
            self.stdout.write(
                self.style.SUCCESS(
                    f'  [OK] Creado: {user.get_full_name()} '
                    f'({user.username}) - Rol: {user.get_rol_display()}'
                )
            )
        self.stdout.write('\n' + '-' * 50)
        self.stdout.write(
            self.style.SUCCESS(f'Seed completado: {creados} creados, {omitidos} omitidos.\n')
        )
        self.stdout.write(self.style.WARNING(
            'Credenciales de acceso:\n'
            '  admin      / Admin123!       (Administrador)\n'
            '  lider1     / Lider123!       (Auditor Líder)\n'
            '  lider2     / Lider123!       (Auditor Líder)\n'
            '  auditor1   / Audit123!       (Auditor)\n'
            '  auditor2   / Audit123!       (Auditor)\n'
            '  auditado1  / Auditado123!    (Auditado)\n'
        ))