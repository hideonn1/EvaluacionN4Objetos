##archivo encargado de consultas sql con la tabla reserva

from src.Logica_de_Negocio.models.Reserva import Reserva

class Reservas_Repository:
    
    def __init__(self, conectar_db):
        self._conectar_db = conectar_db

    # Crea un nuevo registro de reserva en la base de datos
    def create(self, reserva, id_usuario):
        conexion = self._conectar_db()
        cursor = conexion.cursor()
        
        try:
            query = ("""
                    INSERT INTO reserva (fecha_inicio, fecha_final, estado, monto_total, id_usuario) 
                    VALUES (%s, %s, %s, %s, %s);
                """)
            datos = (reserva.fecha_inicio, 
                    reserva.fecha_final,
                    reserva.estado,
                    reserva.monto_total,
                    id_usuario
                    )
            cursor.execute(query, datos)
            conexion.commit() 

            reserva_id = cursor.lastrowid
            reserva.id_reserva = reserva_id

            return reserva
            
        except Exception as e:
            conexion.rollback()
            raise e
            
        finally:
            cursor.close()
            conexion.close()        
        
    
    # Retorna una reserva
    def read_by_id(self, id_reserva):
        conexion = self._conectar_db() 
        cursor = conexion.cursor(dictionary=True)

        try:
            query = "SELECT * FROM reserva WHERE id_reserva = %s"
            datos = (id_reserva,)

            cursor.execute(query,datos)
            resultado = cursor.fetchone()

            if resultado:
                reserva_objeto = Reserva(
                    id_reserva = resultado['id_reserva'],
                    id_usuario = resultado['id_usuario'],

                    fecha_inicio = resultado['fecha_inicio'],
                    fecha_final = resultado['fecha_final'],
                    estado = resultado['estado'],
                    monto_total = resultado['monto_total']
                )
                return reserva_objeto
            else:
                return None 

        finally:
            cursor.close()
            conexion.close() 

    # Actualiza los datos de un usuario ya existente.
    def update(self, reserva):
        conexion = self._conectar_db()
        cursor = conexion.cursor()
        
        try:
            query = ("""
                UPDATE reserva SET 
                    estado = %s, 
                    monto_total = %s
                WHERE id_reserva = %s;
                """)
            datos = (reserva.estado, 
                    reserva.monto_total,
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
            return cursor.rowcount > 0
            
        except Exception as e:
            conexion.rollback()
            raise e
            
        finally:
            cursor.close()
            conexion.close()

