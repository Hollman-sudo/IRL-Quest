# Importo la función que acabo de crear para crear misiones diarias
from personaje import mostrar_personaje, completar_mision, ganar_oro, perder_vida, crear_personaje
from misiones import crear_mision_diaria

misiones_diarias = []
personaje = crear_personaje("Aventurero")

def main():
     
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
        print("[5] Tienda")
        print("[6] Guardar partida")
        print("[7] Nuevo día")
        print("[8] Salir")
        
        # Verificamos si la opción es un número o no
        try:
            opcion = int(input("\nElige una opción: "))
        except ValueError:
            print("ERROR: Ingresa un número válido.")
            continue
    
        # Si elige 1, mostramos el personaje
        if opcion == 1:
            mostrar_personaje(personaje)  



        # Si elige 2, mostramos el menu de opciones de las misiones diarias   
        elif opcion == 2:
            en_misiones = True
            while en_misiones:
                print("\n" + "="*50)
                print("            MENÚ MISIONES")
                print("="*50) 
                print("[1] Crear Misión.")
                print("[2] Mostrar Misiones sin Terminar.")
                print("[3] Completar Misión.")
                print("[4] Volver al menú principal.")
                   
                try:
                    eleccion = int(input("\nDigite su elección: "))
                except ValueError:
                    print("ERROR: Ingrese un número válido.")
                #Si el usuario digita 1, le pedimos la información para crear la misión      
                if eleccion == 1:
                    nombre = input("Digite el nombre de la misión: ")
                    estadistica = input("Digite el nombre de la estadistica que va a ganar puntos: ")
                    estadistica = input("Digite el nombre de la estadistica que va a ganar puntos: ")
                    # Agregar dos puntos si no los tiene
                    if not estadistica.endswith(":"):
                        estadistica += ":"
                    puntos_estadistica = int(input("Digite los puntos que va a ganar por completar la misión: "))
                    oro = int(input("Digite el oro que va a ganar por completar la misión: "))
                    
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
                               print(f"{i} - {m['Nombre:']} | {m['Estadistica:']} + {m['Puntos de Estadistica:']} | {m['Oro:']}")   
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
                        
                        if 0 <= indiceMision <= len(misiones_diarias):
                            mision = misiones_diarias[indiceMision]
                            # Le damos las recompensas al personaje
                            # Llamamos a la función de completar misiones para dar la recompensa
                            completar_mision(personaje, mision['Estadistica:'], mision['Puntos de Estadistica:'])
                            mision['Completado:'] = True
                            # Llamamos a la función para ganar oro
                            ganar_oro(personaje, mision["Oro:"])
                            
                            print("!Misión completada con exito!")
                            
                    except ValueError:
                        print("ERROR: Debe ingresar un número.")
                    
                elif eleccion == 4:
                    en_misiones = False
                else:
                    print("ERROR: Opción no válida, intente de nuevo.")
                        
                        
                        
                   
        elif opcion == 3:
            print("Misiones principales - ")
        elif opcion == 4:
            print("Eventos aleatorios - ")
        elif opcion == 5:
            print("Tienda - ")
        elif opcion == 6:
            print("Guardando partida...")
            
            
        elif opcion == 7:
            penalizacion = 10
            noCompletadas = 0
            for m in misiones_diarias:
                if not m["Completado:"]:
                    perder_vida(personaje, penalizacion)
                    noCompletadas += 1
            for m in misiones_diarias:
                m["Completado:"] = False
            print(f"Nuevo días, has perdido {penalizacion * noCompletadas} de vida por {noCompletadas} misiones no completadas.") 
            print("!EL DÍA HA SIDO REINICIADO CORRECTAMENTE")   
                
                
        elif opcion == 8:
            print("Ciao")
            ejecutando = False
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()