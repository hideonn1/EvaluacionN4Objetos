##archivo encargado de consultas sql con la tabla paquete_turistico
from src.Logica_de_Negocio.models.PaqueteTuristico import PaqueteTuristico

class Usuario_Repository:
    
    def __init__(self, conectar_db):
        self._conectar_db = conectar_db


    def update(self, paquete_turistico):
        conexion = self._conectar_db()
        cursor = conexion.cursor()
        
        try:
            query = ("""
                UPDATE paquete_turistico SET 
                    fecha_llegada = %s,
                    fecha_salida = %s,
                    orden_visita = %s,
                    costo_destino = %s
                WHERE id_paquete_turistico = %s;
                """)
            datos = (paquete_turistico.fecha_llegada,
                    paquete_turistico.fecha_salida,
                    paquete_turistico.orden_visita,
                    paquete_turistico.costo_destino,
                    paquete_turistico.id_paquete_turistico
                    )
            cursor.execute(query, datos)
            conexion.commit() 
            return paquete_turistico
            
        except Exception as e:
            conexion.rollback()
            raise e
            
        finally:
            cursor.close()
            conexion.close()


    def delete(self, id_paquete_turistico):
        conexion = self._conectar_db()
        cursor = conexion.cursor()
        
        try:
            query = ("DELETE FROM paquete_turistico WHERE id_paquete_turistico = %s;")
            datos = (id_paquete_turistico,)
            cursor.execute(query, datos)
            conexion.commit() 
            return True 
            
        except Exception as e:
            conexion.rollback()
            raise e
            
        finally:
            cursor.close()
            conexion.close()

