from mesa import Agent


class Way(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

        # Visualización
        self.path = "assets/images/way.png"
        self.layer = 0
