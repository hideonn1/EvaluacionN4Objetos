## controlador de reservas
from vista.reservas_view import (
    crear_reserva_vista,
    mostrar_reserva,
    menu_reservas
) 

class ReservasController:
    def __init__(self, reserva_service):
        # Recibe el Servicio por inyección. No sabe nada de repositorios o DB.
        self._service = reserva_service

    def crear_reserva(self, id_usuario):
        try:
            #1. Pedir datos a la vista
            datos_reserva = crear_reserva_vista()

            #2. Pasar los datos al service
            nueva_reserva = self._service.crear_reserva(datos_reserva, id_usuario)

            #3. Mostrar resultado
            print("\nReserva creada con exito:")
            mostrar_reserva(nueva_reserva)
        except ValueError as Error:
            print(f"\nError al crear reserva: {Error}")
        except Exception as Error:
            print(f"\nError inesperado {Error}")
    
    def obtener_reserva_por_id(self):
        try:
            id_reserva = int(input("Ingrese el ID de la reserva: "))
            reserva = self._service.obtener_reserva_por_id(id_reserva)
            mostrar_reserva(reserva)
        except ValueError as Error:
            print(f"\n{Error}")

    def actualizar_reserva(self):
        try:
            id_reserva = int(input("Ingrese el ID de la reserva a actualizar: "))
            reserva = self._service.obtener_reserva_por_id(id_reserva)
            # Se piden datos nuevos desde la view
            
            nuevo_estado = input("Ingrese nuevo estado (pendiente/confirmada/cancelada): ")
            reserva.estado = nuevo_estado
            reserva.monto_actual = int(input("Ingrese nuevo monto total: "))

            reserva_actualizada = self._service.actualizar_reserva(reserva)
            print("\nReserva actualizada:")
            mostrar_reserva(reserva_actualizada)
        except ValueError as Error:
            print(f"\n{Error}")
