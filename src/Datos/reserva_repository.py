##archivo encargado de consultas sql con la tabla reserva

from src.Logica_de_Negocio.models.Reserva import Reserva

class Usuario_Repository:
    
    def __init__(self, conectar_db):
        self._conectar_db = conectar_db

    # Crea un nuevo registro de usuario en la base de datos
    def add(self, reserva):
        pass
    
    # Busca y retorna un Usuario por su ID
    def get_by_id(self, id_reserva):
        conexion = self._conectar_db() 
        cursor = conexion.cursor(dictionary=True)

        try:
            query = "SELECT * FROM Usuario WHERE id_usuario = %s"
            datos = (id_reserva,)

            cursor.execute(query,datos)
            resultado = cursor.fetchone()

            if resultado:
                usuario_objeto = Reserva(
                    id_cliente = resultado['id_usuario'],
                    rut = resultado['rut'],
                    nombres = resultado['nombres'],
                    apellido_paterno = resultado['apellido_paterno'],
                    apellido_materno = resultado['apellido_materno'],
                    email = resultado['email'],
                    contraseña_hash = ['contraseña'],
                    telefono = resultado['telefono'],
                    direccion = resultado['direccion'],
                    fecha_nacimiento = resultado['fecha_nacimiento'],
                    fecha_registro = resultado['fecha_registro']
                )
                return usuario_objeto 
            else:
                return None 

        finally:
            pass 

    # Busca y retorna un Usuario por su email
    def get_by_email(self, email):
        conexion = self._conectar_db() 
        cursor = conexion.cursor(dictionary=True)

        try:
            query = "SELECT * FROM Usuario WHERE email = %s"
            datos = (email,)

            cursor.execute(query,datos)
            resultado = cursor.fetchone()

            if resultado:
                usuario_objeto = Reserva(
                    id_cliente = resultado['id_usuario'],
                    rut = resultado['rut'],
                    nombres = resultado['nombres'],
                    apellido_paterno = resultado['apellido_paterno'],
                    apellido_materno = resultado['apellido_materno'],
                    email = resultado['email'],
                    contraseña_hash = ['contraseña'],
                    telefono = resultado['telefono'],
                    direccion = resultado['direccion'],
                    fecha_nacimiento = resultado['fecha_nacimiento'],
                    fecha_registro = resultado['fecha_registro']
                )
                return usuario_objeto 
            else:
                return None 

        finally:
            pass 
    # Actualiza los datos de un usuario ya existente.
    def update(self, reserva):
        conexion = self._conectar_db()
        cursor = conexion.cursor()
        
        try:
            query = ("""
                UPDATE reserva SET 
                    estado = %s, 
                    monto_pagado = %s
                WHERE id_reserva = %s;
                """)
            datos = (reserva.estado, 
                    reserva.monto_pagado,
                    reserva.id_reserva
                    )
            cursor.execute(query, datos)
            conexion.commit() 
            return reserva
            
        except Exception as e:
            conexion.rollback()
            raise e
            
        finally:
            cursor.close()
            conexion.close()

    def delete(self, id_reserva):
        conexion = self._conectar_db()
        cursor = conexion.cursor()
        
        try:
            query = ("DELETE FROM reserva WHERE id_reserva = %s;")
            datos = (id_reserva,)
            cursor.execute(query, datos)
            conexion.commit() 
            return True 
            
        except Exception as e:
            conexion.rollback()
            raise e
            
        finally:
            cursor.close()
            conexion.close()

