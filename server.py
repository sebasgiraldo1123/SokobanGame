import mesa
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization import Choice
from mesa.visualization import StaticText
from mesa.visualization.modules import CanvasGrid

from controllers import canvasTools
from controllers.modelGame import ModelGame
from controllers.readGame import ReadData

data = ReadData("world_1.txt").read_data()
algorithm = ["", "BFS", "Beam Search", "Hill climbing"]

simulation_params = {
    "data": data,
    "algorithm": Choice(name="Selected algorithm",
                        value="",
                        choices=algorithm)
}
# Cada agente que se dibuja en el mundo grilla pasa por aquí y toma las características aquí definidas.

def agent_portrayal(agent):
    portrayal = {"Shape": agent.path,
                 "Layer": agent.layer,
                 "w": agent.w,
                 "h": agent.h,
                 # Coordenadas del agente
                 "text": f"{agent.pos[0]}, {agent.pos[1]}",
                 }
    return portrayal


rows = len(data)
columns = len(data[0])

canvas_height, canvas_width = canvasTools.calculate_canvas_dimensions(
    columns, rows, 600)

grid = CanvasGrid(agent_portrayal, columns, rows, canvas_width, canvas_height)
server = ModularServer(ModelGame, [grid], "Sokoban Game", model_params=simulation_params)
server.port = 8521
server.launch()
