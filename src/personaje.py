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
    