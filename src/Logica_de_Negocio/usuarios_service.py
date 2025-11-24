## archivo encargado de logica y comunicar a usuarios_service con usuarios_controller
import bcrypt
<<<<<<< HEAD
from models.Cliente import Cliente
from datetime import date
import re
=======
from .models.Cliente import Cliente
>>>>>>> b8ec2f3c7ef1a5337d9a387c478a52ec3b076f1e
class Usuario_Service:
    
    def __init__(self, usuario_repository):
        # Recibe el Repositorio por inyección. No sabe nada de conexiones.
        self._repo = usuario_repository 

    def obtener_usuario_por_email(self, email):
        usuario_objeto = self._repo.get_by_email(email)
        if usuario_objeto is None:
            raise ValueError(f"El usuario con email {email} no existe.")
        return usuario_objeto
    
    def verificar_contrasena(self, email, contraseña_ingresada):
        usuario_objeto = self._repo.get_by_email(email)
        if usuario_objeto is None:
            raise ValueError(f"El usuario con email {email} no existe.")
        if bcrypt.checkpw(contraseña_ingresada.encode('utf-8'), usuario_objeto.contraseña_hash.encode('utf-8')):
            return True
        return False
    
    def nuevo_usuario(self, registro):
<<<<<<< HEAD
        usuario_objeto = Cliente(
                    rut = registro['rut'],
                    nombres = registro['nombres'],
                    apellido_paterno = registro['apellido_paterno'],
                    apellido_materno = registro['apellido_materno'],
                    email = registro['email'],
                    contraseña_hash = ['contraseña'],
                    rol_usuario = ['rol'],
                    telefono = registro['telefono'],
                    direccion = registro['direccion'],
                    fecha_nacimiento = registro['fecha_nacimiento'],
                    fecha_registro = registro['fecha_registro']
                )
=======
        usuario_objeto = Cliente()#llenar con datos que estan dentro de registro)
>>>>>>> b8ec2f3c7ef1a5337d9a387c478a52ec3b076f1e
        self._repo.create(usuario_objeto)

    def eliminar_usuario_admin(self, email):
        self._repo.delete(email)

    def eliminar_usuario_basico(self, rut):
        self._repo.delete(rut)
    
    def modificar_usuario_admin(self, email):
        pass

    def modificar_usuario_basico(self, rut):
        pass

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

        return rut.upper()

    def mayor_a_18(self, fecha_nacimiento: date):
        hoy = date.today()

        fecha_cumple_18 = fecha_nacimiento.replace(year=fecha_nacimiento.year + 18)

        if hoy >= fecha_cumple_18:
            return True
        else:
            return False

    #solo en repositorios usan base de datos
    