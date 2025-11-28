##archivo encargado de consultas sql con la tabla paquete_turistico
from src.Logica_de_Negocio.models.PaqueteTuristico import PaqueteTuristico

class Paquete_Repository:
    
    def __init__(self, conectar_db):
        self._conectar_db = conectar_db

    def create(self, paquete):
        conexion = self._conectar_db()
        cursor = conexion.cursor()
        
        try:
            query = ("""
                    INSERT INTO paquete_turistico (costo_destino) 
                    VALUES (%s);
                """)
            datos = (paquete.costo_destino,
                    )
            cursor.execute(query, datos)
            conexion.commit() 

            paquete_id = cursor.lastrowid
            paquete.id_paquete = paquete_id

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
            return cursor.rowcount > 0
            
        except Exception as e:
            conexion.rollback()
            raise e
            
        finally:
            cursor.close()
            conexion.close()

    def destino_x_paquete(self, paquete, destino):
        conexion = self._conectar_db()
        cursor = conexion.cursor()
        
        try:
            query = ("""
                    INSERT INTO destino_has_paquete_turistico (destino_id_destino, paquete_turistico_id_paquete_turistico, fecha_llegada, fecha_salida, orden_visita) 
                    VALUES (%s, %s, %s, %s, %s);
                """)
            datos = (destino.id_destino,
                    paquete.id_paquete,
                    destino.fecha_llegada,
                    destino.fecha_salida,
                    destino.orden_visita
                    )
            print(paquete.id_paquete)
            cursor.execute(query, datos)
            conexion.commit() 
            
        except Exception as e:
            conexion.rollback()
            raise e
            
        finally:
            cursor.close()
            conexion.close()     

    def duplicidad_destino(self, destino_id, paquete_id):

        conexion = self._conectar_db()
        cursor = conexion.cursor()
        
        try:
            # 1. Consulta SQL: Busca si existe al menos una fila con ambos IDs
            query = """
                SELECT 1 FROM destino_has_paquete_turistico 
                WHERE destino_id_destino = %s 
                AND paquete_turistico_id_paquete_turistico = %s 
                LIMIT 1;
            """
            datos = (destino_id, paquete_id)
            
            cursor.execute(query, datos)
            
            resultado = cursor.fetchone()
            
            # 3. Retorno Booleano
            return resultado is not None 

        except Exception as e:
            # En caso de error de DB, lanzamos una excepción
            raise e
            
        finally:
            cursor.close()
            conexion.close()