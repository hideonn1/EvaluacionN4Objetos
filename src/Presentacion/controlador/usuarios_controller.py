## controlador de usuarios

# Módulo: usuario_controller.py
import pwinput
import re
from datetime import datetime

class Usuario_Controller:
    
    def __init__(self, usuario_service):
        # Recibe el Servicio por inyección. No sabe nada de repositorios o DB.
        self._service = usuario_service
        
    def buscar_usuario(self, email_input):        
        try:
            usuario_encontrado = self._service.obtener_usuario_por_email(email_input)
            
            print(f"\nUsuario encontrado: {usuario_encontrado}")
            
        except ValueError as e:
            print(f"\n[CONTROLADOR] ❌ -> Error capturado: {e}")

    def iniciar_sesion(self):
        while True:
            try:
                email = input("Ingrese el email del empleado (ej: usuario@dominio.cl): ").strip()
                patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"               
                if not re.match(patron, email):
                    raise ValueError("Formato de email inválido. Intente nuevamente.")
                if self._service.obtener_usuario_por_email(email) == None:
                    raise ValueError ("Este email no existe en el sistema")
                break
            except ValueError as Error:
                print(Error)
        
        while True:
            contraseña_ingresada = pwinput.pwinput("Ingrese su contraseña: ", mask="*").strip()
            if not contraseña_ingresada:
                print("La contraseña no puede estar vacía. Intente nuevamente.")
            if self._service.verificar_contrasena(contraseña_ingresada) == False:  
                print("Contraseña erronea")
            else:
                print("Sesión iniciada exitosamente!")
            break
        return True
    def registrar_usuario(self):
        while True:
            try:
                email = input("Ingrese el email del empleado (ej: usuario@dominio.cl): ").strip()
                patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"               
                if not re.match(patron, email):
                    raise ValueError("Formato de email inválido. Intente nuevamente.")
                if self._service.obtener_usuario_por_email(email) != None:
                    raise ValueError ("Este email existe en el sistema")
                break
            except ValueError as Error:
                print(Error)

        
        
        while True:
            try:
                fecha_nacimiento = input


            registro = {'nombre':nombre, 'email': email }
            if self._service.nuevo_usuario(registro) == True: 
                print("Usuario registrado con exito")
                return 
            
    def modificar_usuario(self):

            
