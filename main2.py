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
from src.Presentacion.vista.usuario_view import sub_menu_usuario

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
    # Reservas_Controller only accepts reserva_service, unlike main.py which passed extra args
    reserva_cont = Reservas_Controller(reserva_serv) 
    ############################################################

    while True:
        usuario = usuario_cont.menu_controlador()
        if usuario is None:
            print("Saliendo del programa...")
            break
        
        # Check role
        if usuario.rol == "Administrador":
            while True:
                opcion_user = usuario_cont.admin_controlador()
                if opcion_user == 1: # Gestion Destino
                    destino_cont.destino_controleitor()
                elif opcion_user == 2: # Gestion Paquete
                    paquete_cont.paquete_controleitor()
                elif opcion_user == 3: # Gestion Usuario
                    self._view.sub_menu_usuario()
                    try:
                        sub_op = int(input("Seleccione una opcion: "))
                        if sub_op == 1:
                            usuario_cont.modificar_usuario_admin(usuario)
                        elif sub_op == 2:
                            usuario_cont.eliminar_usuario_admin(usuario)
                    except ValueError:
                        print("Opcion invalida")
                elif opcion_user == 4: # Buscar Reservas
                    reserva_cont.obtener_reserva_por_id()
                elif opcion_user == 5: # Volver/Salir
                    break
        
        elif usuario.rol == "Cliente":
             while True:
                opcion_user = usuario_cont.cliente_controlador()
                if opcion_user not in [1,2,3,4,5]:
                    continue
                match opcion_user:
                    case 1: # Buscar Destino por Pais
                        destino_cont.probar_destino()
                    case 2: # Buscar Paquete
                        print("Funcionalidad de buscar paquete aun no implementada completamente.")
                    case 3: # Gestion Reserva
                        while True:
                            op_reserva = usuario_cont.funciones_reserva_cliente()
                            if op_reserva == 1: # Crear
                                # Try to get ID from usuario object
                                user_id = getattr(usuario, 'id_usuario', getattr(usuario, 'id_cliente', None))
                                if user_id:
                                    reserva_cont.crear_reserva(user_id)
                                else:
                                    print("Error: No se pudo identificar al usuario.")
                            elif op_reserva == 2: # Buscar
                                reserva_cont.obtener_reserva_por_id()
                            elif op_reserva == 3: # Volver
                                break
                    case 4: # Gestion Usuario (Mi Cuenta)
                        while True:
                            sub_menu_usuario()
                            try:
                                sub_op = int(input("Seleccione una opcion: "))
                                if sub_op not in [1,2,3]:
                                    print("Opcion invalida, debe estar en el rango [1,3]")
                                    continue
                                elif sub_op == 1:
                                    usuario_cont.modificar_usuario(usuario)
                                    # Check if user still exists (simple check if we can find by email)
                                    if usuario_cont._service.obtener_usuario_por_email(usuario.email) is None:
                                        break # Logout if delet
                                elif sub_op == 2:
                                    usuario_cont.eliminar_usuario(usuario)
                                    # Check if user still exists (simple check if we can find by email)
                                    if usuario_cont._service.obtener_usuario_por_email(usuario.email) is None:
                                        break # Logout if deleted
                                else:
                                    break
                            except ValueError:
                                print("Opcion invalida")
                    case 5: # Volver/Salir
                        break

if __name__ == "__main__":
    main()
