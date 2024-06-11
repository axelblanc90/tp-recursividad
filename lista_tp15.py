from random import choice
from lista import search, by_name, show_list_list,by_hegiht,nivel_pokemon
entrenadores = [
    {
    "nombre": "Ash Ketchum",
    "torneos_ganados": 7,
    "batallas_perdidas": 50,
    "batallas_ganadas": 120
    },
    {
    "nombre": "Goh",
    "torneos_ganados": 2,
    "batallas_perdidas": 10,
    "batallas_ganadas": 40
    },
    {
    "nombre": "Leon",
    "torneos_ganados": 10,
    "batallas_perdidas": 5,
    "batallas_ganadas": 100
    },
    {
    "nombre": "Chloe",
    "torneos_ganados": 1,
    "batallas_perdidas": 8,
    "batallas_ganadas": 30
    },
    {
    "nombre": "Raihan",
    "torneos_ganados": 4,
    "batallas_perdidas": 15,
    "batallas_ganadas": 60
    }
]

pokemons=[
    {
        "nombre": "Pikachu",
        "nivel": 35,
        "tipo": "Eléctrico",
        "subtipo": None
    },
    {
        "nombre": "Pikachu",
        "nivel": 35,
        "tipo": "Eléctrico",
        "subtipo": None
    },
    {
        "nombre": "Charizard",
        "nivel": 40,
        "tipo": "Fuego",
        "subtipo": "Volador"
    },
    {
        "nombre": "Bulbasaur",
        "nivel": 30,
        "tipo": "Planta",
        "subtipo": "Veneno"
    },
    {
        "nombre": "Starmie",
        "nivel": 30,
        "tipo": "Agua",
        "subtipo": "Psíquico"
    },
    {
        "nombre": "Psyduck",
        "nivel": 25,
        "tipo": "Agua",
        "subtipo": None
    },
    {
        "nombre": "Gyarados",
        "nivel": 35,
        "tipo": "Agua",
        "subtipo": "Volador"
    },
    {
        "nombre": "Onix",
        "nivel": 38,
        "tipo": "Roca",
        "subtipo": "Tierra"
    },
    {
        "nombre": "Geodude",
        "nivel": 28,
        "tipo": "Roca",
        "subtipo": "Tierra"
    },
    {
        "nombre": "Vulpix",
        "nivel": 20,
        "tipo": "Fuego",
        "subtipo": None
    },
    {
        "nombre": "Blastoise",
        "nivel": 50,
        "tipo": "Agua",
        "subtipo": None
    },
    {
        "nombre": "Umbreon",
        "nivel": 45,
        "tipo": "Siniestro",
        "subtipo": None
    },
    {
        "nombre": "Nidoking",
        "nivel": 40,
        "tipo": "Veneno",
        "subtipo": "Tierra"
    }
]

lista_entrenadores=[]

nombre=["Ash Ketchum","Goh","Leon","Chloe","Raihan",]
nombre_poke=["Pikachu"]

for entrenador in entrenadores:
    entrenador.update({"sublist":[]})
    lista_entrenadores.append(entrenador)

for pokemon in pokemons:
    pos = search(lista_entrenadores,"nombre",choice(nombre))
    if pos is not None:
        lista_entrenadores[pos]["sublist"].append(pokemon)
    else:
        print("no exsiste el entrenador")

lista_entrenadores.sort(key=by_name)
show_list_list("entrenadores"," pokemons", lista_entrenadores)

print()
#obtener la cantidad de Pokémons de un determinado entrenador;
def cantidad_pokemons(lista_entrenadores,x): 
    for pokemon in pokemons:
        pos = search(lista_entrenadores,"nombre",x)
        if pos is not None:
            return (print ("la cantidda de pokemons es " , len(lista_entrenadores[pos]["sublist"])))
        else:
            print("el entrenador no existe")
x="Raihan"
x=input("escoja a su entrenado para saver la cantidad de pokemos que tiene ")
print(cantidad_pokemons(lista_entrenadores,x))



print()
#b. listar los entrenadores que hayan ganado más de tres torneos;
lista_entrenadores.sort(key=by_hegiht, reverse=True)

def tres_ganados(lista_entrenadores):
    print("estoy son los entrenadores ")
    for index, element in enumerate(lista_entrenadores):
        if element["torneos_ganados"]>3:
            print(index, element["nombre"],"los torneos que gano son: ",element["torneos_ganados"])
    return()

tres_ganados(lista_entrenadores)
print()
##c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
def entrenador_con_mas_torneos(entrenadores):
    entrenadores.sort(key=by_hegiht, reverse=True)
    return entrenadores[0]
def pokemon_de_mayor_nivel(pokemons):
    pokemons.sort(key=nivel_pokemon, reverse=True)
    return pokemons[0]
entrenadores = lista_entrenadores
print('El entrenador con más torneos ganados es:', entrenador_con_mas_torneos(entrenadores))
print('Su pokemon de mayor nivel es:', pokemon_de_mayor_nivel(entrenador['sublist'])," y su nivel es: ",pokemon_de_mayor_nivel(entrenador['sublist']))

print()
#d. mostrar todos los datos de un entrenador y sus Pokémos;
def mostrar_entrenador_y_pokemon(lista_entrenadores):
    pos = search(lista_entrenadores,"nombre","Leon")
    if pos is not None:
        print(f"Nombre del entrenador: {lista_entrenadores[pos]}")


mostrar_entrenador_y_pokemon(lista_entrenadores)



print()
##e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;

def porcentaje_victorias(entrenador):
    total_batallas = entrenador['batallas_ganadas'] + entrenador['batallas_perdidas']#
    return (entrenador['batallas_ganadas'] / total_batallas) * 100

def mostrar_entrenadores_exitosos(entrenadores):
    for entrenador in entrenadores:
        porcentaje = porcentaje_victorias(entrenador)
        if porcentaje > 79:
            print(f"Nombre del entrenador: {entrenador['nombre']}")
            print(f"Porcentaje de victorias: {porcentaje}%")
            print()

mostrar_entrenadores_exitosos(lista_entrenadores)
#f.los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador(tipo y subtipo);
print()
def pokemones_fuego_planta(lista_entrenadores):
     for index, element in enumerate(lista_entrenadores):
         pos = search(lista_entrenadores, 'nombre', nombre[index])
         if pos is not None:
             pos_fuego = search(lista_entrenadores[pos]['sublist'], 'tipo', 'Fuego')
             if pos_fuego is not None:
                 pos_planta = search(lista_entrenadores[pos]['sublist'], 'subtipo', 'Planta')
                 if pos_planta is not None:
                     print(f"Estos son los entrenadores que tienen pokemons de tipo Fuego y Planta:{lista_entrenadores[pos]['nombre']}")
     return
def pokemones_agua_volador(lista_entrenadores):
     for index, element in enumerate(lista_entrenadores):
         pos = search(lista_entrenadores, 'nombre', nombre[index])
         if pos is not None:
             pos_agua = search(lista_entrenadores[pos]['sublist'], 'tipo', 'Agua')
             if pos_agua is not None:
                 pos_volador = search(lista_entrenadores[pos]['sublist'], 'subtipo', 'Volador')
                 if pos_volador is not None:
                     print(f"Estos son los entrenadores que tienen pokemons de tipo Agua y Volador:{lista_entrenadores[pos]['nombre']}")
     return
pokemones_agua_volador(lista_entrenadores)
pokemones_fuego_planta(lista_entrenadores)
print()
#g. el promedio de nivel de los Pokémons de un determinado entrenador;

def promedio_nivel_pokemon(nombre):
    pos = search(lista_entrenadores, 'nombre', nombre)
    if pos is not None:
        pokemons = lista_entrenadores[pos]['sublist']
        promedio = sum([pokemon['nivel'] for pokemon in pokemons]) / len(pokemons)
        return promedio
    else:
        print("No se encontró al entrenador.")
        return None


nombre= input("ingrese el nombre del entrenador: ")
promedio = promedio_nivel_pokemon(nombre)
if promedio is not None:
   print(f"El promedio de nivel de los Pokémon de {nombre} es {promedio}%")

print()
##h. determinar cuántos entrenadores tienen a un determinado Pokémon;
def cantidad_entrenadores(lista_entrenadores,): 
    x=input("escoja a su entrenado para saver la cantidad de pokemos que tiene ")
    y=0
    for index,elememt in enumerate(lista_entrenadores):
        pos = search(lista_entrenadores,"nombre",nombre[index])
        if pos is not None:
            pos_pokenon= search(lista_entrenadores[pos]["sublist"],"nombre",x)
            if pos_pokenon is not None:
                y+=1
    return(f" la cantodad de entrenadores quie tiene {x}, es {y}")

print(cantidad_entrenadores(lista_entrenadores))

print()
#i. mostrar los entrenadores que tienen Pokémons repetidos;
def encontrar_pokemon_repetido(lista_entrenadores):
    for entrenador in lista_entrenadores:
        pila_pokemon = []
        pokemon_repetido = set()
        for pokemon in entrenador['sublist']:
            if pokemon in pila_pokemon:
                pokemon_repetido.add(pokemon)
            else:
                pila_pokemon.append(pokemon)
        if pokemon_repetido:
            print(f"El entrenador {entrenador['nombre']} tiene los siguientes Pokémons repetidos: {pokemon_repetido}")

encontrar_pokemon_repetido(lista_entrenadores)


print()
#j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;
def buscar_Tyrantrum(lista_entrenadores):
    for index, element in enumerate(lista_entrenadores):
        pos = search(lista_entrenadores, 'nombre', element["nombre"])
        if pos is not None:
            pos_Tyrantrum = search(lista_entrenadores[pos]['sublist'], 'nombre', 'Tyrantrum')
            if pos_Tyrantrum is not None:
                print({element["nombre"]},": tiene a Tyrantrum ")
def buscar_Terrakion(lista_entrenadores):
    for index, element in enumerate(lista_entrenadores):
        pos = search(lista_entrenadores, 'nombre', element["nombre"])
        if pos is not None:
            pos_Terrakion = search(lista_entrenadores[pos]['sublist'], 'nombre', 'Terrakion')
            if pos_Terrakion is not None:
                print({element["nombre"]},": tiene a Terrakion ")

def buscar_Wingull(lista_entrenadores):
    for index, element in enumerate(lista_entrenadores):
        pos = search(lista_entrenadores, 'nombre', element["nombre"])
        if pos is not None:
            pos_Wingull = search(lista_entrenadores[pos]['sublist'], 'nombre', 'Wingull')
            if pos_Wingull is not None:
                print({element["nombre"]},": tiene a Wingull ") 
                
buscar_Tyrantrum(lista_entrenadores)
print()
buscar_Terrakion(lista_entrenadores)
print()
buscar_Wingull(lista_entrenadores)


print()
#k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenadorcomo del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
def encontrar_pokemon(lista_entrenadores, nombre,nombre_poke):
    x=input("ingrese el nombre de el pokemmon: ")
    y=input("ingrese el nombre de el pokemon: ")

    pos=search(lista_entrenadores, "nombre", x)
    if pos is not None:
        pos_poke=search(lista_entrenadores[pos]["sublist"], "nombre",y)
        if pos_poke is not None:
            print(f"{x} tiene a {y} y esto son los datos de el pokemon: ")
            print(lista_entrenadores[pos]["sublist"][pos_poke])
            print()
            print(f"los datos de el entrenador son:{lista_entrenadores[pos]} ")
        else:
            print(f"{x} no posee a {y}")

encontrar_pokemon(lista_entrenadores,nombre,nombre_poke)