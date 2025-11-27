## vista encargada de mostrar destinos disponibles al usuario

def eliminar_destino_vista():
    print("---Sistema gestor de Destinos---\n")
    print("---ELIJA UNA OPCION ---\n")
    print("1. ELIMINAR DESTINO POR NOMBRE.")
    print("2. ELIMINAR DESTINO POR ID.")    
    print("3. VOLVER AL MENU ANTERIOR.\n")

def modificar_destino_vista():
    print("---Sistema gestor de Destinos---\n")
    print("---ELIJA UNA OPCION ---\n")
    print("1. MODIFICAR DESTINO POR NOMBRE.")
    print("2. MODIFICAR DESTINO POR ID.")
    print("3. VOLVER AL MENU ANTERIOR.\n")

def modificar_destino_escogido_vista():
    print("\n ¿Que campo desea modificar?")
    print("1. Nombre")
    print("2. Descripcion")
    print("3. Actividades disponibles")
    print("4. Costo")
    print("5. Cancelar y volver al menu anterior")

def buscar_destino_vista():
    print("---Sistema gestor de Destinos---\n")
    print("---ELIJA UNA OPCION ---\n")
    print("1. BUSCAR DESTINO POR NOMBRE.")
    print("2. BUSCAR DESTINO POR ID.")
    print("3. VOLVER AL MENU ANTERIOR.\n")

def mostrar_destinos(lista):
    for i in lista:
        print (i)

def sub_menu_destinos_admin():
    print("---Sistema gestor de Destinos---\n")
    print("---ELIJA UNA OPCION ---")
    print("1. AGREGAR DESTINO.")
    print("2. BUSCAR DESTINO.")
    print("3. MODIFICAR DESTINO.")
    print("4. ELIMINAR DESTINO.")
    print("5. VOLVER AL MENU ANTERIOR.\n")

