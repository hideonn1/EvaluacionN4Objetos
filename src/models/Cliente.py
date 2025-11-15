# Clase de Cliente heredera de la clase abstracta Persona.

from Persona import Persona

class Cliente(Persona):
    def __init__ (self,
                  id_cliente,
                  rut,
                  nombre,
                  apellido_paterno,
                  apellido_materno,
                  email,
                  contraseña_hash,
                  telefono,
                  direccion,
                  fecha_nacimiento,
                  fecha_registro):
        
        super().__init__(self,
                       rut,
                       nombre,
                       apellido_paterno,
                       apellido_materno,
                       email,
                       contraseña_hash,
                       telefono,
                       direccion,
                       fecha_nacimiento,
                       fecha_registro)
        
        self.id_cliente = id_cliente

    def crear_reserva_turistica():
        pass

    def buscar_reserva_turistica():
        pass

# Métodos propios de la clase abstracta Persona
    def buscar_destino():
        pass

    def iniciar_sesion():
        pass