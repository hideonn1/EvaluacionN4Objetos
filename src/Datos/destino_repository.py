##archivo encargado de consultas sql con la tabla destino
from src.Logica_de_Negocio.models.Destino import Destino

class Usuario_Repository:
    
    def __init__(self, conectar_db):
        self._conectar_db = conectar_db




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
