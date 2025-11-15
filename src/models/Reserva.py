# Clase de Reserva

class Reserva():
    def __init__ (self, id_reserva,
                id_cliente,
                paquete,
                fecha_reserva,
                estado,
                monto_pagado):
        
        self.id_reserva = id_reserva
        self.id_cliente = id_cliente
        self.paquete = paquete
        self.fecha_reserva = fecha_reserva
        self.estado = estado
        self.monto_pagado = monto_pagado
    
    def __str__(self):
        return (
            f"Reserva ID: {self.id_reserva}\n"
            f"Cliente ID: {self.id_cliente}\n"
            f"Paquete: {self.paquete.nombre}\n"
            f"Fecha de reserva: {self.fecha_reserva}\n"
            f"Estado: {self.estado}\n"
            f"Monto pagado: ${self.monto_pagado}"
        )
        