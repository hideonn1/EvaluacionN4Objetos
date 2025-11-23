## archivo encargado de logica y comunicar a usuarios_service con usuarios_controller
import bcrypt
from models.Cliente import Cliente
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
        usuario_objeto = Cliente(#llenar con datos que estan dentro de registro)
        self._repo.create(usuario_objeto)
    
    #solo repositorios usan base de datos
    