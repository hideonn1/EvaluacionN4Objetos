## vista encargada de mostrar los datos de la reserva del cliente
from datetime import datetime

def mostrar_reserva(reserva):
    if not reserva:
        print("\nNo se encontró la reserva.")
        return
    print("\n--- RESERVA ---")
    print(f"ID: {reserva.id_reserva}")
    print(f"Usuario: {reserva.id_usuario}")
    print(f"Fecha inicio: {reserva.fecha_inicio}")
    print(f"Fecha final: {reserva.fecha_final}")
    print(f"Estado: {reserva.estado}")
    print(f"Monto total: {reserva.monto_total}")


def sub_menu_reserva_cliente():
    print("---Menú gestión reservas---\n")
    print("---ELIJA UNA OPCIÓN ---\n")
    print("1. CREAR RESERVA.")
    print("2. BUSCAR RESERVA.")
    print("3. ELIMINAR RESERVA.\n")
    print("4. VOLVER A MENÚ ANTERIOR.\n")

def sub_menu_reserva_admin():
    print("---Menú gestión reservas---\n")
    print("---ELIJA UNA OPCIÓN ---\n")
    print("1. BUSCAR RESERVA.")
    print("2. ELIMINAR RESERVA.\n")
    print("3. VOLVER A MENÚ ANTERIOR.\n")