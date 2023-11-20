import heapq

class BeamSearch:
    def __init__(self, robot):
        # Inicializa la clase con una referencia al robot.
        self.robot = robot

    def search(self) -> list:
        # Obtener la grilla del modelo y la posición inicial del robot.
        grid = self.robot.model.grid
        start_x, start_y = self.robot.pos

        # Conjunto para llevar un registro de las celdas visitadas.
        visited = set()
        # Cola de prioridad para los nodos, usando la heurística como clave de ordenamiento.
        queue = [(0, start_x, start_y, [])]  # Formato: (heurística, x, y, path)
        steps = []  # Para almacenar los pasos realizados durante la búsqueda.

        while queue:
            # Extraer el nodo con la mejor heurística.
            _, move_x, move_y, path = heapq.heappop(queue)

            # Si el nodo ya ha sido visitado, continúa con el siguiente.
            if (move_x, move_y) in visited:
                continue

            # Marcar el nodo como visitado y añadirlo al camino actual.
            visited.add((move_x, move_y))
            path = path + [(move_x, move_y)]
            steps.append((move_x, move_y))

            # Comprobar si se ha alcanzado la meta.
            cellmates = grid.get_cell_list_contents([(move_x, move_y)])
            if self.robot.verifyflag(cellmates):
                return steps, path  # Retorna los pasos si se alcanza la meta.

            # Explorar los vecinos del nodo actual.
            for dx, dy in self.robot.directions:
                new_x, new_y = move_x + dx, move_y + dy
                cellmates = grid.get_cell_list_contents([(new_x, new_y)])
                # Comprobar si el vecino es un camino válido y no ha sido visitado.
                if self.robot.verifyWay(cellmates) or self.robot.verifyflag(cellmates):
                    # Calcular la heurística para el vecino.
                    heuristic = self.robot.get_heuristic(new_x, new_y)
                    # Añadir el vecino a la cola de prioridad.
                    heapq.heappush(queue, (heuristic, new_x, new_y, path))

        return steps, path
