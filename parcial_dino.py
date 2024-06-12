#parámetro que es la lista de elementos. 2. Dada una pila con los datos de dinosaurios resolver lo siguiente actividades:

class Stack:
    def __init__(self):
        self.elements = []
    
    def push(self, element):
        self.elements.append(element)

    def pop(self):
        if len(self.elements) > 0:
            return self.elements.pop()
        else:
            return None

    def on_top(self):
        if len(self.elements) > 0:
            return self.elements[-1]
        else:
            return None

    def size(self):
        return len(self.elements)

dinosaurios = [
    {
      "nombre": "Tyrannosaurus Rex",
      "especie": "Theropoda",
      "peso": 7000,
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1902
    },
    {
      "nombre": "Triceratops",
      "especie": "Ceratopsidae",
      "peso": 6000,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1889
    },
    {
      "nombre": "Velociraptor",
      "especie": "Dromaeosauridae",
      "peso": 15,
      "descubridor": "Henry Fairfield Osborn",
      "ano_descubrimiento": 1924
    },
    {
      "nombre": "Brachiosaurus",
      "especie": "Sauropoda",
      "peso": 56000,
      "descubridor": "Elmer S. Riggs",
      "ano_descubrimiento": 1903
    },
    {
      "nombre": "Stegosaurus",
      "especie": "Stegosauridae",
      "peso": 5000,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Spinosaurus",
      "especie": "Spinosauridae",
      "peso": 10000,
      "descubridor": "Ernst Stromer",
      "ano_descubrimiento": 1912
    },
    {
      "nombre": "Allosaurus",
      "especie": "Theropoda",
      "peso": 2000,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Apatosaurus",
      "especie": "Sauropoda",
      "peso": 23000,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Diplodocus",
      "especie": "Sauropoda",
      "peso": 15000,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1878
    },
    {
      "nombre": "Ankylosaurus",
      "especie": "Ankylosauridae",
      "peso": 6000,
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1908
    },
    {
      "nombre": "Parasaurolophus",
      "especie": "Hadrosauridae",
      "peso": 2500,
      "descubridor": "William Parks",
      "ano_descubrimiento": 1922
    },
    {
      "nombre": "Carnotaurus",
      "especie": "Theropoda",
      "peso": 1500,
      "descubridor": "José Bonaparte",
      "ano_descubrimiento": 1985
    },
    {
      "nombre": "Styracosaurus",
      "especie": "Ceratopsidae",
      "peso": 2700,
      "descubridor": "Lawrence Lambe",
      "ano_descubrimiento": 1913
    },
    {
      "nombre": "Therizinosaurus",
      "especie": "Therizinosauridae",
      "peso": 5000,
      "descubridor": "Evgeny Maleev",
      "ano_descubrimiento": 1954
    },
    {
      "nombre": "Pteranodon",
      "especie": "Pterosauria",
      "peso": 25,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1876
    },
    {
      "nombre": "Quetzalcoatlus",
      "especie": "Pterosauria",
      "peso": 200,
      "descubridor": "Douglas A. Lawson",
      "ano_descubrimiento": 1971
    },
    {
      "nombre": "Plesiosaurus",
      "especie": "Plesiosauria",
      "peso": 450,
      "descubridor": "Mary Anning",
      "ano_descubrimiento": 1824
    },
    {
      "nombre": "Mosasaurus",
      "especie": "Mosasauridae",
      "peso": 15000,
      "descubridor": "William Conybeare",
      "ano_descubrimiento": 1829
    },

  ]

pila_dinosaurios = Stack()

pila_aux=Stack()
for dinosaurio in dinosaurios:
    pila_dinosaurios.push(dinosaurio)

def rearmar_pila(pila_dinosaurios, pila_aux):
    while pila_aux.size() > 0:
        pila_dinosaurios.push(pila_aux.pop())


#a) Contar cuantas especies hay;

def contar_especies(pila_dinosaurios, parametro):
    lista_parametro=[]
    while pila_dinosaurios.size() > 0:
        if lista_parametro.count(pila_dinosaurios.on_top()[parametro]) == 0:
            lista_parametro.append(pila_dinosaurios.on_top()[parametro])
            pila_aux.push(pila_dinosaurios.pop())
        else:
            pila_aux.push(pila_dinosaurios.pop())
    return len(lista_parametro)

print("la cantidad de especies unicas son: ",contar_especies(pila_dinosaurios,"especie"))
print()
rearmar_pila(pila_dinosaurios,pila_aux)
#b)Determinar cuantos descubridores distintos hay;


def contar_descubridor(pila_dinosaurios, parametro):
    lista_parametro=[]
    while pila_dinosaurios.size() > 0:
        if lista_parametro.count(pila_dinosaurios.on_top()[parametro]) == 0:
            lista_parametro.append(pila_dinosaurios.on_top()[parametro])
            pila_aux.push(pila_dinosaurios.pop())
        else:
            pila_aux.push(pila_dinosaurios.pop())
    return len(lista_parametro)



print("los descubridores unicos son : ",contar_descubridor(pila_dinosaurios,"descubridor"))
print()

rearmar_pila(pila_dinosaurios, pila_aux)
#c) Mostrar todos los dinosaurios que empiecen con T

def dinosaurios_T(pila_dinosaurios):
    dinos_T=[]
    while pila_dinosaurios.size() > 0:
        if pila_dinosaurios.on_top()["nombre"].startswith(("T")):
            dinos_T.append(pila_dinosaurios.on_top()["nombre"])
            pila_aux.push(pila_dinosaurios.pop())
        else:
            pila_aux.push(pila_dinosaurios.pop())
    return dinos_T

print(dinosaurios_T(pila_dinosaurios))
print()
rearmar_pila(pila_dinosaurios, pila_aux)
#d) Mostrar todos los dinosaurio que pesen menos de 275 Kg

menores_275 = []
for i in range(pila_dinosaurios.size()):
    if pila_dinosaurios.on_top()['peso']<275:
        menores_275.append(pila_dinosaurios.on_top()['nombre'])
        menores_275.append(pila_dinosaurios.on_top()['peso'])
        data=pila_dinosaurios.pop()
        pila_aux.push(data)
    else:
        data=pila_dinosaurios.pop()
        pila_aux.push(data)

print("estos dinosaurios pesan menos de 275KG")
for element in menores_275:
    print(element)

rearmar_pila(pila_dinosaurios, pila_aux)
print()
#e) Dejar en una pila aparte todos los dinosaurios que comienzan con A, Q, S;

def dinosaurios_A_Q_S(pila_dinosaurios):
    dino_A_Q_S=[]
    while pila_dinosaurios.size() > 0:
        if pila_dinosaurios.on_top()["nombre"].startswith(("A","Q","S")):
            dino_A_Q_S.append(pila_dinosaurios.on_top())
            pila_aux.push(pila_dinosaurios.pop())
        else:
            pila_aux.push(pila_dinosaurios.pop())
    return dino_A_Q_S

print(f"los dinosaurios que sus nombres inician con [A][Q][S] son :{dinosaurios_A_Q_S(pila_dinosaurios)}")
print()
rearmar_pila(pila_dinosaurios, pila_aux)


