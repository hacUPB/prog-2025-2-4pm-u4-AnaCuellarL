# Descripción del problema del reto anterior:

Se quiere realizar una simulación que simule el funcionamiento de un tacometro de un motor reciproco,
además, al ingresarle el porcentaje de potencia y al analizarla envia una alerta si hay un sobre torque,
enviando al final del vuelo las alertas que se hayan generado.

## Pseudocódigo:

```
LEER POR_POT
TIEMPO=1
RPM_B=0
RPM_A=0

MIENTRAS TIEMPO<61
    RPM=10+(POR_POT/100)*(3000-10)
    SI RPM<=1000
        RPM_B=RPM_B + 1
        MOSTRAR "Nivel bajo de RPM", TIEMPO
    SINO SI RPM<=2500
        MOSTRAR "Umbral Seguro"
    SINO SI RPM>=2501
        RPM_A=RPM_A+1
        MOSTRAR "Sobretorque", TIEMPO
    FIN SI
    TIMEPO=TIEMPO+10
FIN MIENTRAS 
MOSTRAR RPM_B,RPM_A,TIEMPO

```

## Propuesta de uso de listas y diccionarios:

- **Idea 1:** Se plantea añadir una lista que almacene los valores que estén por encima del rango seguro,
y otra lista qure almacene los valores que estén por debajo del rango seguro, y un diccionario que almacene
el número de alertas que hubo, y, al final imprima todas los valores de las listas.


