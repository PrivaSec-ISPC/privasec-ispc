import os
import json

PUERTAS = os.path.join(os.path.dirname(__file__), "puertas.json")


# cargar puertas
def cargar_puertas():
    if os.path.exists(PUERTAS):
        try:
            with open(PUERTAS, "r", encoding="utf-8") as archivo:
                return json.load(archivo)  # pasar de json a diccionario
        except (json.JSONDecodeError, TypeError) as error:
            print(f"Error al cargar los puertas: {error}")
    return []


# guardar puertas
def guardar_puertas(puertas):
    try:
        with open(PUERTAS, "w", encoding="utf-8") as archivo:
            json.dump(puertas, archivo, indent=2)  # pasar de diccionario a json
    except (json.JSONDecodeError, TypeError) as error:
        print(f"Error al cargar las puertas: {error}")
