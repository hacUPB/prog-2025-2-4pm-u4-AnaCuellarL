# Creamos un objeto (en este caso, un número).
'''
altitud = 10000  # metros

# 'altitud' es una etiqueta que apunta al objeto entero 10000
# Podemos crear otra etiqueta que apunte al mismo objeto
elevacion = altitud

# Si modificamos el valor al que apunta 'elevacion'
elevacion = 9500

# 'altitud' sigue apuntando al valor original
print(altitud)  # 10000
print(elevacion)  # 9500
'''
# ID de Objetos:
'''
velocidad = 800  # km/h
print(id(velocidad))  # Muestra el identificador único del objeto

otra_velocidad = 800
print(id(otra_velocidad))  # Para números pequeños, Python reutiliza objetos

lista1 = [1, 3, 67]
print(id(lista1))
'''
# Ejemplo de inmutabilidad ("string"):
'''
modelo = "Boeing 747"
print(id(modelo))  # Guardamos el ID original

# Intentamos "modificar" el string
modelo = modelo + "-800"
print(modelo)  # "Boeing 747-800"
print(id(modelo))  # ¡ID diferente! Se creó un nuevo objeto
'''
#Ejemplo de mutabilidad ("Listas"):

'''
componentes = ["alas", "fuselaje", "motores"]
print(id(componentes))  # Guardamos el ID original

# Modificamos la lista
componentes.append("tren de aterrizaje")
print(componentes)  # ["alas", "fuselaje", "motores", "tren de aterrizaje"]
print(id(componentes))  # Mismo ID, el objeto fue modificado in-place
'''

#Como afecta la mutabilidad a una función:

'''
def agregar_combustible(tanques, litros):
    tanques.append(litros)
    print(f"Combustible actualizado: {tanques}")

combustible_actual = [1000, 1200, 800]  # Lista (objeto mutable)
agregar_combustible(combustible_actual, 500)
print(combustible_actual)  # [1000, 1200, 800, 500] - La lista original fue modificada
'''

# Iterando sobre una lista de sensores de aeronave

'''
sensores = ["temperatura", "presión", "velocidad", "altitud", "combustible"]

for sensor in sensores:
    print(f"Comprobando sensor de {sensor}...")
'''

# Simulando lecturas de altitud cada 10 segundos

'''
altitudes = [0, 100, 500, 1000, 1500, 2000, 2200, 2500]
tiempo = 0
i = 0

while i < len(altitudes):
    print(f"Tiempo: {tiempo}s - Altitud: {altitudes[i]} metros")
    tiempo += 10
    i += 1
'''

# Funcion enumerate():

'''
for i, etapa in enumerate(["despegue", "ascenso", "crucero", "descenso", "aterrizaje"]):
    print(f"Etapa {i+1}: {etapa}")
'''

# Función zip():

'''
tiempos = [0, 10, 20, 30]
velocidades = [0, 200, 300, 320]

for t, v in zip(tiempos, velocidades):
    print(f"Tiempo: {t}s - Velocidad: {v} km/h")
'''

# Comprensión de listas:

# Convertir altitudes de pies a metros:

'''
altitudes_pies = [10000, 15000, 20000, 25000, 30000]
altitudes_metros = [altura * 0.3048 for altura in altitudes_pies]
print(altitudes_metros)
'''