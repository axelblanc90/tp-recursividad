from grafo import Graph

def cargar_personajes():
    grafo = Graph(dirigido=False)

    personajes = [
        "Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett",
        "C-3PO", "Leia", "Rey", "Kylo Ren", "Chewbacca", 
        "Han Solo", "R2-D2", "BB-8"
    ]

    for personaje in personajes:
        grafo.insert_vertice(personaje)

    grafo.insert_arista("Luke Skywalker", "Darth Vader", 5)
    grafo.insert_arista("Yoda", "Darth Vader", 3)
    grafo.insert_arista("Yoda", "Luke Skywalker", 4)
    grafo.insert_arista("Leia", "Luke Skywalker", 6)
    grafo.insert_arista("Rey", "Kylo Ren", 2)
    grafo.insert_arista("Han Solo", "Chewbacca", 7)
    grafo.insert_arista("C-3PO", "R2-D2", 8)
    grafo.insert_arista("BB-8", "Rey", 1)
    grafo.insert_arista("Darth Vader", "Boba Fett", 2)

    return grafo

def obtener_mst(grafo):
    return grafo.kruskal(None)

def contiene_yoda(árbol_expansión_mínimo):
    for arbol in árbol_expansión_mínimo:
        if "Yoda" in arbol:
            return True
    return False

def max_episodios_compartidos(grafo):
    max_episodios = 0
    personajes = (None, None)

    for nodo in grafo.elements:
        for adyacente in nodo['aristas']:
            if adyacente['peso'] > max_episodios:
                max_episodios = adyacente['peso']
                personajes = (nodo['value'], adyacente['value'])

    return max_episodios, personajes

if __name__ == "__main__":
    grafo = cargar_personajes()

    grafo.show_graph()

    #b-1
    árbol_expansión_mínimo = obtener_mst(grafo)
    print("Árbol de expansión mínimo:")
    for arbol in árbol_expansión_mínimo:
        print(arbol)

    # b-2
    if contiene_yoda(árbol_expansión_mínimo):
        print("El árbol expansión mínimo contiene a Yoda.")
    else:
        print("El árbol expansión mínimo no contiene a Yoda.")

    # c
    max_episodios, personajes = max_episodios_compartidos(grafo)
    print(f"El número máximo de episodios compartidos es {max_episodios} entre {personajes[0]} y {personajes[1]}.")
