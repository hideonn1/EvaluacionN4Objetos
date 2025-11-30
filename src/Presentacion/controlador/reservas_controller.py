## controlador de reservas
from datetime import datetime
from ..vista.reservas_view import (
    mostrar_reserva,
    sub_menu_reserva_cliente,
    sub_menu_reserva_admin
) 

class Reservas_Controller:
    def __init__(self, reserva_service):
        # Recibe el Servicio por inyección. No sabe nada de repositorios o DB.
        self._service = reserva_service

    def crear_reserva(self, id_usuario):
        while True:
                #1. Pedir datos
                while True:
                    try:
                        inicio = input("Ingrese fecha de inicio (YYYY-MM-DD): ").strip()
                        fecha_inicio = datetime.strptime(inicio, "%Y-%m-%d").date()
                        break
                    except ValueError:
                        print("Formato inválido. Use YYYY-MM-DD.")
                        continue

                while True:
                    try:
                        final = input("Ingrese fecha final (YYYY-MM-DD): ").strip()
                        fecha_final = datetime.strptime(final, "%Y-%m-%d").date()
                        if fecha_final < fecha_inicio:
                            print("La fecha final no puede ser menor que la inicial.")
                            continue
                        break
                    except ValueError:
                        print("Formato inválido. Use YYYY-MM-DD.")
                        continue

                while True:
                    try:
                        monto_total = int(input("Ingrese monto total: "))
                        if monto_total <= 0:
                            print("El monto debe ser mayor a 0.")
                            continue
                        break
                    except ValueError:
                        print("Debe ingresar un número válido.")
                try:
                    #2. Pasar los datos al service
                    datos_reserva = {
                        "fecha_inicio": fecha_inicio,
                        "fecha_final": fecha_final,
                        "monto_total": monto_total
                    }
                    nueva_reserva = self._service.crear_reserva(datos_reserva, id_usuario)
            
                    #3. Mostrar resultado
                    print("\nReserva creada con exito:")
                    mostrar_reserva(nueva_reserva)
                    break
                except ValueError as Error:
                    print(f"\nError al crear reserva: {Error}")
                except Exception as Error:
                    print(f"\nError inesperado {Error}")
    
    def obtener_reserva_por_id(self):
        # Verificacion extra 
        todas = self._service.obtener_todas_reservas()
        if not todas:
            print("\nNo hay reservas disponibles.")
            return "volver"

        while True:
            try:
                id_reserva = int(input("Ingrese el ID de la reserva: "))
                reserva = self._service.obtener_reserva_por_id(id_reserva)

                if reserva:
                    mostrar_reserva(reserva)
                    return "ok"

                else:
                    print("\nNo se encontró ninguna reserva con ese ID.")
            except ValueError:
                print(f"\nDebe ingresar un número válido. Intente nuevamente")
            except Exception as Error:
                print(f"\nError inesperado: {Error}")
                return "error"

    def actualizar_reserva(self):
        while True:
            try:
                id_reserva = int(input("Ingrese el ID de la reserva a actualizar: "))
                reserva = self._service.obtener_reserva_por_id(id_reserva)
                # Se piden datos nuevos desde la view
                if not reserva:
                    print("\nNo se encontró ninguna reserva con ese ID.")
                    continue

                nuevo_estado = input("Ingrese nuevo estado (pendiente/confirmada/cancelada): ").strip().lower()
                if nuevo_estado not in ["pendiente", "confirmada", "cancelada"]:
                    print("Estado inválido. Debe ser pendiente, confirmada o cancelada.")
                    continue
                reserva.estado = nuevo_estado
            
                reserva.monto_total = int(input("Ingrese nuevo monto total: "))

                reserva_actualizada = self._service.actualizar_reserva(reserva)
                print("\nReserva actualizada:")
                mostrar_reserva(reserva_actualizada)
                break
            except ValueError as Error:
                print(f"\nError al actualizar reserva: {Error}")
                # Se captura tanto el estado invalido, como reserva no encontrada.
            except Exception as Error:
                print(f"\nError inesperado: {Error}")


    def reserva_controlador_admin(self, usuario):
        while True:
            sub_menu_reserva_admin()
            try:
                opcion_user = int(input("Ingrese una de las opciones disponibles (1-4): "))
            except ValueError:
                print("Debe ingresar un carácter numérico para continuar.")
                continue

            if opcion_user not in (1,2,3,4):
                print("Debe ingresar una de las opciones disponibles para continuar.")
                continue
            return opcion_user    
                
    def funciones_reserva_cliente(self):
            while True:
                sub_menu_reserva_cliente()
                try:
                    opcion_user = int(input("Ingrese una de las opciones disponibles (1-5): "))
                except ValueError:
                    print("Debe ingresar un carácter numérico para continuar.")
                    continue

                if opcion_user not in (1,2,3,4,5):
                    print("Debe ingresar una de las opciones disponibles para continuar.")
                    continue
                return opcion_user 

    def eliminar_reserva(self):
        while True:
            try:
                id_reserva = int(input("Ingrese el ID de la reserva a eliminar: "))
                reserva = self._service.obtener_reserva_por_id(id_reserva)

                if not reserva:
                    print("\nNo se encontró ninguna reserva con ese ID.")
                    continue

                mostrar_reserva(reserva)
                
                while True:
                    confirmacion = input("¿Está seguro que desea eliminar esta reserva? (si/no): ").strip().lower()
                    if confirmacion == 'si':
                        if self._service.eliminar_reserva(id_reserva):
                            print("Reserva eliminada exitosamente.")
                            break
                    elif confirmacion == 'no':
                        print("Operación cancelada.")
                        break
                    else:
                        print("Debe ingresar 'si' o 'no'.")
                        continue
            except ValueError as Error:
                print(f"\nError: {Error}")
            except Exception as Error:
                print(f"\nError inesperado: {Error}")
