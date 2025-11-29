# Clase de Administrador heredera de Persona.

from .Persona import Persona

class Administrador(Persona):
    def __init__ (self,
                  id_administrador,
                  rut,
                  nombres,
                  apellido_paterno,
                  apellido_materno,
                  email,
                  contraseña_hash,
                  telefono,
                  fecha_nacimiento,
                  fecha_registro):
        
        super().__init__(id_administrador,
                       rut,
                       nombres,
                       apellido_paterno,
                       apellido_materno,
                       email,
                       contraseña_hash,
                       telefono,
                       fecha_nacimiento,
                       fecha_registro)
        
        self.id_administrador = id_administrador

    def crear_destino(self):
        pass

    def buscar_destino(self):
        pass

    def modificar_destino(self):
        pass

    def eliminar_destino(self):
        pass

# Métodos propios de la clase abstracta Persona.
    def iniciar_sesion(self):
        pass

    def validar_rut(self):
        pass