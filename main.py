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
    reserva_serv = Reservas_Service(reserva_repo, paquete_repo, usuario_repo)
    reserva_cont = Reservas_Controller(reserva_serv, paquete_serv, usuario_serv)
    ############################################################


    usuario = usuario_cont.menu_controlador()
    if usuario.rol == "Administrador":
        opcion_user = usuario_cont.admin_controlador()
        match opcion_user:
                case 1:
                    destino_cont.crear_destino()
                case 2:
                    destino_cont.modificar_destino()
                case 3:
                    destino_cont.eliminar_destino()
                case 4:
                    paquete_cont.crear_paquete()
                    pass
                case 5:
                    paquete_cont.modificar_paquete()
                    pass
                case 6:
                    paquete_cont.eliminar_paquete()
                    pass
                case 7:
                    usuario_cont.modificar_usuario_admin()
                    pass
                case 8:
                    usuario_cont.eliminar_usuario_admin()
                case 9:
                    reserva_cont.obtener_reserva_por_id()
                case 10:
                    input("PRESIONE ENTER PARA SALIR ")
                    return None     
    else:
        usuario_cont.cliente_controlador()
