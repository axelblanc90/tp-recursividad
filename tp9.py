#Implementar una función para calcular el logaritmo entero de número n en una base b. Recuerde que:
import math

def logaritmo_entero(n, b):
    if n <= 0 or b <= 0:
        return "Error: n y b deben ser mayores que 0"
    else:
        logaritmo = math.log(n, b)
        return int(logaritmo)

print(logaritmo_entero(float(input("introdusca el munerador ")), float(input("introdusca el denominador "))))
