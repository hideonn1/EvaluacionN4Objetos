# Clase del Paquete Turístico.
from Destino import Destino

class PaqueteTuristico():
    def __init__ (self, id_paquete,
                  fecha_llegada,
                  fecha_salida,
                  orden_visita,
                  costo_destino,
                  destinos):
        
        self.id_paquete = id_paquete
        self.fecha_llegada = fecha_llegada
        self.fecha_salida = fecha_salida
        self.orden_visita = orden_visita
        self.costo_destino = costo_destino
        self.destinos = [Destino(**d) for d in destinos]
    
    def __str__ (self):
        destinos_str = '\n    - ' + '\n    - '.join([destino.nombre for destino in self.destinos])
        return (
            f"Paquete Turístico: {self.nombre} (ID: {self.id_paquete})\n"
            f"Fechas: {self.fecha_inicio} → {self.fecha_fin}\n"
            f"Destinos incluidos:{destinos_str}\n"
            f"Descripción: {self.descripcion}\n"
            f"Precio total: ${self.precio_total}\n"
            f"Cupos disponibles: {self.cupos_disp}"
        )

    
    def calcular_precio_total():
        pass

    def ver_disponibilidad():
        pass

    def agregar_destino():
        pass