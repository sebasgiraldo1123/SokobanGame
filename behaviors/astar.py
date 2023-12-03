import heapq


class Astar:
    def __init__(self, robot):
        self.robot = robot

    def search(self) -> list:
        grid = self.robot.model.grid
        start_x, start_y = self.robot.pos
        visited = set()
        self.counter = 0  # Contador que me da prioriodad a la cola
        queue = [(0, self.counter, 0, start_x, start_y)]
        steps = []
        path = []

        while queue:
            _, _, cost, move_x, move_y = heapq.heappop(queue)

            if (move_x, move_y) in visited:
                continue

            visited.add((move_x, move_y))
            path.append((move_x, move_y))

            cellmates = grid.get_cell_list_contents([(move_x, move_y)])
            if self.robot.verifyflag(cellmates):
                break

            for dx, dy in self.robot.directions:
                new_x, new_y = move_x + dx, move_y + dy
                if ((new_x >= 0 and new_x < self.robot.model._get_width()) and (new_y >= 0 and new_y < self.robot.model._get_height())):
                    cellmates = grid.get_cell_list_contents(
                        [(new_x, new_y)])
                    if (self.robot.verifyWay(cellmates) or self.robot.verifyflag(cellmates)) and (new_x, new_y) not in visited:
                        # Costo de llegar a la celda
                        new_cost = cost + self.robot.valueStep
                        # Heuristica de la celda
                        heuristic = self.robot.get_heuristic(new_x, new_y)
                        # Costo total de llegar a la celda
                        fun_cost = new_cost + heuristic
                        # heapq.heappush agrega un elemento al heap y lo ordena de acuerdo a su costo
                        self.counter += 1
                        heapq.heappush(
                            queue, (fun_cost, self.counter, new_cost, new_x, new_y))
                        # Guarda los pasos de expansión del robot
                        steps.append((new_x, new_y))
        return steps, path
