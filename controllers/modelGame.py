import itertools

from mesa import Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation

from agents.bot import Bot
from agents.box import Box
from agents.flag import Flag
from agents.rock import Rock
from agents.way import Way
from controllers.node import Node


class ModelGame(Model):
    def __init__(self, data, algorithm):
        self.data = data
        self.grid = MultiGrid(len(self.data[0]), len(self.data), True)

        # El planeador permite la gestión de los agentes y los coloca en el hilo donde se van a mover
        self.schedule = RandomActivation(self)
        self.running = False
        # Coloca el identificador de cada agente
        self.current_id = 0
        self.algorithm = algorithm
        # Robots, cajas y metas
        self.bots = []
        self.flags = []
        self.boxes = []
        self.routes = []
        # Arbol de búsqueda

        # Crea los agentes
        self.create_agents()
        # Encuentra la referencia los robots, banderas y cajas
        self.asign_agents()

        print(self.bots)
        print(self.flags)
        print(self.boxes)

    # Crea los agentes partiendo dela info en el archivo plano
    def create_agents(self) -> None:
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
                            newRobot = Bot(self.current_id + 1000, self)
                            self.grid.place_agent(newRobot, (j, i))
                            self.schedule.add(newRobot)
                        elif item[k] == "b":
                            newBox = Box(self.current_id + 2000, self, self.algorithm)
                            self.grid.place_agent(newBox, (j, i))
                            self.schedule.add(newBox)

    # Busca de izquierda hacia abajo los bots, cajas o banderas que existan y los almacena en vectores
    def asign_agents(self) -> None:
        rows = len(self.data)
        columns = len(self.data[0])

        for column in range(columns):
            for row in range(rows - 1, -1, -1):

                if self.data[row][column] == "M":
                    for agent in self.schedule.agents:
                        if agent.pos == (column, row):
                            self.flags.append(agent)

                elif self.data[row][column] == "C-a":
                    for agent in self.schedule.agents:
                        if agent.pos == (column, row) and not isinstance(agent, Way):
                            self.bots.append(agent)

                elif self.data[row][column] == "C-b":
                    for agent in self.schedule.agents:
                        if agent.pos == (column, row) and not isinstance(agent, Way):
                            self.boxes.append(agent)

        if len(self.bots) == len(self.boxes) and len(self.bots) == len(self.flags):
            # Le asigna a las cajas su respectiva bandera y genera sus árboles de búsqueda
            for i in range(len(self.boxes)):
                self.boxes[i].bot = self.bots[i]
                self.boxes[i].flag = self.flags[i]
                self.boxes[i].generate_tree_search()
        else:
            print("Error ------------------------- Deben existir el mismo número de bots, banderas y cajas")

    # Ejecuta todos los métodos step de cada agente
    # Aquí se toma una foto del mundo en cada paso
    def step(self) -> None:
        if self.algorithm is not "":
            self.running = True
        self.schedule.step()

    # Imprime un nodo por consola
    def print_grid(self, matriz) -> None:
        matriz = reversed(matriz)
        # Mostrar la matriz
        for fila in matriz:
            fila_str = ",   ".join(fila)
            print(fila_str)

    def show_grid(self):
        # Crear una matriz para representar el grid
        matriz = [["" for _ in range(self.grid.width)] for _ in range(self.grid.height)]

        for content_cell, pos in self.grid.coord_iter():
            if len(content_cell) == 1:
                agente = content_cell[0]
                if isinstance(agente, Way):
                    matriz[pos[1]][pos[0]] = "C"
                elif isinstance(agente, Rock):
                    matriz[pos[1]][pos[0]] = "R"
                elif isinstance(agente, Flag):
                    matriz[pos[1]][pos[0]] = "M"

            elif len(content_cell) == 2:
                agente1, agente2 = content_cell
                if isinstance(agente1, Way) and isinstance(agente2, Bot):
                    matriz[pos[1]][pos[0]] = "C-a"
                elif isinstance(agente1, Way) and isinstance(agente2, Box):
                    matriz[pos[1]][pos[0]] = "C-b"

        return matriz