import mesa
from mesa.visualization.modules import CanvasGrid
from mesa_viz_tornado.ModularVisualization import ModularServer

from controllers import canvasTools
from controllers.modelGame import ModelGame
from controllers.readGame import ReadData

data = ReadData("file.txt").read_data()

simulation_params = {
    "data": data,
    "route": mesa.visualization.Choice(
        name="Informed and uninformed search algorithm",
        value="BFS",
        choices=["BFS", "DFS", "UCS", "Beam Search", "Hill climbing", "A*"]
    ),
    "heuristic": mesa.visualization.Choice(
        name="Heuristic",
        value="Manhattan",
        choices=["Manhattan", "Euclidean"]),
}

# Cada agente que se dibuja en el mundo grilla pasa por aquí y toma las características aquí definidas.

def agent_portrayal(agent):
    portrayal = {"Shape": agent.path,
                 "Layer": agent.layer,
                 "w": agent.w,
                 "h": agent.h,
                 }
    return portrayal


rows = len(data)
columns = len(data[0])

canvas_height, canvas_width = canvasTools.calculate_canvas_dimensions(columns, rows, 600)

grid = CanvasGrid(agent_portrayal, columns, rows, canvas_width, canvas_height)
server = ModularServer(ModelGame, [grid], "Sokoban Game",
                       simulation_params)
server.port = 8521
server.launch()
