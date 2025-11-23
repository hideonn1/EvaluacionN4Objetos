##archivo encargado de consultas sql con la tabla paquete_turistico
from src.Logica_de_Negocio.models.PaqueteTuristico import PaqueteTuristico

class Paquete_Repository:
    
    def __init__(self, conectar_db):
        self._conectar_db = conectar_db

    def create(self, paquete):
        conexion = self._conectar_db()
        cursor = conexion.cursor()
        
        try:
            query = ("""-
                    INSERT INTO paquete_turistico (fecha_llegada, fecha_salida, orden_visita, costo_destino) 
                    VALUES (%s, %s, %s, %s);
                """)
            datos = (paquete.fecha_llegada,
                     paquete.fecha_salida,
                     paquete.orden_visita,
                     paquete.costo_destino
                    )
            cursor.execute(query, datos)
            conexion.commit() 

            return paquete
            
        except Exception as e:
            conexion.rollback()
            raise e
            
        finally:
            cursor.close()
            conexion.close()        
        
    def read_by_id(self, id_paquete):
        conexion = self._conectar_db() 
        cursor = conexion.cursor(dictionary=True)

        try:
            query = "SELECT * FROM paquete_turistico WHERE id_paquete_turistico = %s"
            datos = (id_paquete,)

            cursor.execute(query,datos)
            resultado = cursor.fetchone()

            if resultado:
                paquete_objeto = PaqueteTuristico(
                    id_paquete = resultado['id_paquete_turistico'],
                    fecha_llegada = resultado['fecha_llegada'],
                    fecha_salida = resultado['fecha_salida'],
                    orden_visita = resultado['orden_visita'],
                    costo_destino = resultado['costo_destino']
                )
                return paquete_objeto
            else:
                return None 

        finally:
            cursor.close()
            conexion.close() 



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

