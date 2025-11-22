# Clase de Destino

class Destino():
    def __init__ (self, id_destino,
                nombre,
                ciudad,
                pais,
                descripcion,
                actividades_disponibles,
                costo):

        self.id_destino = id_destino
        self.nombre = nombre
        self.ciudad = ciudad
        self.pais = pais
        self.descripcion = descripcion
        self.actividades_disponibles = actividades_disponibles
        self.costo = costo

    def __str__(self):
        # La variable destinos_str se utiliza para mayor reutilización, legibilidad y depuración
        # para favorecer la escabilidad.

        actividades_str = '\n    - ' + '\n    - '.join(self.actividades_disp)
        return (
        f"Destino: {self.nombre} (ID: {self.id_destino})\n"
        f"Descripción: {self.descripcion}\n"
        f"Actividades disponibles:{actividades_str}\n"
        f"Costo total: ${self.costo}"
        )
    
