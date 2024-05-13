bag = ["R2-D2","celular","Sable de luz","mochila propulsora Z-6","equipo de mate",]

def busqueda(vector,buscado):
    if(len(vector) == 0):
        return -1
    elif(buscado == vector[-1]):
        return len(vector) - 1
    else:
        print("saco de la mochila ",vector[-1])

        return busqueda(vector[:-1],buscado)



busquedaObjetos = busqueda(bag,"Sable de luz")
if(busquedaObjetos != -1):
    print("Se tuvieron que sacar",len(bag)-busquedaObjetos,"objetos de la mochila para encontrar el sable de luz")
else:
    print("el sabel de luz no se encontro entre los ",len(bag),"objetos, lamentablemente no podra escapar")