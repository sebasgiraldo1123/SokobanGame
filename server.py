import mesa
from mesa.visualization.modules import CanvasGrid

from agents.bot import Bot
from agents.box import Box
from agents.flag import Flag
from agents.rock import Rock
from agents.way import Way
from controllers.modelGame import ModelGame
from controllers.readGame import ReadData

SIZE_OF_CANVAS_IN_PIXELS_X = 500
SIZE_OF_CANVAS_IN_PIXELS_Y = 500
FILE = "assets/data/file.txt"

data = ReadData(FILE).read_data()

simulation_params = {
    "data": data,
    "route": mesa.visualization.Choice(name="Informed and uninformed search algorithm",  value=" ", choices=["Selected Route", "BFS", "DFS", "UCS", "Beam Search", "Hill climbing", "A*"]),
    "heuristic": mesa.visualization.Choice(name="Heuristic", value=" ", choices=["Selected Heuristic", "Manhattan", "Euclidean"]),
}

# Cada agente que se dibuja en el mundo grilla pasa por aquí y toma las características aquí definidas.


def agent_portrayal(agent):
    portrayal = {"Shape": "assets/images/way.png",
                 "Layer": 0, "w": 1, "h": 1}
    if isinstance(agent, Rock):
        return {"Shape": "assets/images/rock.png", "Layer": 0, "w": 1, "h": 1}
    elif isinstance(agent, Way):
        return {"Shape": "assets/images/way.png", "Layer": 0, "w": 1, "h": 1}
    elif isinstance(agent, Bot):
        return {"Shape": "assets/images/bot.png", "Layer": 1, "w": 1, "h": 1}
    elif isinstance(agent, Box):
        return {"Shape": "assets/images/box.png", "Layer": 1, "w": 1, "h": 1}
    elif isinstance(agent, Flag):
        return {"Shape": "assets/images/flag.png", "Layer": 0, "w": 1, "h": 1}
    return portrayal


"""
def calculate_canvas_dimensions(num_columns, num_rows, max_height):
    # Calcula la altura de cada cuadro
    box_height = max_height / num_rows
    # Como los cuadros son simétricos, el ancho es igual al alto
    box_width = box_height
    # Calcula el ancho total del canvas
    width = box_width * num_columns

    return max_height, width


rows = 7
columns = 5
canvas_height, canvas_width = calculate_canvas_dimensions(columns, rows, 600)
print(canvas_width/columns)
print(canvas_height/rows)

grid = CanvasGrid(agent_portrayal, columns, rows, canvas_width, canvas_height)
server = ModularServer(SokobanModel, [grid], "Sokoban Model",
                       {"N": 1, "width": columns, "height": rows})
server.port = 8522
server.launch()
"""

grid = CanvasGrid(agent_portrayal, len(data[0]), len(data),
                  SIZE_OF_CANVAS_IN_PIXELS_X, SIZE_OF_CANVAS_IN_PIXELS_Y)

server = mesa.visualization.ModularServer(
    ModelGame, [grid], "Sokoban Game", model_params=simulation_params)
server.port = 8521
server.launch()

