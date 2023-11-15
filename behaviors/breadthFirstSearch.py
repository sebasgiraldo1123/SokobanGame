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

                if not self.robot.veryfyWay(cellmates):
                    continue
