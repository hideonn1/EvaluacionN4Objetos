# Clase de Reserva
# from .PaqueteTuristico import PaqueteTuristico # Removed as it seems unused in this context

class Reserva():
    def __init__ (self, 
                id_usuario,
                fecha_inicio,
                fecha_final,
                estado,
                monto_total,
                id_reserva = None):
        
        self.id_reserva = id_reserva
        self.id_usuario = id_usuario
        self.fecha_inicio = fecha_inicio
        self.fecha_final = fecha_final
        self.estado = estado
        self.monto_total = monto_total
    
    def __str__(self):
        info_reserva = (
            f"Reserva ID: {self.id_reserva}\n"
            f"Usuario ID: {self.id_usuario}\n"
            f"Fecha inicio: {self.fecha_inicio}\n"
            f"Fecha final: {self.fecha_final}\n"
            f"Estado: {self.estado}\n"
            f"Monto total: ${self.monto_total}")
        
        return info_reserva