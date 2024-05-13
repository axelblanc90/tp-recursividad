#Desarrollar un algoritmo que permita calcular la siguiente serie

def sumatoria_serie(numero):
    if numero == 1:
        return 1
    else:
        return 1/numero + sumatoria_serie(numero-1)

print(sumatoria_serie(float(input("introdusca un numero para saver su sumatoria: "))))

