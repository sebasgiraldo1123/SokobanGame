from mesa import Model
from agents.bot import Bot
from mesa.time import RandomActivation
from mesa.space import MultiGrid


class SokobanModel(Model):
    def __init__(self, N, width, height):
        self.num_agents = N
        self.grid = MultiGrid(width, height, True)

        # El planeador permite la gestión de los agentes y los coloca en el hilo donde se van a mover
        self.schedule = RandomActivation(self)

        # Pongo los agentes en el mundo grilla
        # Aquí se carga el mapa
        for i in range(self.num_agents):
            newAgent = Bot(i, self)
            self.schedule.add(newAgent)
            # Coordenadas xy iniciales
            # x = self.random.randrange(self.grid.width)
            # y = self.random.randrange(self.grid.height)
            self.grid.place_agent(newAgent, (1, 1))

    # Ejecuta todos los métodos step de cada agente
    # Aquí se toma una foto del mundo en cada paso
    def step(self) -> None:
        self.schedule.step()

        # Para la simulación dado un condicional
        """
        if SokobanModel.bot_toca_bandera(self) > True:
            self.running = False
        """

