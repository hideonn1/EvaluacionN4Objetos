## vista encargada de mostrar los datos de la reserva del cliente
from datetime import datetime

def crear_reserva_vista():
    print("\n--- CREAR RESERVA ---")

    while True:
        try:
            # Los inputs se dejan al ser vista de consola y no de interfaz web
            fecha_inicio = input("Ingrese fecha de inicio (YYYY-MM-DD): ").strip()
            fecha_final = input("Ingrese fecha final (YYYY-MM-DD): ").strip()

            datetime.strptime(fecha_inicio, "%Y-%m-%d")
            datetime.strptime(fecha_final, "%Y-%m-%d")
            break
        except ValueError:
            print("Formato inválido. Use YYYY-MM-DD.")

    while True:
        try:
            monto_total = int(input("Ingrese monto total: "))
            if monto_total <= 0:
                print("El monto debe ser mayor a 0.")
                continue
            break
        except ValueError:
            print("Debe ingresar un número válido.")

    return {
        "fecha_inicio": fecha_inicio,
        "fecha_final": fecha_final,
        "monto_total": monto_total
    }

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

def menu_reservas():
    return (
        "\n--- MENU RESERVAS ---\n"
        "1. CREAR RESERVA.\n"
        "2. BUSCAR RESERVA.\n"
        "3. ACTUALIZAR RESERVA.\n"
        "4. ELIMINAR RESERVA.\n"
        "5. VOLVER AL MENÚ PRINCIPAL.\n"
        "Seleccione una opción: "
    )

def sub_menu_reserva_cliente():
    print("---Menú gestión reservas---\n")
    print("---ELIJA UNA OPCIÓN ---\n")
    print("1. CREAR RESERVA.")
    print("2. BUSCAR RESERVA.")
    print("3. VOLVER A MENÚ ANTERIOR.\n")