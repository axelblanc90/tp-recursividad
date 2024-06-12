#Desarrollar una función recursiva que permita listar los elementos de vector/lista de
#manera inversa al que están cargados. Preferentemente la función solo debe tener un
#parámetro que es la lista de elementos.

def invertir_lista(lista):
    if len(lista) <= 1:
        return lista
    else:
        return [lista[-1]] + invertir_lista(lista[:-1])

print(invertir_lista([1, 2, 3, 4, 5, 6, 7]))
