import heapq


class HillClimbing:
    def __init__(self, robot):
        self.robot = robot

    def search(self) -> list:
        grid = self.robot.model.grid
        start_x, start_y = self.robot.pos
        visited = set()
        self.count = 0
        queue = [(self.robot.get_heuristic(
            start_x, start_y), 0, self.count, start_x, start_y)]
        steps = []
        path = []

        while queue:
            _, depth, _, move_x, move_y = heapq.heappop(queue)
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
                        heuristic = self.robot.get_heuristic(new_x, new_y)
                        self.count += 1
                        heapq.heappush(
                            queue, (heuristic, depth+1, self.count, new_x, new_y))
                        path.append((new_x, new_y))

        return steps, path
