#Desarrollar el algoritmo de Euclides para calcular el máximo común divisor (MCD) de dos número entero.
def mcd_euclides(a, b):
    while b != 0:
        a, b = b, a % b
    return a


print(mcd_euclides(int(input("introdusca un numero entero: ")), int(input("introdusca un numero entero: "))))  
