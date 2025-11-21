from src.models.Cliente import Cliente

class Usuario_Repository:
    
    def __init__(self, conectar_db):
        self._conectar_db = conectar_db

    # Crea un nuevo registro de usuario en la base de datos
    def add(self, usuario):
        pass
    
    # Busca y retorna un Usuario por su ID
    def get_by_id(self, id_usuario):
        conexion = self._conectar_db() 
        cursor = conexion.cursor(dictionary=True)

        try:
            query = "SELECT * FROM Usuario WHERE id_usuario = %s"
            datos = (id_usuario,)

            cursor.execute(query,datos)
            resultado = cursor.fetchone()

            if resultado:
                usuario_objeto = Cliente(
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
                usuario_objeto = Cliente(
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
    def update(self, usuario):
        # Lógica SQL: UPDATE Usuario SET ... WHERE id_usuario = :id_usuario
        pass

    # Elimina un registro de usuario
    def delete(self, id_usuario):
        # Lógica SQL: DELETE FROM Usuario WHERE id_usuario = :id_usuario
        pass
