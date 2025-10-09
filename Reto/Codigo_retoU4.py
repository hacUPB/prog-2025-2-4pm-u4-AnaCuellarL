Resumen = { "registros_elevados":[], "registros_bajos":[],"Umbral_seguro" : [], "TIEMPO":[]}

estadisticas = {"RPM_B": 0, "RPM_A": 0}

def simulacion_taco():
    RPM_B = 0
    RPM_A = 0



    for TIEMPO in range(1, 61, 5):
        POR_POT = int(input("Introduzca un porcentaje de potencia (sin el signo %): "))
        RPM = 10 + (POR_POT / 100) * (3000 - 10)

        if RPM <= 1000:
            RPM_B += 1
            estadisticas["RPM_B"] += 1
            Resumen["TIEMPO"].append(TIEMPO)
            Resumen["registros_bajos"].append(RPM)
            print(f"Nivel bajo de RPM en el minuto {TIEMPO}")
        elif RPM <= 2500:
            Resumen["TIEMPO"].append(TIEMPO)
            Resumen["Umbral_seguro"].append(RPM)
            print(f"Nivel bajo de RPM en el minuto {TIEMPO}")        
            print("Umbral Seguro")
        elif RPM >= 2501:
            RPM_A += 1
            estadisticas["RPM_A"] += 1
            Resumen["TIEMPO"].append(TIEMPO)
            Resumen["registros_elevados"].append(RPM)
            print(f"Sobretorque en el minuto {TIEMPO}")
        print(f"Contadores: RPM_Bajo={RPM_B}, RPM_Alto={RPM_A}, Tiempo={TIEMPO}")

    print("\nResumen de eventos:")
    for clave, valor in Resumen.items():
        print(f" {clave} : {valor}")

    print("\nEstadísticas generales:")
    for clave, valor in estadisticas.items():
        print(f"{clave}: {valor}")



while True:

    Opc = int(input("Menú principal\n1. Simulación tacómetro\n2. Imprimir diccionario\n3.Imprimir lista\n4.Salir\nIngrese una opción:"))

    match Opc:
        case 1:
            simulacion_taco()
        case 2:
            for clave,valor in Resumen.items():
                print(f"{clave} : {valor}")
        case 3:
            for clave,valor in Resumen.items():
                for datos in Resumen["registros_bajos"]:
                    print(datos)
                for datos in Resumen["registros_elevados"]:
                    print(datos)    
                for datos in Resumen["TIEMPO"]:
                    print(datos)   
                for datos in Resumen["Umbral_seguro"]:
                    print(datos)               
        case 4:
            print("Saliendo del programa...")
            break
        case _:
            print("Opción no valida")