import math
from mesa import Agent
from agents.way import Way
from agents.flag import Flag

class Bot(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        # Visualización
        self.path = "assets/images/bot.png"
        self.layer = 3
        self.w = 0.8
        self.h = 0.8

        # Algoritmos
        self.route = []
        self.pos_goal = None
        self.walk = False
        self.lost = 0
        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # Se ejecuta en cada paso de la simulación
    def step(self) -> None:
        if self.pos_goal is not None and self.walk:
            self.move()

        # Si el bot se pierde se devuelve un paso
        if self.lost > 1:
            self.route = []
            self.route.append(self.pos)
            self.lost = 0

    # Mueve el bot un paso
    def move(self) -> None:
        pos = self.pos
        min_heuristic = 9999

        for dir in self.directions:
            new_pos = tuple(a + b for a, b in zip(self.pos, dir))
            if 0 <= new_pos[0] < self.model.grid.width and 0 <= new_pos[1] < self.model.grid.height and new_pos not in self.route:

                # 1 agente
                if len(self.model.grid.get_cell_list_contents(new_pos)) == 1:
                    # Es camino válido
                    if isinstance(self.model.grid.get_cell_list_contents(new_pos)[0], Way) or isinstance(self.model.grid.get_cell_list_contents(new_pos)[0], Flag):
                        new_pos_heuristic = self.get_heuristic(new_pos, self.pos_goal)
                        if new_pos_heuristic < min_heuristic:
                            min_heuristic = new_pos_heuristic
                            pos = new_pos

                        if new_pos_heuristic == 0:
                            pos = new_pos
                            self.walk = False
                            print("llegué !!!!")
                # No encuentra camino y no llegó, se perdió
                # me devuelvo un paso
                else:
                    self.lost += 1

        self.model.grid.move_agent(self, pos)
        self.route.append(pos)

    # Compara la heurística seleccionada y retorna el valor de la misma para la posición dada
    def get_heuristic(self, pos_a, pos_b) -> float:
        # return abs(pos_a[0] - pos_b[0]) + abs(pos_a[1] - pos_b[1])
        return math.sqrt((pos_a[0] - pos_b[0]) ** 2 + (pos_a[1] - pos_b[1]) ** 2)
