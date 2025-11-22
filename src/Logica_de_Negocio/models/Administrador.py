# Clase de Administrador heredera de Persona.

from Persona import Persona

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
                  direccion,
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
                       direccion,
                       fecha_nacimiento,
                       fecha_registro)
        
        self.id_administrador = id_administrador

    def crear_destino():
        pass

    def buscar_destino():
        pass

    def modificar_destino():
        pass

    def eliminar_destino():
        pass

# Métodos propios de la clase abstracta Persona.
    def iniciar_sesion():
        pass

    def validar_rut():
        pass