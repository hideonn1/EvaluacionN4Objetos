## vista encargada de mostrar destinos disponibles al usuario

def eliminar_destino_vista():
    print("---Gestor de Destinos---\n")
    print("---ELIJA UNA OPCION ---\n")
    print("1. ELIMINAR DESTINO POR NOMBRE.")
    print("2. ELIMINAR DESTINO POR ID.")    
    print("3. VOLVER AL MENU ANTERIOR.\n")
    return "Seleccione una opcion (1-3): "

def modificar_destino_vista():
    print("---Gestor de Destinos---\n")
    print("---ELIJA UNA OPCION ---\n")
    print("1. MODIFICAR DESTINO POR NOMBRE.")
    print("2. MODIFICAR DESTINO POR ID.")
    print("3. VOLVER AL MENU ANTERIOR.\n")
    return "Seleccione una opcion (1-3): "

def modificar_destino_escogido_vista():
    print("\n ¿Que campo desea modificar?")
    print("1. Nombre")
    print("2. Descripcion")
    print("3. Actividades disponibles")
    print("4. Costo")
    print("5. Cancelar y volver al menu anterior")

def buscar_destino_vista():
    print("---Gestor de Destinos---\n")
    print("---ELIJA UNA OPCION ---\n")
    print("1. BUSCAR DESTINO POR NOMBRE.")
    print("2. BUSCAR DESTINO POR ID.")
    print("3. VOLVER AL MENU ANTERIOR.\n")
    return "Seleccione una opcion (1-3): "

def mostrar_destinos(lista_destinos):
    if not lista_destinos:
        print("\n--- No se encontraron destinos disponibles. ---")
        return

    # Imprimir encabezado de la tabla
    print("\n=================================================================================")
    print("              🗺️ DESTINOS DISPONIBLES EN LA BASE DE DATOS 🗺️")
    print("=================================================================================")
    print(f"{'ID':<4} | {'ORDEN':<6} | {'NOMBRE':<30} | {'CIUDAD':<20} | {'COSTO APROX.':<15}")
    print("---------------------------------------------------------------------------------")
    
    # Recorrer e imprimir cada diccionario de destino
    for destino in lista_destinos:
        # Extraer los datos clave para la presentación
        destino_id = destino.get('id_destino', 'N/A')
        nombre = destino.get('nombre', 'N/A')
        ciudad = destino.get('ciudad', 'N/A')
        costo = destino.get('costo', 0)
        
        # ⚠️ Nota: El orden de visita ('orden_visita') solo existe si la lista proviene
        # de una relación de paquete (como en tu ejemplo de lista). 
        # Usamos .get() para evitar errores si no está presente.
        orden = destino.get('orden_visita', '-')

        # Imprimir la fila formateada
        print(f"{destino_id:<4} | {orden:<6} | {nombre:<30} | {ciudad:<20} | ${costo:<14,.0f}")
        
        # Opcional: Mostrar descripción y actividades
        descripcion = destino.get('descripcion', '')
        actividades = destino.get('actividades_disponibles', '')
        
        if descripcion or actividades:
            print(f"       {'Descripción: ' + descripcion[:80]:<80}")
            print(f"       {'Actividades: ' + actividades[:80]:<80}")
            print("---------------------------------------------------------------------------------")


    print("=================================================================================\n")

    
def sub_menu_destinos_admin():
    print("---Gestor de Destinos---\n")
    print("---ELIJA UNA OPCION ---")
    print("1. AGREGAR DESTINO.")
    print("2. BUSCAR DESTINO.")
    print("3. MODIFICAR DESTINO.")
    print("4. ELIMINAR DESTINO.")
    print("5. VOLVER AL MENU ANTERIOR.\n")