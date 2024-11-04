class BinaryTree:

    class __Node:
        def __init__(self, value, left=None, right=None, other_value=None, description="", captured_by=None):
            self.value = value
            self.left = left
            self.right = right
            self.other_value = other_value
            self.height = 0
            self.description = description
            self.captured_by = captured_by

    def __init__(self):
        self.root = None

    def height(self, root):
        if root is None:
            return -1
        else:
            return root.height

    def update_height(self, root):
        if root is not None:
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            root.height = max(left_height, right_height) + 1

    def simple_rotation(self, root, control):
        if control:
            aux = root.left
            root.left = aux.right
            aux.right = root
        else:
            aux = root.right
            root.right = aux.left
            aux.left = root
        self.update_height(root)
        self.update_height(aux)
        root = aux
        return root

    def double_rotation(self, root, control):
        if control:
            root.left = self.simple_rotation(root.left, False)
            root = self.simple_rotation(root, True)
        else:
            root.right = self.simple_rotation(root.right, True)
            root = self.simple_rotation(root, False)
        return root

    def balancing(self, root):
        if root is not None:
            if self.height(root.left) - self.height(root.right) == 2:
                if self.height(root.left.left) >= self.height(root.left.right):
                    root = self.simple_rotation(root, True)
                else:
                    root = self.double_rotation(root, True)
            elif self.height(root.right) - self.height(root.left) == 2:
                if self.height(root.right.right) >= self.height(root.right.left):
                    root = self.simple_rotation(root, False)
                else:
                    root = self.double_rotation(root, False)
        return root

    def insert_node(self, value, other_value=None, description="", captured_by=None):
        def __insert(root, value, other_value=None, description="", captured_by=None):
            if root is None:
                return BinaryTree.__Node(value, other_value=other_value, description=description, captured_by=captured_by)
            elif value < root.value:
                root.left = __insert(root.left, value, other_value, description, captured_by)
            else:
                root.right = __insert(root.right, value, other_value, description, captured_by)
            root = self.balancing(root)
            self.update_height(root)
            return root

        self.root = __insert(self.root, value, other_value, description, captured_by)

    def search(self, key):
        def __search(root, key):
            if root is not None:
                if root.value == key:
                    return root
                elif key < root.value:
                    return __search(root.left, key)
                else:
                    return __search(root.right, key)
        return __search(self.root, key) if self.root is not None else None

    def preorden(self):
        def __preorden(root):
            if root is not None:
                print(f'Nombre: {root.value}, Descripción: {root.description}, Capturado por: {root.captured_by}')
                __preorden(root.left)
                __preorden(root.right)

        if self.root is not None:
            __preorden(self.root)

   

    def inorder(self):
        def __inorder(root):
            if root is not None:
                __inorder(root.left)
                print(f'Nombre: {root.value}, Descripción: {root.description}, Capturado por: {root.captured_by}')
                __inorder(root.right)

        if self.root is not None:
            __inorder(self.root)

    def modify_node(self, name, description=None, captured_by=None):
        node = self.search(name)
        if node:
            if description is not None:
                node.description = description
            if captured_by is not None:
                node.captured_by = captured_by

    def delete_node(self, value):
        def __delete(root, value):
            if root is None:
                return root
            elif value < root.value:
                root.left = __delete(root.left, value)
            elif value > root.value:
                root.right = __delete(root.right, value)
            else:
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                temp = self.get_minimum(root.right)
                root.value = temp.value
                root.right = __delete(root.right, temp.value)
            root = self.balancing(root)
            self.update_height(root)
            return root
        
        self.root = __delete(self.root, value)

    def get_minimum(self, root):
        while root.left is not None:
            root = root.left
        return root

    def list_by_level(self):
        if self.root is None:
            return []

        levels = []
        queue = [(self.root, 0)]
        
        while queue:
            node, level = queue.pop(0)
            if level == len(levels):
                levels.append([])
            levels[level].append(node.value)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        
        for i, level in enumerate(levels):
            print(f"Nivel {i}: {', '.join(level)}")
    

    def captured_by(self, hero):
        def __captured_by(root):
            if root is not None:
                if root.captured_by == hero:
                    print(f'Nombre: {root.value}, Descripción: {root.description}')
                __captured_by(root.left)
                __captured_by(root.right)

        __captured_by(self.root)


tree = BinaryTree()


creatures_data = [
    ("Ceto", ""),
    ("Tifón", "Gigante de las tormentas"),
    ("Equidna", "Madre de todas las criaturas"),
    ("Dino", ""),
    ("Pefredo", ""),
    ("Enio", ""),
    ("Escila", ""),
    ("Caribdis", ""),
    ("Euríale", ""),
    ("Águila del Cáucaso", ""),
    ("Quimera", ""),
    ("Hidra de Lerna", ""),
    ("León de Nemea", ""),
    ("Esfinge", ""),
    ("Dragón de la Cólquida", ""),
    ("Cerbero", ""),
    ("Jabalí de Erimanto", ""),
    ("Cerda de Cromión", ""),
    ("Toro de Creta", ""),
    ("Minotauro de Creta", ""),
    ("Medusa", ""),
    ("Ladón", ""),
    ("Aves del Estínfalo", ""),
    ("Sirenas", ""),
    ("Basilisco", ""),
    ("Talos", "Guardia de Creta"),
    ("Pitón", ""),
    ("Cierva de Cerinea", ""),
    ("Argos Panoptes", ""),
    ("Jabalí de Calidón", "")
]

for creature in creatures_data:
    tree.insert_node(creature[0], description=creature[1])


tree.modify_node("Cerbero", captured_by="Heracles")
tree.modify_node("Toro de Creta", captured_by="Heracles")
tree.modify_node("Cierva Cerinea", captured_by="Heracles")
tree.modify_node("Jabalí de Erimanto", captured_by="Heracles")
tree.modify_node("Ladón", "Dragón Ladón")
tree.modify_node("Aves del Estínfalo", "Derrotadas por Heracles")


print()
print("Listado en orden:")
tree.inorder()

print()
print("Listado por niveles:")
tree.list_by_level()

print()
print("Criaturas capturadas por Heracles:")
tree.captured_by("Heracles")


tree.delete_node("Basilisco")
tree.delete_node("Sirenas")


print()
tree.inorder()


