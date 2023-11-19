from mesa import Agent

from agents.flag import Flag
from agents.way import Way
from behaviors.breadthFirstSearch import BFS


class Bot(Agent):
    def __init__(self, unique_id, model, route, heuristic):
        super().__init__(unique_id, model)
        # Visualización
        self.path = "assets/images/bot.png"
        self.layer = 1
        self.w = 0.8
        self.h = 0.8
        self.route = route
        self.heuristic = heuristic
        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def step(self) -> None:
        self.perform_route()

    def perform_route(self):
        if self.route == "BFS":
            self.perform_bfs()
        elif self.route == "DFS":
            self.perform_dfs()
        elif self.route == "UCS":
            self.perform_ucs()
        elif self.route == "Beam Search":
            self.perform_beam_search()
        elif self.route == "Hill climbing":
            self.perform_hill_climbing()
        elif self.route == "A*":
            self.perform_a_star()

    def perform_bfs(self):
        BFS(self).search()

    def verifyWay(self, cellmates) -> bool:
        for agent in cellmates:
            if isinstance(agent, Way):
                return True
        return False

    def verifyflag(self, cellmates) -> bool:
        for agent in cellmates:
            if isinstance(agent, Flag):
                return True
        return False

    def move(self) -> None:
        print(self.path)
