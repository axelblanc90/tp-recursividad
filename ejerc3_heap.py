from heap import HeapMax

operaciones = HeapMax()

# a. debe contemplar distintas prioridades para el control de operaciones de acuerdo al siguien-
# te criterio: pedidos de líder supremo Snoke y de Kylo Ren nivel tres, de capitán Phasma
# nivel dos y el resto de las operaciones nivel a cargo de los generales de la base de nivel uno;

# b. de cada actividad se conoce quien es el encargado, una descripción, la hora y opcional-
# mente la cantidad de Stormtroopers requeridos;

# c. utilizar una cola de prioridad para administrar las distintas operaciones, debe cargar al
# menos ocho: dos de nivel tres, cuatro de nivel dos y cuatro de nivel uno;

# nivel 3 
operaciones.add((3, "Snoke", "Reunión secreta con los líderes", "14:00", None))
operaciones.add((3, "Kylo Ren", "Entrenamiento con sable láser", "15:30", None))

# nivel 2 
operaciones.add((2, "Capitán Phasma", "Revisión de seguridad de la base", "10:00", 20))
operaciones.add((2, "Capitán Phasma", "Mantenimiento de droides", "12:30", None))
operaciones.add((2, "Capitán Phasma", "Entrenamiento de Stormtroopers", "16:00", 50))
operaciones.add((2, "Capitán Phasma", "Supervisión del hangar", "13:00", 10))

# nivel 1 
operaciones.add((1, "General Hux", "Informe de operaciones", "09:00", None))
operaciones.add((1, "General Hux", "Revisión de suministros", "11:00", None))
operaciones.add((1, "General Hux", "Control de daños en la base", "17:00", 5))
operaciones.add((1, "General Hux", "Reparación del escudo de energía", "18:30", None))

# e. realizar la atención de las operaciones de la cola;
def atender_operaciones(queue):
    operation = queue.remove()
    if operation:
        print(f"Atendiendo operación: {operation[2]} por {operation[1]} a las {operation[3]}")
        if operation[4]:
            print(f"Requiere {operation[4]} Stormtroopers")
        else:
            print("No requiere Stormtroopers")
    else:
        print("No hay más operaciones para atender.")
    
    nueva_operacion = input("¿Deseas agregar una nueva operación? (s/n): ")
    if nueva_operacion == "s":
        encargado = input("Encargado de la operación: ")
        descripcion = input("Descripción de la operación: ")
        hora = input("Hora de la operación: ")
        prioridad = int(input("Prioridad (1, 2, 3): "))
        stormtroopers = input("Cantidad de Stormtroopers: ")
        if stormtroopers == "":
            stormtroopers = None
        else:
            stormtroopers = int(stormtroopers)
        operaciones.add((prioridad, encargado, descripcion, hora, stormtroopers))
        print("Operación añadida con éxito.")
    else:
        print("No hay más operaciones para atender.")


# e. realizar la atención de las operaciones de la cola;
while operaciones.elements:
    atender_operaciones(operaciones)

print()

# f. luego de atender la quinta operación, agregar una operación solicitada por capitán Phasma
# para revisión de intrusos en el hangar B7 que requiere 25 Stormstroopers;
operaciones.add((2, "Capitán Phasma", "Revisión de intrusos en el hangar B7", "19:00", 25))
print("Se ha añadido una operación de Capitán Phasma")

print()

#g. luego de atender la sexta operación, agregar una operación solicitada por el líder supremo
# Snoke para destruir el planeta Takodana.
operaciones.add((3, "Snoke", "Destrucción del planeta Takodana", "20:00", None))
print("Se ha añadido una operación del líder supremo Snoke.")
print()

