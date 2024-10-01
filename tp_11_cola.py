#Dada una cola con personajes de la saga Star Wars, de los cuales se conoce su nombre y planeta
#de origen. Desarrollar las funciones necesarias para resolver las siguientes actividades:

jedis = [
    {
        "name": "Qui-Gon Jinn",
        "rank": "Jedi Master",
        "species": "Human",
        "master": "Tera Sinube/Count Dooku",
        "lightsaber_color": "Green",
        "homeworld": "Coruscant",
        "birth_year": "79ABY",
        "height": 1.93,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Obi-Wan Kenobi",
        "rank": "Jedi Master",
        "species": "Human",
        "master": "Qui-Gon Jinn/Yoda",
        "lightsaber_color": "Blue",
        "homeworld": "Stewjon",
        "birth_year": "57ABY",
        "height": 1.82,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Luke Skywalker",
        "rank": "Jedi Knight",
        "species": "Human",
        "master": "Obi-Wan Kenobi/Yoda",
        "lightsaber_color": "Green",
        "homeworld": "Tatooine",
        "birth_year": "19BBY",
        "height": 1.72,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Han Solo",
        "rank": "Smuggler",
        "species": "Human",
        "master": None,
        "lightsaber_color": None,
        "homeworld": "Corellia",
        "birth_year": "29BBY",
        "height": 1.80,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Yoda",
        "rank": "Jedi Grand Master",
        "species": "Unknown",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Unknown",
        "birth_year": "896BBY",
        "height": 0.66,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Jar Jar Binks",
        "rank": "Senator",
        "species": "Gungan",
        "master": None,
        "lightsaber_color": None,
        "homeworld": "Naboo",
        "birth_year": "52BBY",
        "height": 1.96,
        "to_darkside": None,
        "come_lightside": None
    }
]

def mostrar_personajes_por_planeta(jedis, planetas):
    personajes = [jedi['name'] for jedi in jedis if jedi['homeworld'] in planetas]
    return personajes

def planeta_natal(jedis, nombres):
    planetas = {jedi['name']: jedi['homeworld'] for jedi in jedis if jedi['name'] in nombres}
    return planetas

def insertar_personaje_antes_de(jedis, nuevo_personaje, nombre_referencia):
    for i, jedi in enumerate(jedis):
        if jedi['name'] == nombre_referencia:
            jedis.insert(i, nuevo_personaje)
            break
    return jedis

def eliminar_personaje_despues_de(jedis, nombre_referencia):
    for i, jedi in enumerate(jedis):
        if jedi['name'] == nombre_referencia and i + 1 < len(jedis):
            jedis.pop(i + 1)
            break
    return jedis

planetas = ["Alderaan", "Endor", "Tatooine"]
personajes_en_planetas = mostrar_personajes_por_planeta(jedis, planetas)
print("Personajes en Alderaan, Endor y Tatooine:", personajes_en_planetas)

nombres = ["Luke Skywalker", "Han Solo"]
planetas_natal = planeta_natal(jedis, nombres)
print("Planeta natal de Luke Skywalker y Han Solo:", planetas_natal)

nuevo_personaje = {
    "name": "Ahsoka Tano",
    "rank": "Jedi Knight",
    "species": "Togruta",
    "master": "Anakin Skywalker",
    "lightsaber_color": "White",
    "homeworld": "Shili",
    "birth_year": "36BBY",
    "height": 1.73,
    "to_darkside": None,
    "come_lightside": None
}
jedis_actualizados = insertar_personaje_antes_de(jedis, nuevo_personaje, "Yoda")
print("Lista actualizada con Ahsoka Tano antes de Yoda:", [jedi['name'] for jedi in jedis_actualizados])

jedis_actualizados = eliminar_personaje_despues_de(jedis, "Jar Jar Binks")
print("Lista actualizada tras eliminar personaje después de Jar Jar Binks:", [jedi['name'] for jedi in jedis_actualizados])
