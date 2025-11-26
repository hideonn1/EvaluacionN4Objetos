## archivo encargado de logica y comunicar a paquete_turistico_controller con paquete_turistico_repository
class Paquete_Service:
    
    def __init__(self, paquete_repository, destino_repository):
        # Recibe el Repositorio por inyección. No sabe nada de conexiones.
        self._repo = paquete_repository
        self._repo_destino = destino_repository

    def buscar_paquete(self, paquete_id):
        # Buscar paquete en el repositorio
        paquete_objeto = self._repo.read_by_id(paquete_id)
        if not paquete_objeto:
            # Si no existe, se lanza un mensaje de error claro para el usuario
            raise ValueError("Paquete turístico no encontrado")
        
        # Se obtienen los destinos asociados desde el repositorio de destinos
        lista_destinos = self._repo_destino.get_all_destinos(paquete_id)
        # Se le asigna la lista de destinos al objeto paquete
        paquete_objeto.destinos = lista_destinos
        # Se retorna el paquete completo con sus destinos
        return paquete_objeto
    
    def agregar_paquete(self, paquete):
        self._repo.create(paquete)