## archivo encargado de logica y comunicar a usuarios_service con usuarios_controller

class Usuario_Service:
    
    def __init__(self, usuario_repository):
        # Recibe el Repositorio por inyección. No sabe nada de conexiones.
        self._repo = usuario_repository 

    def obtener_usuario_por_email(self, email):
        usuario_objeto = self._repo.get_by_email(email)
        if usuario_objeto is None:
            raise ValueError(f"El usuario con email {email} no existe.")
        return usuario_objeto