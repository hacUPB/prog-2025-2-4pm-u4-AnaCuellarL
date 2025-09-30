import random

lista = []

lista.append(56)
print(lista)

numero = int(input("Ingrese un número entero: "))
lista.append(numero)

#Ejercicio 1: quiero ingresar 10 números aleatorios.

for i in range (10):
    aleat = random.randint(0,100)
    lista.append(aleat)

print(lista)