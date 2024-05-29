from pila import Stack

nombresepi5=[('Iron Man', 10),('Captain America', 11),('Black Widow', 8),('Rocket Raccoon', 5),('Groot', 5)]

pila_MCU = Stack()
for element in nombresepi5:
    pila_MCU.push(element)


def posicion_personaje(pila, personaje):
    for i in range(pila.size()):
        if pila.elements[i][0] == personaje:
            return pila.size() - i
    return -1

def personajes_mas_de_cinco(pila):
    return [(nombre, peliculas) for nombre, peliculas in pila.elements if peliculas > 5]

def peliculas_personaje(pila, personaje):
    for nombre, peliculas in pila.elements:
        if nombre == personaje:
            return peliculas
    return 0

def personajes_con_letras(pila, letras):
    nombres = []
    while pila.size() > 0:
        nombre, peliculas = pila.pop()
        if nombre[0] in letras:
            nombres.append(nombre)
    return nombres


print(posicion_personaje(pila_MCU, 'Rocket Raccoon'))
print(posicion_personaje(pila_MCU, 'Groot'))
print(personajes_mas_de_cinco(pila_MCU))
print(peliculas_personaje(pila_MCU, 'Black Widow'))
print(personajes_con_letras(pila_MCU, ['C', 'D', 'G']))