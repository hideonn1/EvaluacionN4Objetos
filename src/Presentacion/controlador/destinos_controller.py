## controlador de destinos_view

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
                    raise ValueError("Ingrese un nombre valido (solo letras y espacios).")
                if self._service.obtener_destino_por_nombre(nombre) != None:
                    print("Ya existe un destino con ese nombre. Intentelo denuevo")
                break
            except ValueError as e:
                print("Error en ingresar nombre.")
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
                print("Error en ingresar una ciudad valida.")
        while True:
            try:
                costo = input("Ingrese el costo del destino: ")
                if costo <= 0:
                    raise ValueError("El costo del destino debe ser un numero mayor que 0")
                break
            except ValueError as e:
                print("Error! Ingrese un costo valido.")