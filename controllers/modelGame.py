from mesa import Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation

from agents.bot import Bot
from agents.box import Box
from agents.flag import Flag
from agents.rock import Rock
from agents.way import Way


class ModelGame(Model):
    def __init__(self, data, route="", heuristic=""):
        self.data = data
        self.grid = MultiGrid(len(self.data[0]), len(self.data), True)

        # El planeador permite la gestión de los agentes y los coloca en el hilo donde se van a mover
        self.schedule = RandomActivation(self)
        self.running = True
        # Coloca el identificador de cada agente
        self.current_id = 0
        self.route = route
        self.heuristic = heuristic
        self.create_agents()

    # Pongo los agentes en el mundo grilla
    # Aquí se carga el mapa
    def create_agents(self):
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                self.current_id += 1
                if self.data[i][j] == "R":
                    newRock = Rock(self.current_id, self)
                    self.grid.place_agent(newRock, (j, i))
                    self.schedule.add(newRock)
                elif self.data[i][j] == "C":
                    newWay = Way(self.current_id, self)
                    self.grid.place_agent(newWay, (j, i))
                    self.schedule.add(newWay)
                elif self.data[i][j] == "M":
                    newObjetive = Flag(self.current_id, self)
                    self.grid.place_agent(newObjetive, (j, i))
                    self.schedule.add(newObjetive)
                else:
                    item = self.data[i][j].split("-")
                    for k in range(len(item)):
                        if item[k] == "C":
                            newWay = Way(self.current_id, self)
                            self.grid.place_agent(newWay, (j, i))
                            self.schedule.add(newWay)
                        elif item[k] == "a":
                            newRobot = Bot(self.current_id+100, self, self.route, self.heuristic)
                            self.grid.place_agent(newRobot, (j, i))
                            self.schedule.add(newRobot)
                        elif item[k] == "b":
                            newBox = Box(self.current_id+200, self)
                            self.grid.place_agent(newBox, (j, i))
                            self.schedule.add(newBox)

    # Ejecuta todos los métodos step de cada agente
    # Aquí se toma una foto del mundo en cada paso
    def step(self) -> None:
        self.schedule.step()

        # Para la simulación dado un condicional
        """
        if SokobanModel.bot_toca_bandera(self) > True:
            self.running = False
        """
