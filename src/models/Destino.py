# Clase de Destino

class Destino():
    def __init__ (self, id_destino,
                nombre,
                descripcion,
                actividades_disp,
                costo_total):

        self.id_destino = id_destino
        self.nombre = nombre
        self.descripcion = descripcion
        self.actividades_disp = actividades_disp
        self.costo_total = costo_total

    def __str__(self):
        # La variable destinos_str se utiliza para mayor reutilización, legibilidad y depuración
        # para favorecer la escabilidad.

        actividades_str = '\n    - ' + '\n    - '.join(self.actividades_disp)
        return (
        f"Destino: {self.nombre} (ID: {self.id_destino})\n"
        f"Descripción: {self.descripcion}\n"
        f"Actividades disponibles:{actividades_str}\n"
        f"Costo total: ${self.costo_total}"
        )
    
