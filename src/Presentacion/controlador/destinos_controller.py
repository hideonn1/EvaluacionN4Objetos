## controlador de destinos_view
from ..vista.destinos_view import eliminar_destino_vista, modificar_destino_vista, buscar_destino_vista, modificar_destino_escogido_vista
class Destino_Controller:
    
    def __init__(self, usuario_service):
        # Recibe el Servicio por inyección. No sabe nada de repositorios o DB.
        self._service = usuario_service

    def buscar_destino(self):   
        opcion = int(input(buscar_destino_vista()))
        while opcion not in [1,2,3]:
            print("Error. Opcion no encontrada")
            opcion = int(input(buscar_destino_vista()))
        match opcion:
            case 1:
                while True:
                    try:
                        destino_nombre = input("Ingrese el nombre del destino: ")
                        if not destino_nombre or not all(c.isalpha() or c.isspace() for c in destino_nombre):
                            raise ValueError("Ingrese un nombre valido (solo letras y espacios)")
                        destino_objeto = self._service.obtener_destino_por_nombre(destino_nombre)
                        if destino_objeto == None:
                            raise Exception("No existe un destino con ese nombre")
                        break    
                    except Exception as e:
                        print("Error inesperado")
            case 2:
                while True:
                    try:
                        destino_id = int(input("Ingrese el ID del destino: "))
                        destino_objeto = self._service.obtener_destino_por_id(destino_id)
                        if destino_objeto == None:
                            raise FileNotFoundError("No existe un destino con ese nombre")
                        break    
                    except Exception as e:
                        print("Error inesperado")
                    except ValueError as v:
                        print("Los IDs de destino solo deben contener numeros")
            case 3:
                return

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
                pais = input("Ingrese el país de ubicación: ")
                if not pais or not all(c.isalpha() or c.isspace() for c in pais):
                    raise ValueError("Ingrese un Pais valido (solo letras y espacios).")
                break
            except ValueError as e:
                print(f"Error inesperado al ingresar el país: {e}")
        while True:
            try:
                ciudad = input("Ingrese la ciudad del destino: ")
                if not ciudad or not all(c.isalpha() or c.isspace() for c in ciudad):
                    raise ValueError("Ingrese una ciudad valida (solo letras y espacios).")
                break
            except ValueError as e:
                print(f"Error inesperado al ingresar la ciudad: {e}")
        while True: 
            try:
                descripcion = input("Ingrese una descripcion del destino: ")
                break
            except ValueError as e:
                print(f"Error inesperado al ingresar la descripción: {e}")
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
            case 2:
                while True:
                    try:
                        id_destino = int(input("Ingrese el id del destino"))
                        destino_objeto = self._service.buscar_destino_por_id(id_destino)
                        if destino_objeto == None:
                            raise FileNotFoundError ("No se ha encontrado un destino con ese id intenelo denuevo")
                        break
                    except ValueError as e:
                        print("Error, los IDs solo pueden ser numeros")
                while True: 
                    try:
                        print(f"Esta seguro que desea eliminar {destino_objeto}?")
                        opcion.lower() = input("Para confirmar escriba 'si' o 'no'")
                        while opcion != 'si' or opcion != 'no':
                            print("Error. Las unicas opciones disponibles son 'si' o 'no' ")
                            opcion.lower() = input("Para confirmar escriba 'si' o 'no'")
                        if opcion == 'si':
                            self._service.eliminar_destino_por_id(id_destino)
                        elif opcion == 'no':
                            return
                    except ValueError:
                        print("Error al ingresar una opcion")
            case 1:
                while True:
                    try:
                        nombre_destino = input("Ingrese el nombre del destino")
                        if not nombre_destino or not all(c.isalpha() or c.isspace() for c in nombre_destino):
                            raise ValueError("Ingrese un nombre valido (solo letras y espacios).")
                        destino_objeto = self._service.buscar_destino_por_nombre(nombre_destino)
                        if destino_objeto == None:
                            raise FileNotFoundError ("No se ha encontrado un destino con ese nombre, intenelo denuevo")
                        break
                    except ValueError as e:
                        print(e)
                while True: 
                    try:
                        print(f"Esta seguro que desea eliminar {destino_objeto}?")
                        opcion.lower() = input("Para confirmar escriba 'si' o 'no'")
                        while opcion != 'si' or opcion != 'no':
                            print("Error. Las unicas opciones disponibles son 'si' o 'no' ")
                            opcion.lower() = input("Para confirmar escriba 'si' o 'no'")
                        if opcion == 'si':
                            self._service.eliminar_destino_por_nombre(nombre_destino)
                        elif opcion == 'no':
                            return
                    except ValueError:
                        print("Error al ingresar una opcion")
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
        modificar_destino_escogido_vista()
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
