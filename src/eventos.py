import random
from monstruos import monstruos

def seleccionar_monstruo_aleatorio():
    #Devuelve un monstruo aleatorio de la lista predefinida.
    return random.choice(monstruos)