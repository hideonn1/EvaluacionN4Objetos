## archivo encargado de logica y comunicar a paquete_turistico_controller con paquete_turistico_repository
from .models.PaqueteTuristico import PaqueteTuristico
from datetime import datetime

class Paquete_Service:
    
    def __init__(self, usuario_repository):
        # Recibe el Repositorio por inyección. No sabe nada de conexiones.
        self._repo = usuario_repository 

    def buscar_paquete(self, paquete_id):




        destino_santiago = {
            'id_destino': 101,
            'nombre': 'Santiago Urbano',
            'actividades_disponibles':'Nada',
            'ciudad':'Santiago',
            'pais':'Chile',
            'costo': 250000,
            'descripcion': 'Capital moderna de Chile con parques y museos.'
        }

        destino_valparaiso = {
            'id_destino': 102,
            'nombre': 'Valparaíso Histórico',
            'actividades_disponibles':'Mear en la calle',
            'ciudad':'Valparaiso',
            'pais':'Chile',
            'costo': 150000,
            'descripcion': 'Puerto de murales y ascensores con vista al mar.'
        }

        paquete_ejemplo = PaqueteTuristico(
            id_paquete=55,
            # Asumimos que los atributos de la clase principal son necesarios para el constructor
            fecha_llegada=datetime(2025, 12, 10),
            fecha_salida=datetime(2025, 12, 16),
            orden_visita=1, # Si es un segmento, esta es la posición
            costo_destino=400000, # El costo de este segmento
            
            # Lista de objetos Destino anidados (esto es lo que el Service ensambla)
            destinos=[
                destino_santiago,
                destino_valparaiso
            ]
        )

        return paquete_ejemplo