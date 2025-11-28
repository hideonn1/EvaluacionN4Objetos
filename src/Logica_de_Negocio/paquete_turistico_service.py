## archivo encargado de logica y comunicar a paquete_turistico_controller con paquete_turistico_repository
from datetime import timedelta, date

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
        return paquete
    def agregar_destino_a_paquete(self, paquete, destino):
        self._repo.destino_x_paquete(paquete,destino)

    def confirmar_fecha_salida(self, fecha, fecha_salida = None):
        hoy = date.today()
            
        fecha_limite = hoy + timedelta(days=7)
        if fecha_salida != None and fecha < fecha_salida:
            return "Error! No puede ingresar una fecha anterior a la fecha de inicio del paquete."
        if fecha < fecha_limite:
            return "Error! Solo se pueden ingresar fechas con 7 dias de antelacion."
        else:
            return True

    def confirmar_fecha_llegada(self, fecha_llegada, fecha_salida ):
        if fecha_salida < fecha_llegada:
            print("hola")
            return True
        else:
            return "Error! La fecha de llegada no puede ser anterior a la fecha de Salida. "
        
    def duplicidad_verf(self, destino_id,paquete_id):
        return self._repo.duplicidad_destino(destino_id,paquete_id)
    
    def quitar_paquete(self, id_paquete):
        return self._repo.eliminar_paquete(paquete_id)

    def quitar_destino(self,id_paquete, orden_visita):
        destino = self._repo.obtener_destino(id_paquete, orden_visita)
        fecha_inicio = destino['fecha_salida']
        fecha_fin = destino['fecha_llegada']
        diferencia = fecha_fin - fecha_inicio
        diferencia_dias = diferencia.days

        self._repo.eliminar_destino(id_paquete, orden_visita, diferencia_dias)