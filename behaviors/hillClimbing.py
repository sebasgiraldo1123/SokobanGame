from collections import deque


class HillClimbing:
    def __init__(self, root):
        self.root = root

    def search(self) -> list:
        if not self.root:
            return []

        result = []
        queue = deque()
        queue.append(self.root)

        while queue:
            current_node = queue.popleft()
            result.append(current_node.pos)  # Agregamos el valor del nodo a la lista de resultados

            # Expandir y ordenar los hijos por su heurística
            current_node.children.sort(key=lambda node: node.heuristic)
            best_child = current_node.children[0] if current_node.children else None

            if best_child and best_child.heuristic < current_node.heuristic:
                queue.append(best_child)  # Agregar al mejor hijo si mejora la heurística

        return result  # Dev
