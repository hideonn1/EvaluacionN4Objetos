# Clase de Reserva
from PaqueteTuristico import PaqueteTuristico

class Reserva():
    def __init__ (self, id_reserva,
                id_cliente,
                paquete_turistico,
                fecha_reserva,
                estado,
                monto_pagado):
        
        self.id_reserva = id_reserva
        self.id_cliente = id_cliente
        self.paquete_turistico = PaqueteTuristico(**paquete_turistico)
        self.fecha_reserva = fecha_reserva
        self.estado = estado
        self.monto_pagado = monto_pagado
    
    def __str__(self):
        info_reserva = (
            f"Reserva ID: {self.id_reserva}\n"
            f"Cliente ID: {self.id_cliente}\n"
            f"Fecha de reserva: {self.fecha_reserva}\n"
            f"Estado: {self.estado}\n"
            f"Monto pagado: ${self.monto_pagado}")
        info_paquete = str(self.paquete_turistico)

        return info_reserva + info_paquete