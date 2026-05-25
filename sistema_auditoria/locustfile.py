from locust import HttpUser, task, between

class AuditFlowUser(HttpUser):
    """
    Simulación de un usuario interactuando con el backend de AuditFlow.
    """
    # Tiempo de espera entre tareas (entre 1 y 5 segundos)
    wait_time = between(1, 5)

    @task(3)
    def view_dashboard(self):
        """
        Simula la carga de datos del Dashboard.
        """
        self.client.get("/api/dashboard/")

    @task(2)
    def view_hallazgos(self):
        """
        Simula la consulta de la bitácora de Hallazgos.
        """
        self.client.get("/api/hallazgos/")

    def on_start(self):
        """
        Acciones al iniciar el usuario (si requiere login, se pondría aquí).
        Por ahora los endpoints son públicos para la prueba de estrés.
        """
        pass
