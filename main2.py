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
                opcion_user = usuario_cont.cliente_controlador()
                if opcion_user not in [1,2,3,4,5]:
                    continue
                match opcion_user:
                    case 1:
                        while True:
                            opcion_user = destino_cont.destino_controlador_admin() 
                            if opcion_user == 1:  
                                destino_cont.crear_destino()
                            elif opcion_user == 2: 
                                destino_cont.buscar_destino()
                            elif opcion_user == 3: 
                                destino_cont.modificar_destino()
                            elif opcion_user == 4: 
                                destino_cont.eliminar_destino()
                            elif opcion_user == 5: 
                                break
                    case 2: 
                        while True:
                            opcion_user = paquete_cont.paquete_controlador_admin()
                            if opcion_user == 1:
                                paquete_cont.crear_paquete()
                            elif opcion_user == 2:
                                paquete_cont.buscar_paquete()
                            elif opcion_user == 3:
                                paquete_cont.modificar_paquete()
                            elif opcion_user == 4:
                                paquete_cont.eliminar_paquete()
                            elif opcion_user == 5:
                                break
                    case 3: 
                        while True:
                            opcion_user = usuario_cont.funciones_usuario_admin()
                            if opcion_user == 1:
                                usuario_cont.modificar_usuario()
                            elif opcion_user == 2:
                                usuario_cont.eliminar_usuario_admin()
                            elif opcion_user == 3:
                                break
                    case 4: 
                        while True:
                            opcion_user = reserva_cont.reserva_controlador_admin()
                            if opcion_user == 1:
                                reserva_cont.obtener_reserva_por_id()
                            elif opcion_user == 2:
                                reserva_cont.eliminar_reserva()
                            elif opcion_user == 3:
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
                            opcion_user = reserva_cont.funciones_reserva_cliente()
                            if opcion_user == 1:  
                                reserva_cont.crear_reserva(usuario.id_usuario)
                            elif opcion_user == 2: 
                                reserva_cont.obtener_reserva_por_id()
                            elif opcion_user == 3: 
                                reserva_cont.eliminar_reserva()
                            elif opcion_user == 4: 
                                break 
                    case 4: 
                        while True:
                            opcion_user = usuario_cont.funciones_usuario_cliente()
                            if opcion_user == 1:  
                                usuario_cont.modificar_usuario(usuario)
                            elif opcion_user == 2: 
                                usuario_cont.eliminar_usuario_basico(usuario)
                            elif opcion_user == 3: 
                                break
                    case 5: 
                        break

if __name__ == "__main__":
    main()
