from pila import Stack
pila_star_wars_V = Stack()
pila_star_wars_VII = Stack()

pila_star_wars_V.push('Luke Skywalker')
pila_star_wars_V.push('Han Solo')
pila_star_wars_V.push('Darth Vader')

pila_star_wars_VII.push('Rey')
pila_star_wars_VII.push('Finn')
pila_star_wars_VII.push('Luke Skywalker')


def interseccion_pilas(pila1, pila2):
    return list(set(pila1.elements) & set(pila2.elements))

print(interseccion_pilas(pila_star_wars_V, pila_star_wars_VII))
