#Dada una secuencia de caracteres, obtener dicha secuencia invertida.

def invertir_cadena(cadena):
    
    
    if len(cadena) == 0:
        return cadena
    else:
        return cadena[-1] + invertir_cadena(cadena[:-1])

cadena = input("introduce un secuencia de caracteres para obtener su version inversa: ")
print(invertir_cadena(cadena))