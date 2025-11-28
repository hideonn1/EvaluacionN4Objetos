# Clase de Destino

class Destino():
    def __init__ (self,
                nombre,
                ciudad,
                pais,
                descripcion,
                actividades_disponibles,
                costo,
                orden_visita = None,
                fecha_llegada = None,
                fecha_salida = None,
                id_destino = None):

        self.id_destino = id_destino
        self.nombre = nombre
        self.ciudad = ciudad
        self.pais = pais
        self.descripcion = descripcion
        self.actividades_disponibles = actividades_disponibles
        self.costo = costo
        self.orden_visita = orden_visita
        self.fecha_salida = fecha_llegada
        self.fecha_llegada = fecha_salida

    def __str__(self):
        # La variable destinos_str se utiliza para mayor reutilización, legibilidad y depuración
        # para favorecer la escabilidad.

        return (
        f"Destino: {self.nombre} (ID: {self.id_destino})\n"
        f"Descripción: {self.descripcion}\n"
        f"Actividades disponibles:{self.actividades_disponibles}\n"
        f"Costo total: ${self.costo}"
        )
    
