from collections import deque

class BFS:
    def __init__(self, root):
        self.root = root

    def search(self) -> list:
        if not self.root:
            return []

        result = []
        queue = deque([self.root])  # Inicializamos una cola con el nodo raíz

        while queue:
            node = queue.popleft()  # Tomamos el primer nodo de la cola
            result.append(node.pos)  # Agregamos el valor del nodo a la lista de resultados
            if node.heuristic == 0:
                break

            # Agregamos los hijos del nodo a la cola para explorar en el siguiente nivel
            for child in node.children:
                queue.append(child)

        return result  # Devolvemos la lista con los valores de los nodos visitados
