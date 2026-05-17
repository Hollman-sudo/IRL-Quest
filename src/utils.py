# Importe las librerias para guardar datos
import json
import os

from personaje import crear_personaje  # Para crear personaje nuevo si no hay uno guardado

def guardar_partida(personaje, misiones_diarias, misiones_principales):
    """
    Guardo el estado actual de la partida.
    Recibo el personaje, las listas de misiones diarias y principales.
    Devuelvo True si se guardó correctamente, False si hubo error.
    """
    try:
        # 1. Me aseguro de que la carpeta data exista
        os.makedirs("data", exist_ok=True)
        
        # 2. Preparo un diccionario con todo lo que quiero guardar
        datos = {
            "personaje": personaje,
            "misiones_diarias": misiones_diarias,
            "misiones_principales": misiones_principales
        }
        
        # 3. Abro el archivo en modo escritura y guardo los datos con formato legible
        with open("data/savegame.json", "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
        
        print("Partida guardada exitosamente.")
        return True
    except Exception as e:
        print(f"Error al guardar la partida: {e}")
        return False

def cargar_partida():
    """
    Cargo la partida..
    Devuelvo una tupla (personaje, misiones_diarias, misiones_principales).
    Si no hay archivo o hay error, devuelvo valores por defecto (personaje nuevo, listas vacías).
    """
    try:
        # 1. Verifico si el archivo existe
        if not os.path.exists("data/savegame.json"):
            print("No se encontró partida guardada. Se creará un personaje nuevo.")
            return crear_personaje("Aventurero"), [], []
        
        # 2. Abro el archivo y leo los datos
        with open("data/savegame.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        
        # 3. Extraigo cada parte
        personaje = datos.get("personaje", crear_personaje("Aventurero"))
        misiones_diarias = datos.get("misiones_diarias", [])
        misiones_principales = datos.get("misiones_principales", [])
        
        print("Partida cargada exitosamente.")
        return personaje, misiones_diarias, misiones_principales
    except FileNotFoundError:
        print("Archivo de guardado no encontrado. Comenzando partida nueva.")
        return crear_personaje("Aventurero"), [], []
    except json.JSONDecodeError:
        print("Error: el archivo de guardado está corrupto. Se inicia partida nueva.")
        return crear_personaje("Aventurero"), [], []
    except Exception as e:
        print(f"Error inesperado al cargar la partida: {e}")
        return crear_personaje("Aventurero"), [], []