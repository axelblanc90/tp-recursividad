#Desarrollar el algoritmo de Euclides para calcular también el mínimo común múltiplo (MCM)
#de dos número entero.

def mcd_euclides(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mcm_euclides(a, b):
    mcd = mcd_euclides(a, b)
    return abs(a * b) // mcd


print(mcd_euclides(int(input("introdusca un numero entero para mcd: ")), int(input("introdusca un numero entero para mcd: "))))  
print(mcm_euclides(int(input("introdusca un numero entero para mcm: ")), int(input("introdusca un numero entero para mcm: "))))  

