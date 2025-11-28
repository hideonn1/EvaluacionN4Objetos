## controlador de paquete_turistico_view.py

from ..vista.destinos_view import mostrar_destinos
from ..vista.paquete_turistico_view import menu_paquete_turistico
from ...Logica_de_Negocio.models.PaqueteTuristico import PaqueteTuristico
from datetime import datetime
class Paquete_Controller:
    def __init__(self, paquete_service, destino_service):
        # Recibe el Servicio por inyección. No sabe nada de repositorios o DB.
        self._service = paquete_service
        self._service_destino = destino_service

    def mostrar_destinos(self,id_paquete):

        paquete_objeto = self._service.buscar_paquete(id_paquete)
        lista_destinos = paquete_objeto.destinos

        return lista_destinos

    def mostrar_paquete(self, id_paquete):
        paquete_objeto = self._service.buscar_paquete(id_paquete)
        print(paquete_objeto)

    def agregar_destino(self,paquete):
        lista_destinos = self._service_destino.mostrar_destinos()
        mostrar_destinos(lista_destinos)

        while True:
            try:
                destino_id = int(input("Ingrese el ID del destino que quiere agregar al paquete."))
                break

            except ValueError as Error:
                print(f"Debe ingresar un número válido: {Error}")
        try:
            self._service.agregar_destino_a_paquete(paquete.id_paquete, destino_id)
            print("Destino agregado correctamente al paquete.")
        except ValueError as Error:
            print(f"Error: {Error}")
        self._service.agregar_destino_a_paquete(paquete.id_paquete, destino_id)


    def agregar_destino_paquete(self,id_paquete=None):
        while True:
            try:
                pais = input("Ingrese un Pais para ver sus destinos disponibles: ")
                ###Verificacion pais
                while True:
                    try:
                        lista_destino = self._service_destino.obtener_destinos_por_pais(pais)
                        for i in lista_destino:
                            print(i)
                        destino_id = int(input("Ingrese el id del destino que quiere agregar al paquete (0 para cancelar operacion: "))
                        duplicado = False
                        if id_paquete: 
                            duplicado = self._service.duplicidad_verf(destino_id,id_paquete)
                        if duplicado == True:
                            print("No puede ingresar destinos duplicados!")
                            continue
                        destino_paquete = self._service_destino.obtener_destino_por_id(destino_id)
                        if destino_paquete != None:
                            break
                        else:
                            print("No se ha encontrado un destino con esa id, intentelo denuevo")
                    except Exception as e:
                        print(e)
            except Exception as e:
                print (e)
            return destino_paquete


    def fecha_salida_ver(self, fecha_inicio=None):
        while True:
            try:
                fecha_salida = input("Ingrese la fecha de salida del destino (formato DD/MM/AAAA): ")
                fecha = datetime.strptime(fecha_salida, '%d/%m/%Y').date()
                
                verf = self._service.confirmar_fecha_salida(fecha, fecha_inicio)
                if verf == True:
                    print(f"Fecha ingresada correctamente: {fecha}")
                    return fecha
                else:
                    print (verf)
            except ValueError:
                print("Formato inválido. Use el formato DD/MM/AAAA.")
        
    def fecha_llegada_ver(self, fecha_final=None):
        while True:
            try:
                fecha_llegada = input("Ingrese la fecha de llegada del destino (formato DD/MM/AAAA): ")
                fecha = datetime.strptime(fecha_llegada, '%d/%m/%Y').date()
                verf = self._service.confirmar_fecha_llegada(fecha, fecha_final)
                if verf == True:
                    print(f"Fecha ingresada correctamente: {fecha}")
                    return fecha
                else:
                    print (verf)
            except ValueError:
                print("Formato inválido. Use el formato DD/MM/AAAA.")

    def crear_paquete(self):
            destino_objeto = self.agregar_destino_paquete()
            fecha_salida = self.fecha_salida_ver()
            fecha_llegada = self.fecha_llegada_ver(fecha_salida)
            nuevo_paquete = PaqueteTuristico(fecha_llegada = fecha_llegada,
                                             fecha_salida = fecha_salida,
                                             costo_destino = destino_objeto.costo
            )
            destino_objeto.fecha_inicio = fecha_salida
            destino_objeto.fecha_final = fecha_llegada
            destino_objeto.orden_visita = 1
            print(destino_objeto)
            paquete_completo = self._service.agregar_paquete(nuevo_paquete)
            self._service.agregar_destino_a_paquete(paquete_completo,destino_objeto)
            try:
                while True:
                    respuesta = input("Desea ingresar otro destino? [si/no]: ")
                    if respuesta.lower() == 'si':
                        self.nuevo_destino(paquete_completo)
                    elif respuesta.lower() == 'no':
                        break
                    else:
                        print("Error, debe ingresar una respuesta valida!")
            except ValueError as e:
                print(e)

    def nuevo_destino(self, paquete):
        destino_paquete = self.agregar_destino_paquete(paquete.id_paquete)
        while True:
            fecha_salida = self.fecha_salida_ver(paquete.fecha_salida)
            fecha_llegada = self.fecha_llegada_ver(paquete.fecha_llegada)
            destino_paquete.fecha_inicio = fecha_salida
            destino_paquete.fecha_llegada = fecha_llegada
            break
        self._service.agregar_destino_a_paquete(paquete,destino_paquete)
        
        

    def paquete_controleitor(self):
        try:
            menu_paquete_turistico()
            opcion = int(input("Seleccione una opcion (1-5: "))
            while opcion not in [1,2,3,4,5]:
                print("Error al ingresar una opcion, intentelo denuevo")
                opcion = int(input("Seleccione una opcion (1-5): "))
        except ValueError as e:
            print(e)
        match opcion:
            case 1:
                #crear
                pass
            case 2:
                #buscar
                pass
            case 3:
                #actualizar
                pass
            case 4:
                #eliminar
                pass
            case 5:
                return
