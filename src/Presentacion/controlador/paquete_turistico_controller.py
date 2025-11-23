## controlador de paquete_turistico_view.py

from ..vista.destinos_view import mostrar_destinos

class Paquete_Controller:
    def __init__(self, paquete_service, destino_service):
        # Recibe el Servicio por inyección. No sabe nada de repositorios o DB.
        self._service = paquete_service
        self._service_destino = destino_service

    def mostrar_destinos(self,id_paquete):

        paquete_objeto = self._service.buscar_paquete(id_paquete)
        lista_destinos = paquete_objeto.destinos

        return lista_destinos

    def mostrar_paquete(self, id_paquete):
        paquete_objeto = self._service.buscar_paquete(id_paquete)
        print(paquete_objeto)

    def agregar_destino(self,paquete):
        lista_destinos = self._service_destino.mostrar_destinos()
        mostrar_destinos(lista_destinos)
        while True:
            try:
                destino_id = int(input("Ingrese el ID del destino que quiere agregar al paquete."))
                break
            except Exception as e:
                print(e)
        self._service.agregar_destino_a_paquete(paquete.id_paquete, destino_id)


