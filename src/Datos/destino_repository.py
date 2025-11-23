##archivo encargado de consultas sql con la tabla destino
from src.Logica_de_Negocio.models.Destino import Destino

class Destino_Repository:
    
    def __init__(self, conectar_db):
        self._conectar_db = conectar_db

    def create(self, destino):
        conexion = self._conectar_db()
        cursor = conexion.cursor()
        
        try:
            query = ("""
                    INSERT INTO destino (nombre, ciudad, pais, descripcion, actividades_disponibles, costo) 
                    VALUES (%s, %s, %s, %s, %s, %s);
                """)
            datos = (destino.nombre,
                     destino.ciudad,
                     destino.pais,
                     destino.descripcion,
                     destino.actividades_disponibles,
                     destino.costo
                    )
            cursor.execute(query, datos)
            conexion.commit() 

            return destino
            
        except Exception as e:
            conexion.rollback()
            raise e
            
        finally:
            cursor.close()
            conexion.close()        
        
    
    # Busca y retorna un Usuario por su ID
    def read_by_id(self, id_destino):
        conexion = self._conectar_db() 
        cursor = conexion.cursor(dictionary=True)

        try:
            query = "SELECT * FROM destino WHERE id_destino = %s"
            datos = (id_destino,)

            cursor.execute(query,datos)
            resultado = cursor.fetchone()

            if resultado:
                destino_objeto = Destino(
                    id_destino = resultado['id_destino'],
                    nombre = resultado['nombre'],
                    ciudad = resultado['ciudad'],
                    pais = resultado['pais'],
                    descripcion = resultado['costo'],
                    actividades_disponibles = resultado['actividades_disponibles'],
                    costo = resultado['costo']
                )
                return destino_objeto 
            else:
                return None 

        finally:
            cursor.close()
            conexion.close() 

    def read_by_name(self, nombre):
        conexion = self._conectar_db() 
        cursor = conexion.cursor(dictionary=True)
        try:
            query = "SELECT * FROM destino WHERE nombre = %s"
            datos = (nombre,)

            cursor.execute(query,datos)
            resultado = cursor.fetchone()

            if resultado:
                destino_objeto = Destino(
                    id_destino = resultado['id_destino'],
                    nombre = resultado['nombre'],
                    ciudad = resultado['ciudad'],
                    pais = resultado['pais'],
                    descripcion = resultado['costo'],
                    actividades_disponibles = resultado['actividades_disponibles'],
                    costo = resultado['costo']
                )
                return destino_objeto 
            else:
                return None 

        finally:
            cursor.close()
            conexion.close() 


    def update(self, destino):
        conexion = self._conectar_db()
        cursor = conexion.cursor()
        
        try:
            query = ("""
                UPDATE destino SET 
                    nombre = %s,
                    ciudad = %s,
                    pais = %s,
                    descripcion = %s,
                    actividades_disponibles = %s,
                    costo = %s
                WHERE id_destino = %s;
                """)
            datos = (destino.nombre,
                    destino.ciudad,
                    destino.pais,
                    destino.descripcion,
                    destino.actividades_disponibles,
                    destino.costo,
                    destino.id_destino
                    )
            cursor.execute(query, datos)
            conexion.commit() 
            return destino
            
        except Exception as e:
            conexion.rollback()
            raise e
            
        finally:
            cursor.close()
            conexion.close()


    def delete(self, id_destino):
        conexion = self._conectar_db()
        cursor = conexion.cursor()
        
        try:
            query = ("DELETE FROM destino WHERE id_destino = %s;")
            datos = (id_destino,)
            cursor.execute(query, datos)
            conexion.commit() 
            return True 
            
        except Exception as e:
            conexion.rollback()
            raise e
            
        finally:
            cursor.close()
            conexion.close()
