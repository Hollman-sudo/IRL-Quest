# IRL Quest - Sistema de hábitos con mecánicas RPG
# Copyright (C) 2026  Hollman (o tu nombre real)

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

import random
from monstruos import monstruos

def seleccionar_monstruo_aleatorio():
    #Devuelve un monstruo aleatorio de la lista predefinida.
    return random.choice(monstruos)