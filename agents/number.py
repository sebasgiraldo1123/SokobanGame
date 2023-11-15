from mesa import Agent


class Number(Agent):
    def __init__(self, unique_id, model, number):
        super().__init__(unique_id, model)
        self.number = number
