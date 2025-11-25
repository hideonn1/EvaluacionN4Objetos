## controlador de destinos_view
from ..vista.destinos_view import eliminar_destino_vista, modificar_destino_vista
class Destino_Controller:
    
    def __init__(self, usuario_service):
        # Recibe el Servicio por inyección. No sabe nada de repositorios o DB.
        self._service = usuario_service

    def buscar_destino(self, destino_nombre):        
        try:
            destino_encontrado = self._service.obtener_destino_por_nombre(destino_nombre)
            
            print(f"\nDestino encontrado: {destino_encontrado}")
            
        except ValueError as e:
            print(f"\n[CONTROLADOR] ❌ -> Error capturado: {e}")

    def crear_destino(self):
        while True:
            try:
                nombre = input("Ingrese el nombre del destino: ")
                if not nombre or not all(c.isalpha() or c.isspace() for c in nombre):
                    raise ValueError("Ingrese un nombre válido (solo letras y espacios).")
                
                if self._service.obtener_destino_por_nombre(nombre) is not None:
                    print("Ya existe un destino con ese nombre. Inténtelo de nuevo.")
                    continue

                break
            except ValueError as Error:
                print(f"Error inesperado al ingresar el nombre: {Error}")
        while True:
            try:
                pais = input("Ingrese el Pais de ubicacion: ")
                if not pais or not all(c.isalpha() or c.isspace() for c in pais):
                    raise ValueError("Ingrese un Pais valido (solo letras y espacios).")
                break
            except ValueError as e:
                print("Error en ingresar un Pais valido.")
        while True:
            try:
                ciudad = input("Ingrese la ciudad del destino: ")
                if not ciudad or not all(c.isalpha() or c.isspace() for c in ciudad):
                    raise ValueError("Ingrese una ciudad valida (solo letras y espacios).")
                break
            except ValueError as e:
                print("Error en ingresar una ciudad valida.")
        while True: 
            try:
                descripcion = input("Ingrese una descripcion del destino: ")
                break
            except ValueError as e:
                print("Error en ingresar una descripcion valida.")
        while True:
            try:
                actividades_disponibles = input("Ingrese las actividades disponibles del destino: ")
                break
            except ValueError as e:
                print("Error en ingresar una actividad valida.")
        while True:
            try:
                costo = int(input("Ingrese el costo del destino: "))
                if costo <= 0:
                    raise ValueError("El costo del destino debe ser un numero mayor que 0")
                break
            except ValueError as e:
                print("Error! Ingrese un costo valido.")
        datos_destino = {
            'nombre':nombre,
            'ciudad':ciudad,
            'pais':pais,
            'descripcion':descripcion,
            'actividades_disponibles':actividades_disponibles,
            'costo':costo}
        
        self._service.nuevo_destino(datos_destino)
    def eliminar_destino(self):
        opcion = int(input(eliminar_destino_vista()))
        while opcion not in [1,2,3]:
            print("Error. Opcion no encontrada")
            opcion = int(input(eliminar_destino_vista()))
        match opcion:
            case 1:
                while True:
                    try:
                        id_destino = int(input("Ingrese el id del destino"))
                        break
                    except ValueError as e:
                        print(e)
                self._service.eliminar_destino_por_id(id_destino)
            case 2:
                while True:
                    try:
                        nombre_destino = input("Ingrese el id del destino")
                        if not nombre_destino or not all(c.isalpha() or c.isspace() for c in nombre_destino):
                            raise ValueError("Ingrese un Pais valido (solo letras y espacios).")
                        break
                    except ValueError as e:
                        print(e)
                self._service.eliminar_destino_por_nombre(nombre_destino)
            case 3:
                print("Será devuelto al menu anterior...")
                input("PRESIONE ENTER PARA CONTINUAR")
                return
    def modificar_destino(self):
        opcion = int(input(modificar_destino_vista()))
        while opcion not in [1,2,3]:
            print("Error. Opcion no encontrada")
            opcion = int(input(modificar_destino_vista()))
        match opcion:
            case 1:
                while True:
                    try:
                        id_destino = int(input("Ingrese el id del destino"))
                        break
                    except ValueError as e:
                        print(e)
                destino_objeto = self._service.buscar_destino_por_id(id_destino)
                nuevo_destino = self.modificar_datos_objeto(destino_objeto)
                self._service.modificar_destino(nuevo_destino)
            case 2:
                while True:
                    try:
                        nombre_destino = input("Ingrese el nombre del destino")
                        if not nombre_destino or not all(c.isalpha() or c.isspace() for c in nombre_destino):
                            raise ValueError("Ingrese un Pais valido (solo letras y espacios).")
                        break
                    except ValueError as e:
                        print(e)
                destino_objeto = self._service.buscar_destino_por_nombre(nombre_destino)
                nuevo_destino = self.modificar_datos_objeto(destino_objeto)
                self._service.modificar_destino(nuevo_destino)
            case 3:
                print("Será devuelto al menu anterior...")
                input("PRESIONE ENTER PARA CONTINUAR")
                return
            
    def modificar_datos_objeto(self, destino):
        print(destino)
        print("\n ¿Que campo desea modificar?")
        print("1. Nombre")
        print("2. Descripcion")
        print("3. Actividades disponibles")
        print("4. Costo")
        print("5. Cancelar y volver al menu anterior")

        try: 
            opcion = int(input("Seleccione una opcion (1-5): "))
            while opcion not in [1,2,3,4,5]:
                print("Error al ingresar una opcion, intenelo denuevo")
                opcion = int(input("Seleccione una opcion (1-5): "))    
        except ValueError as e:
            print(e)

        match opcion:
            case 1:
                while True:
                    try:
                        nombre = input("Ingrese el nombre del destino: ")
                        if not nombre or not all(c.isalpha() or c.isspace() for c in nombre):
                            raise ValueError("Ingrese un nombre valido (solo letras y espacios).")
                        if self._service.obtener_destino_por_nombre(nombre) != None:
                            print("Ya existe un destino con ese nombre. Intentelo denuevo")
                        break
                    except ValueError as e:
                        print("Error en ingresar nombre.")
                    destino.nombre = nombre
                    return destino
            case 2:
                while True: 
                    try:
                        descripcion = input("Ingrese una descripcion del destino: ")
                        break
                    except ValueError as e:
                        print("Error en ingresar una descripcion valida.")
                    destino.descripcion = descripcion
                    return destino
            case 3:
                while True:
                    try:
                        actividades_disponibles = input("Ingrese las actividades disponibles del destino: ")
                        break
                    except ValueError as e:
                        print("Error en ingresar una actividad valida.")
                    destino.actividades_disponibles = actividades_disponibles
                    return destino
            case 4:
                while True:
                    try:
                        costo = input("Ingrese el costo del destino: ")
                        if costo <= 0:
                            raise ValueError("El costo del destino debe ser un numero mayor que 0")
                        break
                    except ValueError as e:
                        print("Error! Ingrese un costo valido.")
                    destino.costo = costo
                    return destino
            case 5:
                return
