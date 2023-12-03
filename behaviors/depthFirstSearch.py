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
            if (move_x, move_y) in visited:
                continue
            visited.add((move_x, move_y))
            cellmates = grid.get_cell_list_contents([(move_x, move_y)])

            steps.append((move_x, move_y))
            if self.robot.verifyflag(cellmates):
                break

            self.robot.directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
            for dx, dy in self.robot.directions:
                new_x, new_y = move_x + dx, move_y + dy
                if ((new_x >= 0 and new_x < self.robot.model._get_width()) and (new_y >= 0 and new_y < self.robot.model._get_height())):
                    cellmates = grid.get_cell_list_contents(
                        [(new_x, new_y)])
                    if self.robot.verifyWay(cellmates) or self.robot.verifyflag(cellmates):
                        stack.append((new_x, new_y))

        return steps
