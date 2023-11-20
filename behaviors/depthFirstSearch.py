class DFS:
    def __init__(self, robot):
        # Inicializar la clase con una instancia de robot
        self.robot = robot

    def search(self) -> list:
        # Obtener la grilla del modelo del robot
        grid = self.robot.model.grid
        # Obtener la posición inicial del robot
        start_x, start_y = self.robot.pos
        # Conjunto para registrar las celdas visitadas
        visited = set()
        # Usar una pila para gestionar los nodos a visitar
        stack = [(start_x, start_y)]
        # Lista para almacenar los pasos para visualización
        steps = []

        while stack:
            # Tomar la última posición añadida a la pila
            move_x, move_y = stack.pop()
            if (move_x, move_y) not in visited:
                # Marcar la posición actual como visitada
                visited.add((move_x, move_y))
                # Obtener los objetos en la celda actual
                cellmates = grid.get_cell_list_contents([(move_x, move_y)])
                # Añadir la posición actual a los pasos
                steps.append((move_x, move_y))
                # Verificar si la celda actual contiene la meta
                if self.robot.verifyflag(cellmates):
                    break

                # Iterar sobre las direcciones posibles
                for dx, dy in self.robot.directions:
                    new_x, new_y = move_x + dx, move_y + dy
                    # Obtener los objetos en la nueva celda
                    cellmates = grid.get_cell_list_contents([(new_x, new_y)])
                    # Verificar si la nueva celda es transitable y no ha sido visitada
                    if self.robot.verifyWay(cellmates) or self.robot.verifyflag(cellmates):
                        # Añadir la nueva posición a la pila para visitar después
                        stack.append((new_x, new_y))

        return steps