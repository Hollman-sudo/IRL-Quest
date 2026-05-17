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