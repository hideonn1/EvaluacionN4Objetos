## archivo encargado de logica y comunicar a usuarios_service con usuarios_controller
import bcrypt
from .models.Cliente import Cliente
from datetime import date
import re

class Usuario_Service:
    
    def __init__(self, usuario_repository):
        # Recibe el Repositorio por inyección. No sabe nada de conexiones.
        self._repo = usuario_repository 

    def obtener_usuario_por_email(self, email):
        usuario_objeto = self._repo.get_by_email(email)
        return usuario_objeto
    
    def verificar_contrasena(self, email, contraseña_ingresada):
        usuario_objeto = self._repo.get_by_email(email)
        if usuario_objeto is None:
            raise ValueError(f"El usuario con email {email} no existe.")
        # Check if password matches
        if bcrypt.checkpw(contraseña_ingresada.encode('utf-8'), usuario_objeto.contraseña_hash.encode('utf-8')):
            return True
        return False
    
    def nuevo_usuario(self, registro):
        usuario_objeto = Cliente(
            id_cliente=None,
            rut=registro['rut'],
            nombres=registro['nombre'],
            apellido_paterno=registro['apellido_paterno'],
            apellido_materno=registro['apellido_materno'],
            email=registro['email'],
            contraseña_hash=registro['contraseña'],
            telefono=registro['telefono'],
            fecha_nacimiento=registro['fecha_nacimiento'],
            fecha_registro=registro['fecha_registro'],
            rol=registro['rol']
        )
        self._repo.create(usuario_objeto)
        return True

    def eliminar_usuario_admin(self, email):
        self._repo.delete(email)

    def eliminar_usuario_basico(self, email):
        self._repo.delete(email)
    
    def modificar_usuario_admin(self, email):
        self._repo.update(email)

    def modificar_usuario_basico(self, email):
        self._repo.update(email)

    def validador_rut(self, rut):
        rut = rut.strip().lower()
        if rut.count('-') != 1:
            raise ValueError("El RUT debe contener un solo guion ('-').")

        parte_num, dv = rut.split('-')

        if len(rut) < 9 or len(rut) > 10:
            raise ValueError("El RUT debe tener entre 9 y 10 caracteres en total.")

        if not parte_num.isdigit():
            raise ValueError("Los caracteres antes del guion deben ser solo números.")

        if len(parte_num) not in [7, 8]:
            raise ValueError("La parte numérica del RUT debe tener 7 u 8 dígitos.")

        if dv not in ['0','1','2','3','4','5','6','7','8','9','k']:
            raise ValueError("El dígito verificador debe ser un número o la letra 'k'.")

        return rut.upper(), True

    def mayor_a_18(self, fecha_nacimiento: date):
        hoy = date.today()

        fecha_cumple_18 = fecha_nacimiento.replace(year=fecha_nacimiento.year + 18)

        if hoy >= fecha_cumple_18:
            return True
        else:
            return False
        
    def verificar_numero(self, numero):
        return self._repo.get_telefono(numero)

    def obtener_usuario_por_rut(self, rut):
        return self._repo.get_by_rut(rut)

    def verificador_contraseña(self, contraseña_nueva):
        return self._repo.get_contraseña(contraseña_nueva)