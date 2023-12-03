import heapq


class BeamSearch:
    def __init__(self, robot, beam_width=2):
        self.robot = robot
        self.beam_width = beam_width

    def search(self) -> list:
        grid = self.robot.model.grid
        start_x, start_y = self.robot.pos
        visited = set()
        self.counter = 0  # Contador que me da prioriodad a la cola
        queue = [(0, self.counter, 0, start_x, start_y)]
        steps = []

        while queue:
            # heapq.nsmallest devuelve los n elementos más pequeños de la lista
            queue = heapq.nsmallest(self.beam_width, queue)
            new_queue = []
            for _, _, cost, move_x, move_y in queue:
                if (move_x, move_y) in visited:
                    continue

                visited.add((move_x, move_y))
                steps.append((move_x, move_y))

                cellmates = grid.get_cell_list_contents([(move_x, move_y)])
                if self.robot.verifyflag(cellmates):
                    break

                for dx, dy in self.robot.directions:
                    new_x, new_y = move_x + dx, move_y + dy
                    if ((new_x >= 0 and new_x < self.robot.model._get_width()) and (new_y >= 0 and new_y < self.robot.model._get_height())):
                        cellmates = grid.get_cell_list_contents(
                            [(new_x, new_y)])
                        if (self.robot.verifyWay(cellmates) or self.robot.verifyflag(cellmates)) and (new_x, new_y) not in visited:
                            new_cost = cost + self.robot.valueStep
                            heuristic = self.robot.get_heuristic(
                                new_x, new_y)
                            fun_cost = new_cost + heuristic
                            self.counter += 1
                            new_queue.append(
                                (fun_cost, self.counter, new_cost, new_x, new_y))
            queue = new_queue

        return steps
