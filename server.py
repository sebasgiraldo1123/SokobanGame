from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid

from controllers.model import SokobanModel


# Cada agente que se dibuja en el mundo grilla pasa por aquí y toma las características aquí definidas.
def agent_portrayal(agent):
    portrayal = {
        "Shape": agent.path,
        "Layer": agent.layer,
        "w": 1,
        "h": 1
    }
    return portrayal


num_row_width = 5
num_row_height = 7

grid = CanvasGrid(agent_portrayal, num_row_width, num_row_height, 650, 650)
server = ModularServer(SokobanModel, [grid], "Sokoban Model",
                       {"N": 1, "width": num_row_width, "height": num_row_height})
server.port = 8522
server.launch()
