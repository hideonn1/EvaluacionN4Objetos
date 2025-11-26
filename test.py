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

    usuario_cont.registrar_usuario()
    #destino_cont.buscar_destino_nombre("mi_casa")
    #destino_cont.buscar_destino_id(1)
    #paquete_cont.mostrar_paquete(1)

    destino_cont.probar_destino()
    """
    usuario = usuario_cont.menu_controlador()
    if usuario.rol == "Administrador":
        opcion_user = usuario_cont.admin_controlador()

    #usuario = usuario_cont.menu_controlador()
    #if usuario.rol == "Administrador":
    """    opcion_user = usuario_cont.admin_controlador()

        match opcion_user:
                case 1:
                    paquete_cont._self.crear_destino()
                case 2:
                    paquete_cont._self.modificar_destino()
                case 3:
                    paquete_cont._self.eliminar_destino()
                case 4:
                    pass
                case 5:
                    pass
                case 6:
                    pass
                case 7:
                    pass
                case 8:
                    paquete_cont._self.eliminar_usuario_admin()
                case 9:
                    paquete_cont._self.obtener_reserva_por_id()
                case 10:
                    input("PRESIONE ENTER PARA SALIR ")
                    return None     
    else:

        usuario_cont.cliente_controlador()"""

        usuario_cont.cliente_controlador()

>>>>>>> 43cbf49c783b9d7f5a462fb1540649f606beae92


"""
main()