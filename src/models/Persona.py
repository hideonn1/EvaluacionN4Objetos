# Clase abstracta de Persona para después
# definir las clases de Cliente y Administrador,
# con la posibilidad de integrar otra clase heredera de Persona en un futuro.

from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__ (self, rut,
                  nombre,
                  apellido_paterno,
                  apellido_materno,
                  email,
                  contraseña_hash,
                  telefono,
                  direccion,
                  fecha_nacimiento,
                  fecha_registro):
        
        self.rut = rut
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.email = email
        self.contraseña_hash = contraseña_hash
        self.telefono = telefono
        self.direccion = direccion
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_registro = fecha_registro

    @abstractmethod
    def iniciar_sesion(self):
        pass
    
    @abstractmethod
    def validar_rut(self):
        pass
