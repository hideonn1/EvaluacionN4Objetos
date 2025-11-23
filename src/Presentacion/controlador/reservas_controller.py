## controlador de reservas
class Reservas_Controller:
    def __init__(self, reserva_service):
        # Recibe el Servicio por inyección. No sabe nada de repositorios o DB.
        self._service = reserva_service

    def crear_reserva(self):
        pass