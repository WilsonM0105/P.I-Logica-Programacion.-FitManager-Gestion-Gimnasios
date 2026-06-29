import json
import os

RUTA_CLIENTES = "datos/clientes.json"
RUTA_PAGOS = "datos/pagos.json"

def crear_archivos_si_no_existen():
    if not os.path.exists("datos"):
        os.makedirs("datos")

    if not os.path.exists(RUTA_CLIENTES):
        guardar_datos(RUTA_CLIENTES, [])

    if not os.path.exists(RUTA_PAGOS):
        guardar_datos(RUTA_PAGOS, [])

def cargar_datos(ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except:
        return []

def guardar_datos(ruta, datos):
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

def cargar_clientes():
    return cargar_datos(RUTA_CLIENTES)

def guardar_clientes(clientes):
    guardar_datos(RUTA_CLIENTES, clientes)

def cargar_pagos():
    return cargar_datos(RUTA_PAGOS)

def guardar_pagos(pagos):
    guardar_datos(RUTA_PAGOS, pagos)