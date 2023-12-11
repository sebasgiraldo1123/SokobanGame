class HillClimbing:
    def __init__(self, robot):
        # Inicializar con una instancia del robot.
        self.robot = robot

    def search(self) -> list:
        # Obtener la grilla del modelo y la posición inicial del robot.
        grid = self.robot.model.grid
        current_x, current_y = self.robot.pos

        # Lista para almacenar los pasos realizados durante la búsqueda.
        steps = [(current_x, current_y)]
        # Conjunto para registrar las celdas visitadas.
        visited = set([(current_x, current_y)])

        while True:
            best_heuristic = float('inf')
            next_step = None

            # Explorar los vecinos del nodo actual.
            for dx, dy in self.robot.directions:
                new_x, new_y = current_x + dx, current_y + dy
                # Verificar si la nueva celda es transitable y no ha sido visitada.
                cellmates = grid.get_cell_list_contents([(new_x, new_y)])
                if (new_x, new_y) not in visited and self.robot.verifyWay(cellmates):
                    # Calcular la heurística para el vecino.
                    heuristic = self.robot.get_heuristic(new_x, new_y)
                    # Seleccionar el vecino con la mejor heurística.
                    if heuristic < best_heuristic:
                        best_heuristic = heuristic
                        next_step = (new_x, new_y)

            # Si no se encuentra un mejor vecino, terminar la búsqueda.
            if next_step is None:
                break

            # Moverse al mejor vecino encontrado y actualizar la posición actual.
            current_x, current_y = next_step
            steps.append(next_step)
            visited.add(next_step)  # Añadir el nuevo nodo a los visitados.

        return steps
