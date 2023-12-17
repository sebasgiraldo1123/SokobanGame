class BeamSearch:
    def __init__(self, root, beam_width):
        self.root = root
        self.beam_width = beam_width

    def search(self) -> list:
        if not self.root:
            return []

        result = []
        current_level = [self.root]

        while current_level:
            next_level = []

            # Ordenamos los nodos del nivel actual por su heurística de menor a mayor
            current_level.sort(key=lambda node: node.heuristic)

            # Tomamos los mejores nodos según el ancho del haz
            candidates = current_level[:self.beam_width]

            for node in candidates:
                result.append(node.pos)  # Agregamos el valor del nodo a la lista de resultados

                # Agregamos los hijos del nodo al próximo nivel
                next_level.extend(node.children)

            current_level = next_level

        return result  # Devolvemos la lista con los valores de los nodos visitados
