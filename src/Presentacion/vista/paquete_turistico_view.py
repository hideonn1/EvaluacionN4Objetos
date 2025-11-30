## vista encargada de mostrar el paquete turistico formado por el cliente
from datetime import datetime

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
        "---ELIJA UNA OPCIÓN ---\n"
        "1. CREAR PAQUETE\n"
        "2. BUSCAR PAQUETE POR ID\n"
        "3. ACTUALIZAR PAQUETE\n"
        "4. ELIMINAR PAQUETE\n"
        "5. VOLVER AL MENÚ PRINCIPAL\n"
    )

def modificar_paquete_vista():
    return (
        "\n--- MENU MODIFICACION PAQUETE TURÍSITCO ---\n"
        "1. AGREGAR NUEVO DESTINO\n"
        "2. QUITAR UN DESTINO\n"
        "3. VOLVER AL MENU ANTERIOR\n"
    )
