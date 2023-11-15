from mesa import Agent


class Bot(Agent):
    def __init__(self, unique_id, model, route, heuristic):
        super().__init__(unique_id, model)

        # Visualización
        self.path = "assets/images/bot.png"
        self.layer = 1
        self.route = route
        self.heuristic = heuristic

    def step(self) -> None:
        self.move()

    def move(self) -> None:
        print(self.path)