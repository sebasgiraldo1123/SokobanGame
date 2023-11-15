from mesa import Agent


class Flag(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
