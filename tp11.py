#Desarrollar un algoritmo que invierta un número entero sin convertirlo a cadena.
def invert_number(numero):
    if numero < 10:
        return numero
    else:
        return (numero % 10) * 10 ** len(str(numero//10)) + invert_number(numero//10)


print(invert_number(int(input("introdusca la cadena de numero que quieres invertir: "))))