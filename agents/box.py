from mesa import Agent


class Box(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

        # Visualización
        self.path = "assets/images/box.png"
        self.layer = 1
        self.w = 0.8
        self.h = 0.8
