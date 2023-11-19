from mesa import Agent


class Number(Agent):
    def __init__(self, unique_id, model, number):
        super().__init__(unique_id, model)
        self.number = number

        # Visualización
        self.path = ""
        self.layer = 2
        self.w = 1
        self.h = 1
