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




# Importo las funciones de las demas features
from personaje import mostrar_personaje, completar_mision, ganar_oro, perder_vida, crear_personaje
from misiones import crear_mision_diaria
from misiones_principales import crear_mision_principal
from eventos import seleccionar_monstruo_aleatorio
from utils import cargar_partida, guardar_partida

def main():
    print("IRL Quest Copyright (C) 2026 [Tu Nombre]")
    print("Este programa viene SIN GARANTÍA ALGUNA; para más detalles, escribe 'show w'.")
    print("Este es software libre y eres libre de redistribuirlo bajo ciertas condiciones; escribe 'show c' para más detalles.\n")
    # Cargar partida al iniciar
    personaje, misiones_diarias, misiones_principales = cargar_partida()

    # Si no hay partida guardada, crear personaje nuevo
    if personaje is None:
        nombre = input("¡Bienvenido! ¿Cómo se llama tu aventurero? ")
        personaje = crear_personaje(nombre)
        print(f"¡{nombre} ha sido creado! Comienza tu aventura.")

    # Si el personaje está muerto, no se puede continuar
    if not personaje["Vivo:"]:
        print("Tu personaje está muerto. No se puede continuar.")
        return

    # Menú para que el usuario interactue con la app   
    ejecutando = True
    while ejecutando:
        print("\n" + "="*50)
        print("            MENÚ PRINCIPAL")
        print("="*50)
        print("[1] Ver personaje")
        print("[2] Misiones diarias")
        print("[3] Misiones principales")
        print("[4] Eventos aleatorios")
        print("[5] Guardar partida")
        print("[6] Nuevo día")
        print("[7] Salir")
        
        # Verificamos si la opción es un número o no
        try:
            opcion = int(input("\nElige una opción: "))
        except ValueError:
            print("ERROR: Ingresa un número válido.")
            continue
        
# BLOQUE DE CÓDIGO PARA LOS DIFERENTES MENÚS
####################################################################################################    
        # Si elige 1 en el menú principal, mostramos el personaje
        if opcion == 1:
            mostrar_personaje(personaje)  
####################################################################################################

        # Si elige 2 en el menú principal, mostramos el menu de opciones de las misiones diarias   
        elif opcion == 2:
            en_misiones = True
            while en_misiones:
                print("\n" + "="*50)
                print("            MENÚ MISIONES DIARIAS")
                print("="*50) 
                print("[1] Crear Misión.")
                print("[2] Mostrar Misiones sin Terminar.")
                print("[3] Completar Misión.")
                print("[4] Volver al menú principal.")
                   
                try:
                    eleccion = int(input("\nDigite su elección: "))
                except ValueError:
                    print("ERROR: Ingrese un número válido.")
                    continue
                #Si el usuario digita 1, le pedimos la información para crear la misión      
                if eleccion == 1:
                    nombre = input("Digite el nombre de la misión: ")
                    estadistica = input("Digite el nombre de la estadistica que va a ganar puntos: ")
                    # Agregar dos puntos si no los tiene
                    if not estadistica.endswith(":"):
                        estadistica += ":"
                    puntos_estadistica = 5
                    oro = 3
                    
                    # Creo una variable para meter la información en la función
                    mision = crear_mision_diaria(nombre, estadistica, puntos_estadistica, oro)
                    # Agregamos la mision diaria
                    misiones_diarias.append(mision)
                    
                    print("!Misión creada con exito!")
                # Si el usuario digita 2,  le mostramos todas las misiones diarias que no han sido completadas
                elif eleccion == 2:
                    
                    if not misiones_diarias:
                        print("No tiene misiones pendientes.")
                    else:
                        for i, m in enumerate(misiones_diarias):
                            if not m["Completado:"]:
                               print(f"{i} - {m['Nombre:']} | {m['Estadistica:']} + {m['Puntos de Estadistica:']} | Oro: {m['Oro:']}")   
                            else:
                                print(f"{i} - {m['Nombre:']} | (COMPLETADA HOY)")
                            
                elif eleccion == 3:
                    if not misiones_diarias:
                        print("No hay misiones por completar")
                        continue
                    for i, m in enumerate(misiones_diarias):
                        print(f"{i} - {m['Nombre:']}")
                        
                    try:
                        indiceMision = int(input("Ingrese el indice de la misión a completar: "))
                        
                        if 0 <= indiceMision < len(misiones_diarias):
                            mision = misiones_diarias[indiceMision]
                            # Le damos las recompensas al personaje
                            completar_mision(personaje, mision['Estadistica:'], mision['Puntos de Estadistica:'])
                            mision['Completado:'] = True
                            ganar_oro(personaje, mision["Oro:"])
                            
                            print("!Misión completada con exito!")
                        else:
                            print("Índice no válido.")
                    except ValueError:
                        print("ERROR: Debe ingresar un número.")
                    
                elif eleccion == 4:
                    en_misiones = False
                else:
                    print("ERROR: Opción no válida, intente de nuevo.")
                        
                        
####################################################################################################                   
        # Si el usuario elige la opción 3 del menú principal, le mostramos el menú de misiones principales           
        elif opcion == 3:
            en_misiones = True
            while en_misiones:
                print("\n" + "="*50)
                print("            MENÚ MISIONES PRINCIPALES")
                print("="*50) 
                print("[1] Crear Misión.")
                print("[2] Mostrar Misiones sin Terminar.")
                print("[3] Completar Misión.")
                print("[4] Volver al menú principal.")
                try:
                    eleccion = int(input("\nDigite su elección: "))
                except ValueError:
                    print("ERROR: Ingrese un número válido.")
                    continue
                #Si el usuario digita 1, le pedimos la información para crear la misión      
                if eleccion == 1:
                    nombre = input("Digite el nombre de la misión: ")
                    estadistica = input("Digite el nombre de la estadistica que va a ganar puntos: ")
                    if not estadistica.endswith(":"):
                        estadistica += ":"
                    puntos_estadistica = 20
                    oro = 15
                    dias_limites = int(input("Por favor digite el número de días que va a durar la misión: "))
                    
                    mision = crear_mision_principal(nombre, estadistica, puntos_estadistica, oro, dias_limites)
                    misiones_principales.append(mision)
                    print("!Misión creada con exito!")
                    
                elif eleccion == 2:
                    if not misiones_principales:
                        print("No tiene misiones pendientes.")
                    else:
                        for i, m in enumerate(misiones_principales):
                            if not m["Completado:"]:
                                print(f"{i} - {m['Nombre:']} | {m['Estadistica:']} + {m['Puntos de Estadistica:']} | Oro: {m['Oro:']} | Tiempo Restante: {m['Dias restantes:']}")   
                            else:
                                print(f"{i} - {m['Nombre:']} | (COMPLETADA HOY)")
                            
                elif eleccion == 3:
                    if not misiones_principales:
                        print("No hay misiones para completar.")
                        continue
                    for i, m in enumerate(misiones_principales):
                        print(f"{i} - {m['Nombre:']}")
                    try:
                        indiceMision = int(input("Número de misión a completar: "))
                        if 0 <= indiceMision < len(misiones_principales):
                            mision = misiones_principales[indiceMision]
                            completar_mision(personaje, mision['Estadistica:'], mision['Puntos de Estadistica:'])
                            ganar_oro(personaje, mision['Oro:'])
                            del misiones_principales[indiceMision]
                            print("¡Misión completada!")
                        else:
                            print("Índice no válido.")
                    except ValueError:
                        print("Debe ingresar un número.")
                    
                elif eleccion == 4:
                    en_misiones = False
                else:
                    print("ERROR: Opción no válida, intente de nuevo.")
                        
                
####################################################################################################       
        elif opcion == 4:
            monstruo = seleccionar_monstruo_aleatorio()
            print(f"\n¡Ha aparecido un {monstruo['nombre']} (Rango {monstruo['rango']})!")
            print(f"Vida del monstruo: {monstruo['vida_max']}")
            print(f"Condición para golpear: {monstruo['condicion']}")
            print("Escribe '1' para luchar (cumplir la condición), '2' para huir.\n")
            
            vida_monstruo = monstruo['vida_max']
            en_combate = True
            
            while en_combate and personaje["Vivo:"]:
                print(f"\nTu vida: {personaje['Vida:']} | Vida monstruo: {vida_monstruo}")
                accion = input("¿[1]Luchar / [2]Huir? ")
                
                if accion == '2':
                    print("Has huido. Pierdes 10 de vida.")
                    perder_vida(personaje, 10)
                    en_combate = False
                elif accion == '1':
                    vida_monstruo -= monstruo['golpe_usuario']
                    print(f"¡Golpeas al {monstruo['nombre']}! Le haces {monstruo['golpe_usuario']} de daño.")
                    
                    if vida_monstruo <= 0:
                        print(f"¡Has derrotado al {monstruo['nombre']}!")
                        ganar_oro(personaje, monstruo['recompensa_oro'])
                        completar_mision(personaje, monstruo['recompensa_estadistica'], monstruo['recompensa_puntos'])
                        print(f"Oro +{monstruo['recompensa_oro']} | {monstruo['recompensa_estadistica']} +{monstruo['recompensa_puntos']}")
                        en_combate = False
                    else:
                        perder_vida(personaje, monstruo['ataque_monstruo'])
                        print(f"El {monstruo['nombre']} te ataca y te quita {monstruo['ataque_monstruo']} de vida.")
                        if not personaje["Vivo:"]:
                            print("Has muerto en combate.")
                            en_combate = False
                else:
                    print("Opción no válida. Usa '1' o '2'.")
            
            if not personaje["Vivo:"]:
                print("Tu personaje ha muerto. Reinicia el juego para crear uno nuevo.")
            
            
####################################################################################################             
        elif opcion == 5:
            guardar_partida(personaje, misiones_diarias, misiones_principales)
            
####################################################################################################                   
        elif opcion == 6:
            # Procesar misiones diarias
            penalizacionDiarias = 10
            noCompletadas = 0
            for m in misiones_diarias:
                if not m["Completado:"]:
                    perder_vida(personaje, penalizacionDiarias)
                    noCompletadas += 1
            for m in misiones_diarias:
                m["Completado:"] = False
            print(f"Nuevo día, has perdido {penalizacionDiarias * noCompletadas} de vida por {noCompletadas} misiones no completadas.") 
            
            # Procesar misiones principales
            expiradas = 0
            for m in misiones_principales[:]:
                m["Dias restantes:"] -= 1
                if m["Dias restantes:"] <= 0:
                    perder_vida(personaje, 25)
                    print(f"La misión principal '{m['Nombre:']}' ha expirado. Pierdes 25 puntos de vida")
                    misiones_principales.remove(m)
                    expiradas += 1
            if expiradas > 0:
                print(f"Se expiraron {expiradas} misiones principales.")
            else:
                print("No expiró ninguna misión principal.")
                
            print("!EL DÍA HA SIDO REINICIADO CORRECTAMENTE")   
####################################################################################################             
                
        elif opcion == 7:
            print("Ciao")
            ejecutando = False
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()