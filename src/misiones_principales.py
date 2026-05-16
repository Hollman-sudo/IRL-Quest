# Función para crear misiones principales
def crear_mision_principal(nombre, estadistica, puntos_estadistica, oro, dias_limites):
    return {
        "Nombre:" : nombre,
        "Estadistica:" : estadistica,
        "Puntos de Estadistica:" : puntos_estadistica,
        "Oro:" : oro,
        "Dias Restantes:" : dias_limites,
        "Completado:" : False
    }