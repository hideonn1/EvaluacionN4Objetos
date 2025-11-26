# Clase del Paquete Turístico.
from .Destino import Destino

class PaqueteTuristico():
    def __init__ (self,
                  fecha_llegada,
                  fecha_salida,
                  orden_visita,
                  costo_destino,
                  id_paquete = None,
                  destinos = None):
        
        self.id_paquete = id_paquete
        self.fecha_llegada = fecha_llegada
        self.fecha_salida = fecha_salida
        self.orden_visita = orden_visita
        self.costo_destino = costo_destino
        if destinos:
            self.destinos = [Destino(**d) for d in destinos] 
        else:
            self.destinos = []
    
    def __str__ (self):
        return (
            f"(ID: {self.id_paquete})\n"
            f"Fechas: {self.fecha_llegada} → {self.fecha_salida}\n"
            f"Destinos incluidos:{self.destinos}\n"

        )

    
    def calcular_precio_total():
        pass

    def ver_disponibilidad():
        pass

    def agregar_destino():
        pass