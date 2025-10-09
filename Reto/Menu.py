from Codigo_retoU4 import *

while True:

    Opc = int(input("Menú principal\n1. Simulación tacómetro\n2. Salir\nIngrese una opción:"))

    match Opc:
        case 1:
            simulacion_taco()
        case 2:
            print("Saliendo del programa...")
            break
        case _:
            print("Opción no valida")