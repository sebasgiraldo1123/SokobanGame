from mesa import Agent
from behaviors.breadthFirstSearch import BFS


class Bot(Agent):
    def __init__(self, unique_id, model, route_type, heuristic):
        super().__init__(unique_id, model)
        # Visualización
        self.path = "assets/images/bot.png"
        self.layer = 1
        self.route_type = route_type
        self.heuristic = heuristic

    def step(self) -> None:
        self.perform_route()

    def perform_route(self):
        if self.route_type == "BFS":
            self.perform_bfs()
        elif self.route_type == "DFS":
            self.perform_dfs()
        elif self.route_type == "UCS":
            self.perform_ucs()
        elif self.route_type == "Beam Search":
            self.perform_beam_search()
        elif self.route_type == "Hill climbing":
            self.perform_hill_climbing()
        elif self.route_type == "A*":
            self.perform_a_star()

    def perform_bfs(self):
        BFS(self).search()

    def veryfyWay(self, cellmates) -> bool:
        for agent in cellmates:
            if isinstance(agent, Way):
                return True
        return False
     
    def move(self) -> None:
        print(self.path)

