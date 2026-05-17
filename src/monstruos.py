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



# src/monstruos.py
# Cree una matriz con varios monstruos para la aplicación
monstruos = [
    {
        "nombre": "Goblin",
        "rango": "Normal",
        "vida_max": 30,
        "ataque_monstruo": 5,
        "condicion": "hacer 10 flexiones",
        "golpe_usuario": 10,
        "recompensa_oro": 15,
        "recompensa_estadistica": "Fuerza:",
        "recompensa_puntos": 5
    },
    {
        "nombre": "Orco",
        "rango": "Común",
        "vida_max": 50,
        "ataque_monstruo": 8,
        "condicion": "hacer 20 sentadillas",
        "golpe_usuario": 15,
        "recompensa_oro": 25,
        "recompensa_estadistica": "Fuerza:",
        "recompensa_puntos": 8
    },
    {
        "nombre": "Troll de Montaña",
        "rango": "Raro",
        "vida_max": 80,
        "ataque_monstruo": 12,
        "condicion": "hacer 10 lagartijas con una mano",
        "golpe_usuario": 20,
        "recompensa_oro": 40,
        "recompensa_estadistica": "Fuerza:",
        "recompensa_puntos": 12
    }
]