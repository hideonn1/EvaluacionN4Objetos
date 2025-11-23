import json
import os
from datetime import datetime, timedelta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_DIR = os.path.join(BASE_DIR, "..", "docs")
os.makedirs(DOCS_DIR, exist_ok=True)

ruta_bloqueo = os.path.join(DOCS_DIR, "bloqueos.json")

max_intentos = 4
tiempo_bloqueo_min = 5


def cargar_estado():
    if not os.path.exists(ruta_bloqueo):
        return {"intentos_fallidos_totales": 0, "bloqueado_hasta": None}
    with open(ruta_bloqueo, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_estado(data):
    with open(ruta_bloqueo, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def esta_bloqueado():
    estado = cargar_estado()
    if estado["bloqueado_hasta"]:
        hasta = datetime.fromisoformat(estado["bloqueado_hasta"])
        if datetime.now() < hasta:
            return True
        else:
            estado["bloqueado_hasta"] = None
            estado["intentos_fallidos_totales"] = 0
            guardar_estado(estado)
    return False

def registrar_intento(exito):
    estado = cargar_estado()
    if exito:
        estado["intentos_fallidos_totales"] = 0
        estado["bloqueado_hasta"] = None
    else:
        estado["intentos_fallidos_totales"] += 1
        if estado["intentos_fallidos_totales"] >= max_intentos:
            estado["bloqueado_hasta"] = (datetime.now() + timedelta(minutes=tiempo_bloqueo_min)).isoformat()
            print(f"Sistema bloqueado por {tiempo_bloqueo_min} minutos debido a múltiples intentos fallidos.")
    guardar_estado(estado)