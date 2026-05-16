# Importo la función que acabo de crear para crear misiones diarias
from personaje import mostrar_personaje, completar_mision_diaria, ganar_oro, perder_vida

def main():
    misiones_diarias = []
    
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
        print("[7] Salir")
        
        try:
            opcion = int(input("\nElige una opción: "))
        except ValueError:
            print("ERROR: Ingresa un número válido.")
            continue
        
        if opcion == 1:
            # Llamar a función que muestra el personaje
            print("Mostrando personaje...")  
            
        elif opcion == 2:
            en_misiones = True
            if en_misiones == True:
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
                       
                    if eleccion == 4:
                        en_misiones = False
                        
                   
        elif opcion == 3:
            print("Misiones principales - ")
        elif opcion == 4:
            print("Eventos aleatorios - ")
        elif opcion == 5:
            print("Tienda - ")
        elif opcion == 6:
            print("Guardando partida...")  # placeholder
        elif opcion == 7:
            print("¡Hasta luego!")
            ejecutando = False
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()