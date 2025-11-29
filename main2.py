from config import conectar_db
import mysql.connector
from src.Datos.usuario_repository import Usuario_Repository
from src.Logica_de_Negocio.usuarios_service import Usuario_Service
from src.Presentacion.controlador.usuarios_controller import Usuario_Controller
from src.Datos.destino_repository import Destino_Repository
from src.Logica_de_Negocio.destino_service import Destino_Service
from src.Presentacion.controlador.destinos_controller import Destino_Controller
from src.Datos.paquete_turistico_repository import Paquete_Repository
from src.Logica_de_Negocio.paquete_turistico_service import Paquete_Service
from src.Presentacion.controlador.paquete_turistico_controller import Paquete_Controller
from src.Datos.reserva_repository import Reservas_Repository
from src.Logica_de_Negocio.reservas_service import Reservas_Service
from src.Presentacion.controlador.reservas_controller import Reservas_Controller

def main():
    ## BLOQUE DE DEPENDENCIAS ##
    usuario_repo = Usuario_Repository(conectar_db)
    usuario_serv = Usuario_Service(usuario_repo)
    usuario_cont = Usuario_Controller(usuario_serv)

    destino_repo = Destino_Repository(conectar_db)
    destino_serv = Destino_Service(destino_repo)
    destino_cont = Destino_Controller(destino_serv)

    paquete_repo = Paquete_Repository(conectar_db)
    paquete_serv = Paquete_Service(paquete_repo, destino_repo)
    paquete_cont = Paquete_Controller(paquete_serv,destino_serv)

    reserva_repo = Reservas_Repository(conectar_db)
    reserva_serv = Reservas_Service(reserva_repo)
    reserva_cont = Reservas_Controller(reserva_serv) 
    ############################################################

    while True:
        usuario = usuario_cont.menu_controlador()
        if usuario is None:
            print("Saliendo del programa...")
            break
        
        if usuario.rol == "Administrador":
            while True:
                opcion_user = usuario_cont.admin_controlador() 
                if opcion_user not in [1,2,3,4,5]:
                    continue
                match opcion_user:
                    case 1:  # Gestión Destinos
                        while True:
                            op_destino = destino_cont.destino_controlador_admin()
                            if op_destino == 1:
                                destino_cont.crear_destino()
                            elif op_destino == 2:
                                destino_cont.buscar_destino()
                            elif op_destino == 3:
                                destino_cont.modificar_destino()
                            elif op_destino == 4:
                                destino_cont.eliminar_destino()
                            elif op_destino == 5:
                                break
                    case 2:  # Gestión Paquetes
                        while True:
                            op_paquete = paquete_cont.paquete_controlador_admin()
                            if op_paquete == 1:
                                paquete_cont.crear_paquete()
                            elif op_paquete == 2:
                                paquete_cont.buscar_paquete()
                            elif op_paquete == 3:
                                paquete_cont.modificar_paquete()
                            elif op_paquete == 4:
                                paquete_cont.eliminar_paquete()
                            elif op_paquete == 5:
                                break
                    case 3:  # Gestión Usuarios
                        while True:
                            print("\n--- GESTIÓN USUARIOS ---")
                            print("1. Modificar Usuario")
                            print("2. Eliminar Usuario")
                            print("3. Volver")
                            try:
                                sub_op = int(input("Seleccione una opcion: "))
                                if sub_op == 1:
                                    email = input("Ingrese el email del usuario a modificar: ").strip()
                                    usuario_modificar = usuario_cont._service.obtener_usuario_por_email(email)
                                    if usuario_modificar:
                                        usuario_cont.modificar_usuario(usuario_modificar)
                                    else:
                                        print("Usuario no encontrado.")
                                elif sub_op == 2:
                                    usuario_cont.eliminar_usuario_admin()
                                elif sub_op == 3:
                                    break
                            except ValueError:
                                print("Opcion invalida")
                    case 4:  
                        while True:
                            op_reserva = reserva_cont.reserva_controlador_admin(usuario)
                            if op_reserva == 1:
                                reserva_cont.obtener_reserva_por_id()
                            elif op_reserva == 2:
                                reserva_cont.eliminar_reserva()
                            elif op_reserva == 3: 
                                break
                            elif op_reserva == 4: 
                                break
                    case 5: 
                        break
            
        elif usuario.rol == "Cliente":
             while True:
                opcion_user = usuario_cont.cliente_controlador()
                if opcion_user not in [1,2,3,4,5]:
                    continue
                match opcion_user:
                    case 1:  
                        destino_cont.probar_destino()
                    case 2:  
                        paquete_cont.buscar_paquete()
                    case 3:  
                        while True:
                            op_reserva = usuario_cont.funciones_reserva_cliente()
                            if op_reserva not in [1,2,3,4]:
                                continue
                            if op_reserva == 1:  
                                user_id = getattr(usuario, 'id_usuario', getattr(usuario, 'id_cliente', None))
                                if user_id:
                                    reserva_cont.crear_reserva(user_id)
                                else:
                                    print("Error: No se pudo identificar al usuario.")
                            elif op_reserva == 2:  
                                reserva_cont.obtener_reserva_por_id()
                            elif op_reserva == 3:  
                                reserva_cont.eliminar_reserva()
                            elif op_reserva == 4:  
                                break
                    case 4: 
                        while True:
                            print("\n--- MI CUENTA ---")
                            print("1. Modificar mis datos")
                            print("2. Eliminar mi cuenta")
                            print("3. Volver")
                            try:
                                sub_op = int(input("Seleccione una opcion: "))
                                if sub_op == 1:
                                    usuario_cont.modificar_usuario(usuario)
                                elif sub_op == 2:
                                    usuario_cont.eliminar_usuario_basico(usuario)
                                    if usuario_cont._service.obtener_usuario_por_email(usuario.email) is None:
                                        break  
                                elif sub_op == 3:
                                    break
                            except ValueError:
                                print("Opcion invalida")
                    case 5:  
                        break

if __name__ == "__main__":
    main()