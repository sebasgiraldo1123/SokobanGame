import heapq


class UCS:
    def __init__(self, robot):
        self.robot = robot

    def search(self) -> list:
        grid = self.robot.model.grid
        start_x, start_y = self.robot.pos
        visited = set()
        self.counter = 0  # Contador que me da prioriodad a la cola
        # (cost, x, y, path) path = lista de pasos para llegar a la bandera
        queue = [(0, self.counter, start_x, start_y, [])]

        while queue:
            # heapq.heappop(queue) devuelve el elemento con menor costo
            cost, _, move_x, move_y, path = heapq.heappop(queue)

            if (move_x, move_y) in visited:
                continue

            visited.add((move_x, move_y))
            path = path + [(move_x, move_y)]

            cellmates = grid.get_cell_list_contents([(move_x, move_y)])
            if self.robot.verifyflag(cellmates):
                break

            for dx, dy in self.robot.directions:
                new_x, new_y = move_x + dx, move_y + dy
                cellmates = grid.get_cell_list_contents([(new_x, new_y)])
                if (self.robot.verifyWay(cellmates) or self.robot.verifyflag(cellmates)) and (new_x, new_y) not in visited:
                    # heapq.heappush agrega un elemento al heap y lo ordena de acuerdo a su costo
                    self.counter += 1
                    heapq.heappush(
                        queue, (cost + self.robot.valueStep, self.counter, new_x, new_y, path))
        return path
