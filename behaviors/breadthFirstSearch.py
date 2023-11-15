from agents.number import Number


class BFS:
    def __init__(self, robot):
        self.robot = robot

    def search(self):
        grid = self.robot.model.grid
        x, y = self.robot.pos
        visited = set()
        queue = [(x, y, 0)]

        while queue:
            x, y, depth = queue.pop(0)
            if (x, y) not in visited:
                visited.add((x, y))
                cellmates = grid.get_cell_list_contents([(x, y)])

                if depth != 0:
                    number_agent = Number(
                        self.robot.model.next_id(), self.robot.model, depth)
                    grid.place_agent(number_agent, (x, y))
                    self.robot.model.schedule.add(number_agent)

                print(f"step: {depth}: Move to ({x}, {y})")

                if self.robot.verifyflag(cellmates):
                    print("Found the flag")
                    break

                for dx, dy in self.robot.directions:
                    new_x, new_y = x + dx, y + dy
                    cellmates = grid.get_cell_list_contents([(new_x, new_y)])
                    if self.robot.verifyWay(cellmates) or self.robot.verifyflag(cellmates):
                        queue.append((new_x, new_y, depth + 1))
