from collections import deque
import pydot
from agents.bot import Bot
from behaviors.breadthFirstSearch import BFS
from behaviors.beamSearch import BeamSearch
from behaviors.hillClimbing import HillClimbing
import math
from mesa import Agent
from agents.flag import Flag
from agents.way import Way
from controllers.node import Node


class Box(Agent):
    def __init__(self, unique_id, model, algorithm):
        super().__init__(unique_id, model)

        # Visualización
        self.path = "assets/images/box.png"
        self.layer = 1
        self.w = 0.8
        self.h = 0.8

        # Algoritmos
        self.algorithm = algorithm
        self.bot = None
        self.flag = None
        self.route = []
        self.walk = False
        self.root = None
        self.expanded = []
        self.directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        self.next_step = 1
        self.req_bot_pos = None

    # Se ejecuta en cada paso de la simulación
    def step(self) -> None:
        # Si el robot existe y hay una ruta para la caja
        if len(self.route) > 0 and self.bot is not None:
            # Siempre se mueve hacia la caja
            self.move_bot()
            # Si el robot está ubicado da un paso
            self.move_box()

    # Crea la ruta con el algoritmo asignado
    def create_route(self):
        if self.algorithm == "BFS":
            self.route = BFS(self.root).search()
            print("BFS ", self.route)
        elif self.algorithm == "Beam Search":
            self.route = BeamSearch(self.root, 3).search()
            print("Beam Search ", self.route)
        elif self.algorithm == "Hill climbing":
            self.route = HillClimbing(self.root).search()
            print("Hill Climbing ", self.route)
        else:
            print("Seleccione un algoritmo")

    # Crear el árbol de búsqueda
    def create_tree_search(self):
        queue = deque([self.root])
        self.expanded = set()  # Usar un conjunto para un acceso más eficiente
        self.expanded.add(self.root.pos)

        while queue:
            node = queue.popleft()

            if node.heuristic == 0:
                print("Arbol creado, bandera en", node.pos)
                graph = self.add_nodes_edges(self.root)
                graph.write_png("assets/images/Tree" + f"{self.root.pos}" + ".png")
                self.create_route()

            else:
                for dir in self.directions:
                    new_pos = tuple(a + b for a, b in zip(node.pos, dir))

                    if (0 <= new_pos[0] < self.model.grid.width and
                            0 <= new_pos[1] < self.model.grid.height and
                            new_pos not in self.expanded):
                        neighbor = self.model.grid.get_cell_list_contents(new_pos)

                        if isinstance(neighbor[0], Way) or isinstance(neighbor[0], Flag):
                            new_node = Node(new_pos, self.get_heuristic(new_pos, self.flag.pos))
                            node.append_child(new_node)
                            queue.append(new_node)
                            self.expanded.add(new_pos)

    # inicia la creación del arbol de búsqueda
    def generate_tree_search(self):
        if self.bot is not None and self.flag is not None:
            self.root = Node(self.pos, self.get_heuristic(self.pos, self.flag.pos))
            self.create_tree_search()

    # Compara la heurística seleccionada y retorna el valor de la misma para la posición dada
    def get_heuristic(self, pos_a, pos_b) -> float:
        return abs(pos_a[0] - pos_b[0]) + abs(pos_a[1] - pos_b[1])
        # return math.sqrt((pos_a[0] - pos_b[0]) ** 2 + (pos_a[1] - pos_b[1]) ** 2)

    # Genera el gráfico del árbol de búsqueda
    def add_nodes_edges(self, tree, graph=None):
        if graph is None:
            graph = pydot.Dot(graph_type='graph', rankdir="TB")

        for child in tree.children:
            parent_name = f"{tree.pos}, {tree.heuristic}"
            child_name = f"{child.pos}, {child.heuristic}"
            edge = pydot.Edge(parent_name, child_name)
            graph.add_edge(edge)
            self.add_nodes_edges(child, graph)

        return graph

    # Mueve el bot hacia la posición deseada para la caja
    def move_bot(self):
        actual_pos = self.pos

        if self.flag.pos != self.pos:
            next_pos = self.route[self.route.index(actual_pos) + 1]
            self.req_bot_pos = tuple(a + (n - a) * -1 for a, n in zip(actual_pos, next_pos))
        else:
            self.req_bot_pos = self.route[len(self.route) - 2]
            print("Caja en bandera, terminé !!!!")

        if self.req_bot_pos != self.bot.pos:
            self.bot.pos_goal = self.req_bot_pos
            self.bot.walk = True

    # Mueve la caja
    def move_box(self):
        back_neighbor = self.model.grid.get_cell_list_contents(self.req_bot_pos)

        # Si el bot está atrás y no ha llegado a la meta mueve la caja
        if len(back_neighbor) == 2 and isinstance(back_neighbor[1], Bot) and self.flag.pos != self.pos:
            self.model.grid.move_agent(self, self.route[self.next_step])
            self.next_step += 1
            self.move_bot()
