#Desarrollar un algoritmo que permita realizar la suma de los dígitos de un número entero, no se puede convertir el número a cadena.
def sumar_digitos(numero):
    if numero < 10:
        return numero
    else:
        return (numero % 10) + sumar_digitos(numero//10)

print(sumar_digitos(int(input("ingrese sun numero entero: "))))