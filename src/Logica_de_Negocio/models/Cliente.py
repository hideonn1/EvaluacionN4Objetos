# Clase de Cliente heredera de la clase abstracta Persona.

from .Persona import Persona

class Cliente(Persona):
    def __init__ (self,
                  id_cliente,
                  rut,
                  nombres,
                  apellido_paterno,
                  apellido_materno,
                  email,
                  contraseña_hash,
                  telefono,
                  fecha_nacimiento,
                  fecha_registro,
                  rol="Cliente"):
        
        super().__init__(id_cliente,
                       rut,
                       nombres,
                       apellido_paterno,
                       apellido_materno,
                       email,
                       contraseña_hash,
                       telefono,
                       fecha_nacimiento,
                       fecha_registro,
                       rol)
        
        self.id_cliente = id_cliente

    def __str__(self):
        return (f"Usuario ID: {self.id_usuario}, "
                f"Nombre: {self.nombres} {self.apellido_paterno}, "
                f"Email: {self.email}")
    def iniciar_sesion(self):
        pass
    
    def validar_rut(self):
        pass

    def crear_reserva_turistica():
        pass

    def buscar_reserva_turistica():
        pass

# Métodos propios de la clase abstracta Persona
    def buscar_destino():
        pass

    def iniciar_sesion():
        pass

