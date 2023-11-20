from mesa import Agent
from controllers.canvasTools import  create_number_image


class Number(Agent):
    def __init__(self, unique_id, model, number):
        super().__init__(unique_id, model)
        self.number = number
        print(self.number)

        # Visualización
        self.path = "assets/images/number_" + str(self.number) + ".png"
        self.layer = 2
        self.w = 1
        self.h = 1

        # Crea la imagen del número
        create_number_image(self.number, self.path)

