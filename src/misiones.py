# Función para crear misiones diarias
def crear_mision_diaria(nombre, estadistica, puntos_estadistica, oro):
    return {
        "Nombre:" : nombre,
        "Estadistica:" : estadistica,
        "Puntos de Estadistica:" : puntos_estadistica,
        "Oro:" : oro,
        "Completado:" : False,
    }
        
    