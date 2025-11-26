## vista encargada de mostrar el paquete turistico formado por el cliente
from datetime import datetime

def crear_paquete_vista():
    print("\n--- CREAR PAQUETE TURÍSTICO ---")
    while True:
        try:
            fecha_llegada = input("Ingrese fecha de llegada (YYYY-MM-DD): ").strip()
            fecha_salida = input("Ingrese fecha de salida (YYYY-MM-DD): ").strip()
            datetime.strptime(fecha_llegada, "%Y-%m-%d")
            datetime.strptime(fecha_salida, "%Y-%m-%d")
            break
        except ValueError:
            print("Formate inválido. Use YYYY-MM-DD.")

        try:
            orden_visita = int(input("Ingrese el orden de visita: "))
        except ValueError:
            print("Debe ingresar un carácter numérico para indicar el orden.")
        
        try:
            costo_destino = int(input("Ingrese el costo total del paquete: "))
        except ValueError:
            print("Debe ingresar un carácter numérico para indicar el costo total.")

    return {
        "fecha_llegada":fecha_llegada,
        "fecha_salida":fecha_salida,
        "orden_visita":orden_visita,
        "costo_destino":costo_destino
    }

def mostrar_paquete_vista(paquete):
    print("\n--- PAQUETE TURÍSTICO ---")
    print(f"ID: {paquete.id_paquete}")
    print(f"Fecha llegada: {paquete.fecha_llegada}")
    print(f"Fecha salida: {paquete.fecha_salida}")
    print(f"Orden de visita: {paquete.orden_visita}")
    print(f"Costo destino: {paquete.costo_destino}")

    if hasattr(paquete,"destinos") and paquete.destinos:
        print("\nDestinos incluidos:")
        for destino in paquete.destinos:
            print(f" - {destino['nombre']} {destino['ciudad']}, {destino['pais']} - Costo: {destino['costo']}")
    else:
        print("\nEste paquete no tiene destinos asociados.")

def menu_paquete_turistico():
    return (
        "\n--- MENÚ PAQUETE TURÍSITCO ---\n"
        "1. Crear paquete\n"
        "2. Buscar paquete por ID\n"
        "3. Actualizar paquete\n"
        "4. Eliminar paquete\n"
        "5. Agregar destino a paquete\n"
        "6. Volver al menú principal\n"
        "Seleccione una opción: "
    )