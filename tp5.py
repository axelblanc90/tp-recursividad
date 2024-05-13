#Desarrollar una función que permita convertir un número romano en un número decimal.
valor = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

def Convertir_Decimal(num_Romano, acumulador = 0):
    if len(num_Romano) > 1:
        if valor[num_Romano[0]] >= valor[num_Romano[1]]:
            acumulador = acumulador + valor[num_Romano[0]]
            return Convertir_Decimal(num_Romano[1:], acumulador)
        else:
            acumulador = acumulador - valor[num_Romano[0]]
            return Convertir_Decimal(num_Romano[1:], acumulador)
    elif len(num_Romano) == 1:
       return acumulador + valor[num_Romano[0]]
    else:
        return acumulador

num = input("ingrese los numero a combertir: ")
res = Convertir_Decimal(num)
print("Número decimal:", res)
