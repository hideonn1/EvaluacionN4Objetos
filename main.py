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
                    destino_cont.destino_controleitor()
                case 2:
                    paquete_cont.paquete.controleitor() #crear controlador y vista de menu de paquetes
                    pass
                case 3:
                    usuario_cont.usuario.controleitor() #crear controlador y vista de menu de usuarios (contiene modificar y eliminar)
                case 4:
                    reserva_cont.obtener_reserva_por_id()
                case 5:
                    input("PRESIONE ENTER PARA SALIR ")
                    return None     
    else:
        usuario = usuario_cont.menu_controlador()
        if usuario.rol == "Cliente":
            opcion_user = usuario_cont.admin_controlador()        

            match opcion_user:
                case 1:
                    self._service.obtener_destinos_por_pais()
                case 2:
                    #buscar_paquete_turistico() #crear esta funcion
                    pass
                case 3:
                    paquete_cont.funciones_reserva_cliente #crear esta funcion
                case 4:
                    paquete_cont.funciones_usuario_cliente #crear esta funcion
                    pass
                case 5:
                    input("PRESIONE ENTER PARA SALIR ")
                    return None   
