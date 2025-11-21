## controlador de usuarios

# Módulo: usuario_controller.py

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
