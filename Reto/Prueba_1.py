# Inicialización de variables
RPM_B = 0
RPM_A = 0
registro_eventos = []  # Lista para guardar eventos por minuto
estadisticas = {"RPM_Bajo": 0, "RPM_Alto": 0, "RPM_Seguro": 0}  # Diccionario para contar tipos de eventos

# Entrada del usuario


# Simulación por intervalos de tiempo
for TIEMPO in range(1, 61, 10):
    POR_POT = int(input("Introduzca un porcentaje de potencia (sin el signo %): "))
    RPM = 10 + (POR_POT / 100) * (3000 - 10)
    evento = {"minuto": TIEMPO, "RPM": RPM, "estado": ""}

    if RPM <= 1000:
        RPM_B += 1
        estadisticas["RPM_Bajo"] += 1
        evento["estado"] = "Nivel bajo de RPM"
        print(f"Nivel bajo de RPM en el minuto {TIEMPO}")
    elif RPM <= 2500:
        estadisticas["RPM_Seguro"] += 1
        evento["estado"] = "Umbral Seguro"
        print("Umbral Seguro")
    elif RPM >= 2501:
        RPM_A += 1
        estadisticas["RPM_Alto"] += 1
        evento["estado"] = "Sobretorque"
        print(f"Sobretorque en el minuto {TIEMPO}")

    registro_eventos.append(evento)
    print(f"Contadores: RPM_Bajo={RPM_B}, RPM_Alto={RPM_A}, Tiempo={TIEMPO}")

# Mostrar resumen final
print("\nResumen de eventos:")
for evento in registro_eventos:
    print(f"Minuto {evento['minuto']}: RPM={evento['RPM']:.2f} - Estado: {evento['estado']}")

print("\nEstadísticas generales:")
for clave, valor in estadisticas.items():
    print(f"{clave}: {valor}")