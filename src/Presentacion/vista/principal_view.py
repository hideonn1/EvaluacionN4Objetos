## vista encargada de mostrar la interfaz principal del programa

def pincipal_view_inicio_sesion():
        while True:
            print("---Sistema gestor de Viajes Aventura---\n")
            print("---ELIJA UNA OPCIÓN ---\n")
            print("1. INICIAR SESIÓN.")
            print("2. REGISTRARSE.")
            print("3. CERRAR EL PROGRAMA.\n")
            try:
                opcion_user = int(input("Ingrese una de las opciones disponibles (1-3): "))
            except ValueError:
                print("Debe ingresar un carácter numérico para continuar.")
                continue

            if opcion_user not in (1,2,3):
                print("Debe ingresar una de las opciones disponibles para continuar.")
                continue

            match opcion_user:
                case 1:
                    usuario = iniciar_sesion()
                    return usuario
                case 2:
                    registrar_usuario()

                case 3:
                    input("PRESIONE ENTER PARA SALIR ")
                    break