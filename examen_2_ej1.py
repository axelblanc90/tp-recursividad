from arbol import BinaryTree
from arbol_avl import BinaryTree

tree_by_number = BinaryTree()
tree_by_name = BinaryTree()
tree_by_type = BinaryTree()

pokemons = [
    {"nombre": "Bulbasaur", "numero": 1, "tipo": ["Planta","veneno"]},
    {"nombre": "Charmander", "numero": 4, "tipo": ["Fuego"]},
    {"nombre": "Jolteon", "numero": 6, "tipo": ["Eléctrico"]},
    {"nombre": "Squirtle", "numero": 7, "tipo": ["Agua"]},
    {"nombre": "Pidgey", "numero": 13, "tipo": ["Normal", "Volador"]},
    {"nombre": "Psyduck", "numero": 54, "tipo": ["Agua"]},
    {"nombre": "Machop", "numero": 66, "tipo": ["Lucha"]},
    {"nombre": "Geodude", "numero": 74, "tipo": ["Roca", "Tierra"]},
    {"nombre": "Ponyta", "numero": 77, "tipo": ["Fuego"]},
    {"nombre": "Magnemite", "numero": 81, "tipo": ["Eléctrico", "Acero"]},
    {"nombre": "Snorlax", "numero": 143, "tipo": ["Normal"]},
    {"nombre": "Gengar", "numero": 94, "tipo": ["Fantasma", "Veneno"]},
    {"nombre": "Tyranitar", "numero": 248, "tipo": ["Roca", "Siniestro"]},
    {"nombre": "Lucario", "numero": 448, "tipo": ["Lucha", "Acero"]},
    {"nombre": "Greninja", "numero": 658, "tipo": ["Agua", "Siniestro"]},
    {"nombre": "Cinderace", "numero": 810, "tipo": ["Fuego"]},
    {"nombre": "Chikorita", "numero": 152, "tipo": ["Planta"]},
    {"nombre": "Togepi", "numero": 175, "tipo": ["Hada"]},
    {"nombre": "Shinx", "numero": 403, "tipo": ["Eléctrico"]},
    {"nombre": "Bagon", "numero": 371, "tipo": ["Dragón"]},
    {"nombre": "Toxel", "numero": 848, "tipo": ["Eléctrico", "Veneno"]},
]


for pokemon in pokemons:
    print(f"Nombre: {pokemon['nombre']}, Número: {pokemon['numero']}, Tipos: {', '.join(pokemon['tipo'])}")

for pokemon in pokemons:
    tree_by_name.insert_node(pokemon["nombre"], other_value=pokemon)
    tree_by_number.insert_node(pokemon["numero"], other_value=pokemon)
    for tipos in pokemon["tipo"]:
        tree_by_type.insert_node(tipos, other_value=pokemon)

def mostrar_pokemon_numero(numero):
    pokemon_by_number = tree_by_number.search(numero)
    if pokemon_by_number is not None:
        print(pokemon_by_number.other_value)
    else: print("no se encontró el pokemon con el número", numero)


mostrar_pokemon_numero(4)

print("b")
print(tree_by_name.proximity_search("bul"))

print("c")
#c)
print("pokemons de tipo Eléctrico ")
tree_by_type.mostrar_pokemons_por_tipo("Eléctrico")
print("pokemons de tipo Fuego ")
tree_by_type.mostrar_pokemons_por_tipo("Fuego")
print("pokemons de tipo Agua ")
tree_by_type.mostrar_pokemons_por_tipo("Agua")
print("pokemons de tipo Planta ")
tree_by_type.mostrar_pokemons_por_tipo("Planta")

print("d")
#d)
print("number")
tree_by_number.inorden()
print("name")
tree_by_name.inorden()
print("name_level")
tree_by_name.by_level()

print("e")
#e)
def mostrar_pokemon():
    for name in ["Jolteon", "Lycanroc", "Tyrantrum"]:
        pokemon = tree_by_name.search(name)
        if pokemon is not None:
            print(pokemon.other_value)

mostrar_pokemon()

print("f")
#f)

def contar_tipos():
    electricos = tree_by_type.contar_pokemons_por_tipo("Eléctrico")
    if electricos is not None:
        print("la cantidad de pokemon tipo electrico es:", electricos)

    aceros = tree_by_type.contar_pokemons_por_tipo("Acero")
    if aceros is not None:
        print("la cantidad de pokemon tipo acero es:", aceros)

contar_tipos()