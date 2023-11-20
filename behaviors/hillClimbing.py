class HillClimbing:
    def __init__(self, robot):
        self.robot = robot

    def search(self) -> list:
        # Obtener la posición inicial del robot
        current_x, current_y = self.robot.pos
        current_cost = self.robot.get_heuristic(current_x, current_y)
        steps = [(current_x, current_y)]

        while True:
            neighbors = self.get_neighbors(current_x, current_y)
            next_node = None
            next_cost = current_cost

            # Explorar los vecinos para encontrar una mejor solución
            for (nx, ny) in neighbors:
                cost = self.robot.get_heuristic(nx, ny)
                if cost < next_cost:
                    next_node = (nx, ny)
                    next_cost = cost

            # Si no se encuentra un mejor vecino, termina la búsqueda
            if next_node is None:
                break

            # Moverse al mejor vecino encontrado
            current_x, current_y = next_node
            current_cost = next_cost
            steps.append(next_node)

        return steps

    def get_neighbors(self, x, y):
        # Generar y devolver los vecinos de la posición actual
        grid = self.robot.model.grid
        neighbors = []
        for dx, dy in self.robot.directions:
            cellmates = grid.get_cell_list_contents([(x + dx, y + dy)])
            if self.robot.verifyWay(cellmates) or self.robot.verifyflag(cellmates):
                neighbors.append((x + dx, y + dy))
        return neighbors
