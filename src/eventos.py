# Funció para crear eventos aleatorios
def crear_evento(nombre, rango, vida, condicion, golpe):
    return {
        "Nombre:" : nombre,
        "Rango:" : rango,
        "Vida:" : vida,
        "Condición Para Vencerlo:" : condicion,
        "Luchar:" : golpe
    }