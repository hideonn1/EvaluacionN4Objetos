## controlador de paquete_turistico_view.py

class Paquete_Controller:
    def __init__(self, paquete_service):
        # Recibe el Servicio por inyección. No sabe nada de repositorios o DB.
        self._service = paquete_service

    def mostrar_destinos(self):

        paquete_objeto = self._service.buscar_paquete(1)
        lista_destinos = paquete_objeto.destinos

        for i in lista_destinos:
            print(i)

