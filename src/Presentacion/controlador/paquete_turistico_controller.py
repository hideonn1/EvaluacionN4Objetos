## controlador de paquete_turistico_view.py

from ..vista.destinos_view import mostrar_destinos
from ..vista.paquete_turistico_view import menu_paquete_turistico, modificar_paquete_vista
from ...Logica_de_Negocio.models.PaqueteTuristico import PaqueteTuristico
from datetime import datetime, timedelta
class Paquete_Controller:
    def __init__(self, paquete_service, destino_service):
        # Recibe el Servicio por inyección. No sabe nada de repositorios o DB.
        self._service = paquete_service
        self._service_destino = destino_service

    def mostrar_destinos(self,id_paquete):

        paquete_objeto = self._service.buscar_paquete(id_paquete)
        lista_destinos = paquete_objeto.destinos

        return lista_destinos

    def buscar_paquete(self):
        while True:
            try:
                id_paquete_input = input("Ingrese ID del paquete (o 0 para cancelar): ")
                
                if id_paquete_input == '0':
                    print("Búsqueda cancelada.")
                    return None

                id_paquete = int(id_paquete_input)
                
                paquete_objeto = self._service.obtener_paquete_por_id(id_paquete)
                
                print("\n Paquete Encontrado:")
                print(paquete_objeto) 
                
                return paquete_objeto
                
            except ValueError:
                print("\n Error de formato: Por favor, ingrese un número entero válido para el ID.")
                
            except Exception as e:
                print(f"\n Error de Búsqueda: {e}")

    
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
                while True: 
                    pais = input("Ingrese un Pais para ver sus destinos disponibles: ")
                    if not pais or not all(c.isalpha() or c.isspace() for c in pais):
                        print("Error: Ingrese un Pais válido (solo letras y espacios).")
                        continue 
                    lista_destino = self._service_destino.obtener_destinos_por_pais(pais)
                    if len(lista_destino) < 1:
                        raise ValueError("Error! No se ha encontrado destinos en el país especificado.")
                    break 

                while True:
                    mostrar_destinos(lista_destino)
                    destino_id_input = input("Ingrese el id del destino que quiere agregar (0 para cancelar): ")
                    if destino_id_input == '0':
                        print("Operación cancelada.")
                        return None 
                    destino_id = int(destino_id_input) 
                    
                    if id_paquete and self._service.duplicidad_verf(destino_id, id_paquete):
                        print("No puede ingresar destinos duplicados!")
                        continue 
                    
                    destino_paquete = self._service_destino.obtener_destino_por_id(destino_id)
                    
                    if destino_paquete is None:
                        print("No se ha encontrado un destino con ese ID, inténtelo de nuevo.")
                        continue                      
                    break 
                return destino_paquete

            except ValueError as e:
                print(f"Error de formato o validación: {e}")

            except Exception as e:
                print(f"Error inesperado del sistema: {e}")
                return None 

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
        
    def fecha_llegada_ver(self, fecha_inicio=None):
        while True:
            try:
                duracion = int(input("Ingrese la duracion del destino: "))
                if duracion <= 0:
                    print("Error! la duracion debe ser igual o mayor a 1 dia")
                elif duracion > 30:
                    print("Error! la duracion no debe superar los 30 dias.")
                else:
                    break
            except ValueError:
                print("Error! debe ingresar un numero para la duracion de dias.")
        fecha_final = fecha_inicio + timedelta(days = duracion)
        return fecha_final

    def crear_paquete(self):
            destino_objeto = self.agregar_destino_paquete()
            if destino_objeto == None:
                print("Será devuelto al menu anterior")
                return
            fecha_salida = self.fecha_salida_ver()
            fecha_llegada = self.fecha_llegada_ver(fecha_salida)
            multiplicador = self._service.obtener_multiplicador(fecha_salida)
            nuevo_paquete = PaqueteTuristico(fecha_llegada = fecha_llegada,
                                             fecha_salida = fecha_salida,
                                             costo_destino = destino_objeto.costo * multiplicador
            )
            destino_objeto.fecha_salida = fecha_salida
            destino_objeto.fecha_llegada = fecha_llegada
            destino_objeto.orden_visita = 1
            paquete_completo = self._service.agregar_paquete(nuevo_paquete)
            self._service.agregar_destino_a_paquete(paquete_completo,destino_objeto)
            while True:
                try:
                    respuesta = input("Desea ingresar otro destino? [si/no]: ").strip()
                    if respuesta.lower() == 'si':
                        self.nuevo_destino(paquete_completo)
                    elif respuesta.lower() == 'no':
                        return
                    else:
                        print("Error, debe ingresar una respuesta valida!")
                except ValueError as e:
                    print(e)

    def nuevo_destino(self, paquete):
        destino_paquete = self.agregar_destino_paquete(paquete.id_paquete)
        destino_paquete.fecha_salida = paquete.fecha_llegada
        while True:
            fecha_llegada = self.fecha_llegada_ver(paquete.fecha_llegada)
            destino_paquete.fecha_llegada = fecha_llegada
            break
        self._service.agregar_destino_a_paquete(paquete,destino_paquete)

    def quitar_destino(self, paquete):
        while True:
            try:
                lista_destinos = self.mostrar_destinos(paquete.id_paquete)
                input("")
                orden_destino = int(input("Ingrese el orden de visita del destino que desea eliminar: "))
                ordenes_validas = [d['orden_visita'] for d in lista_destinos]
                if orden_destino not in ordenes_validas:
                    raise ValueError ("El numero de orden ingresado no existe en este paquete turistico.")
                break
            except ValueError as e:
                print(e)
            except Exception as f:
                print(f)
        while True:
            try:
                print(f"Esta seguro que desea eliminar este destino?")
                opcion = input("Para confirmar escriba 'si' o 'no': ")
                while opcion.lower() != 'si' and opcion.lower() != 'no':
                    print("Error. Las unicas opciones disponibles son 'si' o 'no' ")
                    opcion = input("Para confirmar escriba 'si' o 'no': ")
                if opcion.lower() == 'si':
                    self._service.quitar_destino(paquete.id_paquete, orden_destino)
                    print("Destino eliminado")
                    return
            except Exception as e:
                print(e)
        
    def modificar_paquete(self):
        while True:
            try:
                print(modificar_paquete_vista())
                opcion = int(input("Selecciona una opcion (1-3): "))
                while opcion not in [1,2,3]:
                    print("Error al ingresar una opcion, intentelo denuevo.")
                    opcion = int(input("Selecciona una opcion (1-3): "))
                match opcion:
                    case 1:
                        paquete = self.buscar_paquete()
                        if paquete:
                            self.nuevo_destino(paquete)
                    case 2:
                        paquete = self.buscar_paquete()
                        if paquete:
                            self.quitar_destino(paquete)
                    case 3:
                        return
            except ValueError as e:
                print(e)
        
    def eliminar_paquete(self):
        paquete = self.buscar_paquete()
        if not paquete:
            return
        while True:
            try:
                while True:
                    print(f"Esta seguro que desea eliminar este paquete?")
                    opcion = input("Para confirmar escriba 'si' o 'no': ")
                    if opcion.lower() == 'si':
                        self._service.quitar_paquete(paquete.id_paquete)
                        print("Paquete eliminado")
                        return
                    elif opcion.lower() == 'no' :
                        print("No se ha eliminado el paquete.")
                        input("PRESIONE ENTER PARA CONTINUAR")
                        return
                    else:
                        print("No se ha ingresado una opcion valida, intentelo denuevo.")
            except Exception as e:
                print(e)


    def paquete_controlador_admin(self):
        while True:
            print(menu_paquete_turistico())
            try:
                opcion_user = int(input("Seleccione una opcion (1-5): "))
            except ValueError:
                print("Debe ingresar un carácter numérico para continuar.")
                continue

            if opcion_user not in (1,2,3,4,5):
                print("Debe ingresar una de las opciones disponibles para continuar.")
                continue
            return opcion_user 


