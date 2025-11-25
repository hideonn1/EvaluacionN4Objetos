## vista encargada de mostrar los datos de la reserva del cliente
from datetime import datetime

def crear_reserva_vista():
    print("\n--- CREAR RESERVA ---")
    while True:
        try:
            fecha_inicio = input("Ingrese fecha de inicio (YYYY-MM-DD): ")
            fecha_final = input("Ingrese fecha final (YYYY-MM-DD): ")
            #Validaciones de fecha :
            datetime.strptime(fecha_inicio, "%Y-%m-%d")
            datetime.strptime(fecha_final, "%Y-%m-%d")
            break
        except ValueError:
            print("Formato inválido. Use YYYY-MM-DD.")

        monto_total = int(input("Ingrese monto total: "))

    return {
        "fecha_inicio": fecha_inicio,
        "fecha_final": fecha_final,
        "monto_total": monto_total
    }

def mostrar_reserva(reserva):
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
        "1. Crear reserva\n"
        "2. Buscar reserva por ID\n"
        "3. Actualizar reserva\n"
        "4. Eliminar reserva\n"
        "5. Volver al menú principal\n"
        "Seleccione una opción: "
    )