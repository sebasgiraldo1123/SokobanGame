import heapq

class BeamSearch:
    def __init__(self, robot, beam_width):
        self.robot = robot
        self.beam_width = beam_width  # Ancho del haz

    def search(self) -> list:
        grid = self.robot.model.grid
        start_x, start_y = self.robot.pos
        visited = set()
        # Cola de prioridad inicializada con la posición inicial
        queue = [(0, start_x, start_y, [])]  # (costo, x, y, path)
        steps = []

        while queue:
            next_level = []

            # Expandir los nodos en la cola actual
            while queue:
                cost, move_x, move_y, path = heapq.heappop(queue)
                if (move_x, move_y) in visited:
                    continue

                visited.add((move_x, move_y))
                path = path + [(move_x, move_y)]
                steps.append((move_x, move_y))

                cellmates = grid.get_cell_list_contents([(move_x, move_y)])
                if self.robot.verifyflag(cellmates):
                    return steps, path  # Retorna los pasos y el camino al encontrar la meta

                for dx, dy in self.robot.directions:
                    new_x, new_y = move_x + dx, move_y + dy
                    if (new_x, new_y) not in visited:
                        new_cost = cost + self.robot.valueStep
                        next_level.append((new_cost, new_x, new_y, path))

            # Seleccionar los 'beam_width' mejores nodos para continuar la búsqueda
            # Ordenar los nodos por costo y seleccionar los primeros 'beam_width'
            queue = sorted(next_level, key=lambda node: node[0])[:self.beam_width]

        return steps, path
