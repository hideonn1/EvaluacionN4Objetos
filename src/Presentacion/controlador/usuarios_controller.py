## controlador de usuarios

# Módulo: usuario_controller.py
import bcrypt
import re
from datetime import datetime
import pwinput
from ...Logica_de_Negocio.models.Cliente import Cliente
from ..vista.principal_view import principal_view_inicio_sesion, principal_view_menu_admin, principal_view_menu_cliente
from ..vista.usuario_view import modificar_usuario_vista
from ..vista.reservas_view import sub_menu_reserva_cliente

class Usuario_Controller:
    
    def __init__(self, usuario_service):
        # Recibe el Servicio por inyección. No sabe nada de repositorios o DB.
        self._service = usuario_service
        
    def _validar_contraseña_segura(self, contraseña):
        if len(contraseña) < 8:
            raise ValueError("La contraseña debe tener al menos 8 caracteres.")
        if not re.search(r"[A-Z]", contraseña):
            raise ValueError("La contraseña debe tener al menos una letra mayúscula.")
        if not re.search(r"[a-z]", contraseña):
            raise ValueError("La contraseña debe tener al menos una letra minúscula.")
        if not re.search(r"[0-9]", contraseña):
            raise ValueError("La contraseña debe tener al menos un número.")
        return True

    def buscar_usuario(self, email_input):        
        try:
            usuario_encontrado = self._service.obtener_usuario_por_email(email_input)
            
            print(f"\nUsuario encontrado: {usuario_encontrado}")
            
        except ValueError as e:
            print(f"\nError capturado: {e}")

    def iniciar_sesion(self):
        usuario = None
        while True:
            try:
                email = input("Ingrese el email del empleado (ej: usuario@dominio.cl) o 'salir' para volver: ").strip()
                if email.lower() == 'salir':
                    return None
                patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"               
                if not re.match(patron, email):
                    raise ValueError("Formato de email inválido. Intente nuevamente.")
                usuario = self._service.obtener_usuario_por_email(email)
                if usuario == None:
                    raise ValueError ("Este email no existe en el sistema")
                break
            except ValueError as Error:
                print(Error)
        
        while True:
            contraseña_ingresada = pwinput.pwinput("Ingrese su contraseña: ", mask="*").strip()
            if not contraseña_ingresada:
                print("La contraseña no puede estar vacía. Intente nuevamente.")
                continue
            
            # Pass email to verify password
            if self._service.verificar_contrasena(email, contraseña_ingresada) == False:  
                print("Contraseña erronea")
            else:
                print("Sesión iniciada exitosamente!")
                return usuario # Return user on success

    
    def registrar_usuario(self):
        while True:
            try:
                email = input("Ingrese el email del empleado (ej: usuario@dominio.cl): ").strip()
                patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"               
                if not re.match(patron, email):
                    raise ValueError("Formato de email inválido. Intente nuevamente.")
                if self._service.obtener_usuario_por_email(email) != None:
                    raise ValueError ("Este email existe en el sistema. ")
                break
            except ValueError as Error:
                print(Error)

        while True:
            try: 
                nombre = input("Ingrese el primer nombre del empleado: ").strip()
                if not nombre or not all(c.isalpha() or c.isspace() for c in nombre):
                    raise ValueError("Ingrese un nombre válido (solo letras y espacios).")
                break
            except ValueError as Error:
                print(Error)
        
        while True:
            try: 
                apellido_paterno = input("Ingrese el apellido paterno del empleado: ").strip()
                if not apellido_paterno or not all(c.isalpha() or c.isspace() for c in apellido_paterno):
                    raise ValueError("Ingrese un apellido paterno válido (solo letras y espacios).")
                break
            except ValueError as Error:
                print(Error)

        while True:
            try: 
                apellido_materno = input("Ingrese el apellido materno del empleado: ").strip()
                if not apellido_materno or not all(c.isalpha() or c.isspace() for c in apellido_materno):
                    raise ValueError("Ingrese un apellido materno válido (solo letras y espacios).")
                break
            except ValueError as Error:
                print(Error)  

        while True:
            try:
                rut = input("Ingrese su RUT: (ej: 12345678-K o 9876543-1): ").strip().lower()
                rut_formateado, es_valido = self._service.validador_rut(rut)
                if not es_valido:
                     raise ValueError("RUT inválido.")
                
                # Check if RUT exists in DB
                if self._service.obtener_usuario_por_rut(rut_formateado):
                    raise ValueError("El RUT ya se encuentra registrado en el sistema.")
                
                rut = rut_formateado # Use formatted RUT
                break
            except ValueError as e:
                print(f"Error: {e}")
        
        while True:
            try:
                fecha = input("Ingrese la fecha de nacimiento del empleado (formato DD/MM/AAAA): ")
                fecha_nacimiento = datetime.strptime(fecha, '%d/%m/%Y').date()

                if self._service.mayor_a_18(fecha_nacimiento) == False:   
                    print("Usted no tiene 18 años.")
                    return
                break
            except ValueError:
                print("Formato inválido. Use el formato DD/MM/AAAA.")

        
        while True:
            try:
                nro_telefono = input("Ingrese el número de teléfono del empleado (formato: +56 9 XXXX XXXX): ").strip()
                patron = r"^\+56 9 \d{4} \d{4}$"
                if not re.match(patron, nro_telefono):
                    raise ValueError("Formato inválido. Use: +56 9 XXXX XXXX")
                
                # Check if phone exists
                if self._service.verificar_numero(nro_telefono): 
                    raise ValueError("Numero ya registrado en la base de datos")
                break
            except ValueError as Error:
                print(Error)

        # Auto-assign role as Cliente for registration
        rol_usuario = "Cliente"

        # Use current date for registration
        fecha_registro = datetime.now().date()

        while True:
            try:
                contraseña_texto_plano = pwinput.pwinput("Ingrese la contraseña para el nuevo usuario: ", mask="*")
                if self._validar_contraseña_segura(contraseña_texto_plano) == True:
                    contraseña_hash = bcrypt.hashpw(contraseña_texto_plano.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
                    break
            except ValueError as Error:
                # Asumo que validar_contraseña_segura levanta ValueError
                print(Error)
            except Exception as Error: 
                print(f"Error inesperado al guardar la contraseña: {Error}")

        try:
            registro = {'rut': rut, 'nombre':nombre, 'apellido_paterno': apellido_paterno, 
                        'apellido_materno': apellido_materno, 'email':email, 'contraseña': contraseña_hash,
                        'rol': rol_usuario, 'telefono': nro_telefono, 'fecha_nacimiento': fecha_nacimiento,
                        'fecha_registro': fecha_registro}
            
            if self._service.nuevo_usuario(registro) == True: 
                print("Usuario registrado con exito. ")
                return
        except Exception as e:
            print(f"Error al crear el objeto: {e}")
        
            
    def modificar_usuario_admin(self):
        email = input("Ingrese el email del empleado (ej: usuario@dominio.cl): ").strip()
        patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"               
        if not re.match(patron, email):
            raise ValueError("Formato de email inválido. Intente nuevamente.")
        usuario = self._service.obtener_usuario_por_email(email) 
        if usuario != None:
            opcion = int(input(modificar_usuario_vista()))
            if opcion in [1,2,3,4,5,6,7,8,9,10]:
                match opcion:
                    case 1:
                        while True:
                            try:
                                rut = input("Ingrese su rut: ")
                                rut_validado = self._service.validador_rut(rut)
                                if rut_validado == True:
                                    usuario.rut = rut_validado
                                    self._service.modificar_usuario_admin(usuario)
                                    return
                                else:
                                    return
                            except ValueError as Error:
                                print(Error)
                    case 2:
                        while True:
                            try: 
                                nombre = input("Ingrese el primer nombre del empleado: ")
                                if not nombre or not all(c.isalpha() or c.isspace() for c in nombre):
                                    raise ValueError("Ingrese un nombre válido (solo letras y espacios).")
                                usuario.nombres = nombre
                                self._service.modificar_usuario_admin(usuario)
                                return
                            except ValueError as Error:
                                print(Error)
                    case 3:
                        while True:
                            try: 
                                apellido_paterno = input("Ingrese el apellido paterno del empleado: ")
                                if not apellido_paterno or not all(c.isalpha() or c.isspace() for c in apellido_paterno):
                                    raise ValueError("Ingrese un apellido paterno válido (solo letras y espacios).")
                                usuario.apellido_paterno = apellido_paterno
                                self._service.modificar_usuario_admin(usuario)
                                return
                            except ValueError as Error:
                                print(Error)
                    case 4:
                        while True:
                            try: 
                                apellido_materno = input("Ingrese el apellido materno del empleado: ")
                                if not apellido_materno or not all(c.isalpha() or c.isspace() for c in apellido_materno):
                                    raise ValueError("Ingrese un apellido materno válido (solo letras y espacios).")
                                usuario.apellido_materno = apellido_materno
                                self._service.modificar_usuario_admin(usuario)
                                return
                            except ValueError as Error:
                                print(Error) 
                    case 5:
                        while True:
                            try:
                                email_nuevo = input("Ingrese el email del empleado (ej: usuario@dominio.cl): ").strip()
                                patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"               
                                if not re.match(patron, email_nuevo):
                                    raise ValueError("Formato de email inválido. Intente nuevamente.")
                                # Verificar que el nuevo email no esté ya en uso por otro usuario
                                usuario_existente = self._service.obtener_usuario_por_email(email_nuevo)
                                if usuario_existente and usuario_existente.id_usuario != usuario.id_usuario:
                                    raise ValueError("Este email ya está en uso por otro usuario.")
                                usuario.email = email_nuevo
                                self._service.modificar_usuario_admin(usuario)
                                return
                            except ValueError as Error:
                                print(Error)
                                
                    case 6:
                        while True:
                            try:
                                contraseña_texto_plano = input("Ingrese la contraseña actual: ")
                                if self._validar_contraseña_segura(contraseña_texto_plano) == True:
                                    contraseña_actual = bcrypt.hashpw(contraseña_texto_plano.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
                                    validado = self._service.verificador_contraseña(contraseña_actual)
                                    if validado == True:
                                        break
                                    else:
                                        print("La contraseña que ingresaste no se encuentra registrada")
                                        return
                            except ValueError as Error:
                                # Asumo que validar_contraseña_segura levanta ValueError
                                print(Error)
                            except Exception as Error: 
                                print(f"Error inesperado al guardar la contraseña: {Error}")
                        while True:
                            try:
                                contraseña_texto_plano = input("Ingrese la contraseña nueva: ")
                                if self._validar_contraseña_segura(contraseña_texto_plano) == True:
                                    contraseña_hash = bcrypt.hashpw(contraseña_texto_plano.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
                                    usuario.contraseña = contraseña_hash
                                    self._service.modificar_usuario_admin(usuario)
                                    return
                            except ValueError as Error:
                                # Asumo que validar_contraseña_segura levanta ValueError
                                print(Error)
                            except Exception as Error: 
                                print(f"Error inesperado al guardar la contraseña: {Error}")
                    case 7:
                        while True:
                            try:
                                nro_telefono = input("Ingrese el número de teléfono del empleado (formato: +56 9 XXXX XXXX): ").strip()
                                patron = r"^\+56 9 \d{4} \d{4}$"
                                if not re.match(patron, nro_telefono):
                                    raise ValueError("Formato inválido. Use: +56 9 XXXX XXXX")
                                if self._service.verificar_numero(nro_telefono) == True: 
                                    usuario.telefono = nro_telefono
                                    self._service.modificar_usuario_admin(usuario)
                                return
                            except ValueError as Error:
                                print(Error)
                    case 8:
                        while True:
                            try:
                                fecha = input("Ingrese la fecha de nacimiento del empleado (formato DD/MM/AAAA): ")
                                fecha_nacimiento = datetime.strptime(fecha, '%d/%m/%Y').date()

                                if self._service.mayor_a_18(fecha_nacimiento) == False:   
                                    print("Usted no tiene 18 años.")
                                    continue
                                if self._service.mayor_a_18(fecha_nacimiento) == True:
                                    usuario.fecha_nacimiento = fecha_nacimiento
                                    self._service.modificar_usuario_admin(usuario)
                                return
                            except ValueError:
                                print("Formato inválido. Use el formato DD/MM/AAAA.")
                    case 9:
                        input("PRESIONE ENTER PARA SALIR ")
                        return None    



    def eliminar_usuario_admin(self):
        while True:
            try:
                email = input("Ingrese el email del empleado (ej: usuario@dominio.cl): ").strip()
                patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"               
                if not re.match(patron, email):
                    raise ValueError("Formato de email inválido. Intente nuevamente.")
                if self._service.obtener_usuario_por_email(email) != None:
                    while True:
                        try:
                            print("Desea eliminar de forma permanente a este usuario? ")
                            print("1.- Eliminar permanentemente ")
                            print("2.- No Eliminar\n ")
                            respuesta = int(input("Elija una opcion: "))
                            if respuesta not in [1, 2]:
                                raise ValueError("Las opciones de respuesta son solo '1' o '2'. ")
                            elif respuesta == 1:
                                self._service.eliminar_usuario_admin(email)
                                print("Usuario eliminado. ")
                                break
                            else:
                                break
                        except ValueError as Error:
                            print(Error)
                    break
                if self._service.obtener_usuario_por_email(email) == None:
                    raise ValueError("No se encontro este correo en la base de datos.")
            except ValueError as Error:
                print(Error)

    def eliminar_usuario_basico(self, usuario:Cliente):
        while True:
            try:
                email_usuario = usuario.email
                print(f"Desea eliminar la cuenta de usuario, email:{email_usuario}? ")
                print("1.- Eliminar permanentemente ")
                print("2.- No Eliminar\n ")
                respuesta = int(input("Elija una opcion: "))
                if respuesta not in [1, 2]:
                    raise ValueError("Las opciones de respuesta son solo '1' o '2'. ")
                elif respuesta == 1:
                    self._service.eliminar_usuario_admin(email_usuario)
                    print("Usuario eliminado. ")
                    break
                else:
                    break
            except ValueError as Error:
                print(Error)

    def menu_controlador(self):
        while True:
            principal_view_inicio_sesion()
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
                    usuario = self.iniciar_sesion()
                    return usuario
                case 2:
                    self.registrar_usuario()
                case 3:
                    input("PRESIONE ENTER PARA SALIR ")
                    return None     
        

    def admin_controlador(self):
        while True:
            principal_view_menu_admin()
            try:
                opcion_user = int(input("Ingrese una de las opciones disponibles (1-5): "))
            except ValueError:
                print("Debe ingresar un carácter numérico para continuar.")
                continue

            if opcion_user not in (1,2,3,4,5):
                print("Debe ingresar una de las opciones disponibles para continuar.")
                continue 
            return opcion_user
        
                
    def cliente_controlador(self):
        while True:
            principal_view_menu_cliente()
            try:
                opcion_user = int(input("Ingrese una de las opciones disponibles (1-5): "))
            except ValueError:
                print("Debe ingresar un carácter numérico para continuar.")
                continue

            if opcion_user not in (1,2,3,4,5):
                print("Debe ingresar una de las opciones disponibles para continuar.")
                continue
            return opcion_user  
        
    def funciones_reserva_cliente(self):
        while True:
            sub_menu_reserva_cliente()
            try:
                opcion_user = int(input("Ingrese una de las opciones disponibles (1-3): "))
            except ValueError:
                print("Debe ingresar un carácter numérico para continuar.")
                continue

            if opcion_user not in (1,2,3,4,5):
                print("Debe ingresar una de las opciones disponibles para continuar.")
                continue
            return opcion_user 
