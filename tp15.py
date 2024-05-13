#Desarrollar una función que permita calcular la raíz cuadrada entera de un número entero.
#Puede utilizar una función auxiliar para que la función principal solo reciba como parámetro
#el número a calcular su raíz.
import math

def raiz_cuadrada_entera(n):
    if n < 0:
        return "Error: n debe ser mayor o igual a 0"
    else:
        raiz = math.sqrt(n)
        return int(raiz)


print(raiz_cuadrada_entera(int(input("ingrese un num entero: "))))  
