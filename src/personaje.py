# Función para crear personaje:
def crear_personaje(nombre):
    return {
        "Nombre:": nombre,
        "Vida:": 100,
        "Vivo:": True,
        "Rango:": "F",
        "Oro:": 0,
        "Fuerza:": 0,
        "Velocidad:": 0,                 
        "Defensa:": 0,                     
        "Apariencia:": 0,
        "Estamina:": 0,                   
        "Carisma:": 0,
        "Agilidad:": 0,
        "Inteligencia:": 0,
        "Flexibilidad:": 0,
        "Determinación:": 0,
        "Reflejos:": 0
    }
    
# Función que da puntos de estadistica despues de completar una misión:
def completar_mision(personaje,estadistica,puntos):
    personaje[estadistica] = personaje[estadistica] + puntos
    actualizar_rango(personaje)
    return personaje

# Función para ganar oro
def ganar_oro(personaje, cantidad):
    personaje["Oro:"] = personaje["Oro:"] + cantidad
    return personaje

# Función para quitarle vida al personaje:
def perder_vida(personaje,perdida):
    personaje["Vida:"] = personaje["Vida:"] - perdida
    if personaje["Vida:"] <= 0:
        personaje["Vivo"] = False
    return personaje

# Función para mostrar el personaje:
def mostrar_personaje(personaje):
    for clave, valor in personaje.items():
        print(f"{clave:15} : {valor}")
        
# Función para calcular el rango del personaje
def actualizar_rango(personaje):
    """
    Calcula el rango del personaje según la suma total de sus estadísticas.
    Actualiza la clave "Rango:" en el diccionario del personaje.
    """
    # Lista de todas las estadísticas que se suman (excluyendo Vida, Oro, Vivo, etc.)
    estadisticas = [
        "Fuerza:", "Velocidad:", "Defensa:", "Apariencia:", "Estamina:",
        "Carisma:", "Agilidad:", "Inteligencia:", "Flexibilidad:",
        "Determinación:", "Reflejos:"
    ]
    
    # Sumar todos los valores
    total = 0
    for stat in estadisticas:
        total += personaje.get(stat, 0)  # get() por si falta alguna clave
    
    # Determinar rango según el total
    if total <= 20:
        rango = "F"
    elif total <= 40:
        rango = "E"
    elif total <= 60:
        rango = "D"
    elif total <= 80:
        rango = "C"
    elif total <= 100:
        rango = "B"
    elif total <= 120:
        rango = "A"
    else:
        rango = "S"
    
    # Actualizar el rango en el personaje
    personaje["Rango:"] = rango
    