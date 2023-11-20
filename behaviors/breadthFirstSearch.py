class BFS:
    def __init__(self, robot):
        self.robot = robot

    def search(self) -> list:
        grid = self.robot.model.grid
        start_x, start_y = self.robot.pos
        visited = set()
        queue = [(start_x, start_y)]
        steps = []  # Lista de pasos para la visualización de la ruta del bot

        while queue:
            move_x, move_y = queue.pop(0)
            if (move_x, move_y) not in visited:
                visited.add((move_x, move_y))
                cellmates = grid.get_cell_list_contents([(move_x, move_y)])

                steps.append((move_x, move_y))

                if self.robot.verifyflag(cellmates):
                    break

                for dx, dy in self.robot.directions:
                    new_x, new_y = move_x + dx, move_y + dy
                    cellmates = grid.get_cell_list_contents([(new_x, new_y)])
                    if self.robot.verifyWay(cellmates) or self.robot.verifyflag(cellmates):
                        queue.append((new_x, new_y))
        return steps
