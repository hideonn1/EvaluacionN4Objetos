# Clase del Paquete Turístico.

class PaqueteTuristico():
    def __init__ (self, id_paquete,
                  nombre,
                  destinos,
                  fecha_inicio,
                  fecha_fin,
                  precio_total,
                  cupos_disp,
                  descripcion):
        
        self.id_paquete = id_paquete
        self.nombre = nombre
        self.destinos = destinos
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.precio_total = precio_total
        self.cupos_disp = cupos_disp
        self.descripcion = descripcion
    
    def __str__ (self):
        # La variable destinos_str se utiliza para mayor reutilización, legibilidad y depuración
        # para favorecer la escabilidad.

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