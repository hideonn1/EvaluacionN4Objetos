## archivo encargado de logica y comunicar a reservas_controller con reservas_repository

from src.Datos.reserva_repository import Reserva_Repository
from src.Logica_de_Negocio.models.Reserva import Reserva

class Reservas_Service:
    def __init__(self, reserva_repository: Reserva_Repository):
        self._repo = reserva_repository

    def crear_reserva(self, datos_reserva, id_usuario):
        #Validaciones de negocio

        if datos_reserva["fecha_inicio"] >= datos_reserva["fecha_final"]:
            raise ValueError("La fecha de inicio debe ser anterior a la fecha final.")
        
        if datos_reserva["monto_total"] <= 0:
            raise ValueError("El monto total debe ser mayor a 0.")
        
        nueva_reserva = Reserva(
            fecha_inicio = datos_reserva["fecha_inicio"],
            fecha_final = datos_reserva["fecha_final"],
            estado = "pendiente",
            monto_total = datos_reserva["monto_total"]
        )

        return self._repo.create(nueva_reserva, id_usuario)
    
    def obtener_reserva_por_id(self, id_reserva):
        reserva = self._repo.read_by_id(id_reserva)

        if not reserva:
            raise ValueError("Reserva no encontrada")
        return reserva
    
    def actualizar_reserva(self, reserva_objeto):
        if reserva_objeto.estado not in ["pendiente", "confirmada", "cancelada"]:
            raise ValueError("Estado inválido para la reserva.")
        
        if reserva_objeto <= 0:
            raise ValueError("El monto total debe ser mayor a 0.")
        
        if reserva_objeto.fecha_inicio >= reserva_objeto.fecha_final:
            raise ValueError("La fecha de inicio debe ser anterior a la fecha final.")
        
        return self._repo.update(reserva_objeto)

    
    def eliminar_reserva(self, id_reserva):
        return self._repo.delete(id_reserva)
    
    def obtener_reservas_por_usuario(self, id_usuario):
        return self._repo.read_by_usuario(id_usuario)