import mesa
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid

from agents.number import Number
from controllers import canvasTools
from controllers.modelGame import ModelGame
from controllers.readGame import ReadData

data = ReadData("file.txt").read_data()
routes = ["Select Routes", "BFS", "DFS", "UCS",
          "Beam Search", "Hill climbing", "A*"]
heuristics = ["Select Heuristic", "Manhattan", "Euclidean"]

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
    portrayal = {
        "Layer": agent.layer,
        "w": agent.w,
        "h": agent.h,
    }

    # Si el agente es una instancia de Number, agregar detalles de texto
    if isinstance(agent, Number):
        portrayal.update({
            # "Text": str(agent.number),  # Si quieres usar un atributo del agente
            "Text": str(1),
            "Text_color": "black",
            "Text_size": 12
        })
    else:
        # Para agentes que no son de tipo Number, definir la forma
        portrayal["Shape"] = agent.path

    return portrayal


rows = len(data)
columns = len(data[0])

canvas_height, canvas_width = canvasTools.calculate_canvas_dimensions(
    columns, rows, 600)

grid = CanvasGrid(agent_portrayal, columns, rows, canvas_width, canvas_height)
server = ModularServer(ModelGame, [grid], "Sokoban Game",
                       simulation_params)
server.port = 8521
server.launch()
