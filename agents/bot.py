import math
from mesa import Agent
from behaviors.breadthFirstSearch import BFS
from behaviors.uniformCostSearch import UCS
from behaviors.astar import Astar
from agents.way import Way
from agents.flag import Flag
from agents.number import Number


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
        self.valueStep = 1

    # Se ejecuta en cada paso de la simulación

    def step(self) -> None:
        self.perform_route()

    # Ejecuta el algoritmo de búsqueda que se seleccionó
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
        steps = BFS(self).search()
        self.perform_step(steps)

    def perform_ucs(self):
        steps = UCS(self).search()
        self.perform_step(steps)

    def perform_a_star(self):
        steps, path = Astar(self).search()
        self.perform_step(path)

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

    # Captura el step del programa y recorre la lista resultante para crear los agentes número
    def perform_step(self, steps) -> None:
        numStep = self.model.schedule.steps + 1
        if numStep < len(steps):
            self.create_number_agent(numStep, steps[numStep])

    # Crea un agente número en la posición dada con step del recorrido
    def create_number_agent(self, depth, pos) -> None:
        number_agent = Number(
            self.model.next_id(), self, depth)
        self.model.grid.place_agent(number_agent, pos)
        self.model.schedule.add(number_agent)

    # Compara la heurística seleccionada y retorna el valor de la misma para la posición dada
    def get_heuristic(self, x, y) -> float:
        flag_x, flag_y = self.get_flag_position()
        if self.heuristic == "Manhattan":
            return abs(x - flag_x) + abs(y - flag_y)
        elif self.heuristic == "Euclidean":
            return math.sqrt((x - flag_x)**2 + (y - flag_y)**2)

    # Retorna la posición de la bandera
    def get_flag_position(self):
        for agent in self.model.schedule.agents:
            if isinstance(agent, Flag):
                return agent.pos
        return None
