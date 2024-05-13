#Desarrollar un algoritmo que cuente la cantidad de dígitos de un número entero.

def count_digit(numero):
    if numero < 10:
        return 1
    else:
        return 1 + count_digit(numero//10)

print(count_digit(int(input("introdusca los numeros a contar: "))))