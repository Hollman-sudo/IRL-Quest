# IRL Quest - Sistema de hábitos con mecánicas RPG
# Copyright (C) 2026  Hollman 

# Este programa es software libre: puedes redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General de GNU publicada por
# la Free Software Foundation, ya sea la versión 3 de la Licencia, o
# (a tu elección) cualquier versión posterior.

# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; sin siquiera la garantía implícita de
# COMERCIABILIDAD o IDONEIDAD PARA UN PROPÓSITO PARTICULAR. Véase la
# Licencia Pública General de GNU para más detalles.

# Deberías haber recibido una copia de la Licencia Pública General de GNU
# junto con este programa. Si no, consulta <https://www.gnu.org/licenses/>.



# src/utils.py
# Módulo para guardar y cargar partida en formato JSON

import json
import os

def guardar_partida(personaje, misiones_diarias, misiones_principales):
    """
    Guardo el estado actual de la partida en data/savegame.json.
    Recibo el personaje (dict), las listas de misiones diarias y principales.
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
    Cargo la partida desde data/savegame.json si existe.
    Devuelvo una tupla (personaje, misiones_diarias, misiones_principales).
    Si no hay archivo o hay error, devuelvo (None, [], []) para que main.py cree un personaje nuevo.
    """
    try:
        # 1. Verifico si el archivo existe
        if not os.path.exists("data/savegame.json"):
            print("No se encontró partida guardada. Crearás un personaje nuevo.")
            return None, [], []
        
        # 2. Abro el archivo y leo los datos
        with open("data/savegame.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        
        # 3. Extraigo cada parte (si falta alguna clave, uso valores por defecto)
        personaje = datos.get("personaje", None)
        misiones_diarias = datos.get("misiones_diarias", [])
        misiones_principales = datos.get("misiones_principales", [])
        
        # Si el archivo contenía personaje None (raro), también devolvemos None
        if personaje is None:
            print("El archivo de guardado no contiene un personaje válido. Se creará uno nuevo.")
            return None, [], []
        
        print("Partida cargada exitosamente.")
        return personaje, misiones_diarias, misiones_principales
    except FileNotFoundError:
        print("Archivo de guardado no encontrado. Crearás un personaje nuevo.")
        return None, [], []
    except json.JSONDecodeError:
        print("Error: el archivo de guardado está corrupto. Se iniciará una partida nueva.")
        return None, [], []
    except Exception as e:
        print(f"Error inesperado al cargar la partida: {e}")
        return None, [], []