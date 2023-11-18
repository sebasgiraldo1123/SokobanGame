from mesa import Agent


class Flag(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

        # Visualización
        self.path = "assets/images/flag.png"
        self.layer = 1
        self.w = 1
        self.h = 1
        self.pos
