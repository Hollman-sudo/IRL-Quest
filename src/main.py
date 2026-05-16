# Importo la función que acabo de crear para crear misiones diarias
from misiones import crear_mision_diaria

def main():
    # Crear personaje 
    # personaje = crear_personaje("Aventurero")
    
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
            print("Misiones diarias - ")
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