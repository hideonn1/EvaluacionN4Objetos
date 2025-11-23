## archivo encargado de logica y comunicar a destinos_controller con destinos_repository


class Destino_Service:
    
    def __init__(self, usuario_repository):
        # Recibe el Repositorio por inyección. No sabe nada de conexiones.
        self._repo = usuario_repository 

    def obtener_destino_por_nombre(self, nombre_destino):
        destino_objeto = self._repo.read_by_name(nombre_destino)
        if destino_objeto is None:
            raise ValueError(f"El destino con nombre {nombre_destino} no existe.")
        return destino_objeto
    def obtener_destino_por_id(self, id_destino):
        destino_objeto = self._repo.read_by_(id_destino)
        if destino_objeto is None:
            raise ValueError(f"El destino con nombre {id_destino} no existe.")
        return destino_objeto
    def nuevo_destino(self,registro):
        pass
    def eliminar_destino_por_id(self,id_destino):
        pass
    def eliminar_destino_por_nombre(self, nombre_destino):
        pass
    def modificar_destino(self, destino):
        pass