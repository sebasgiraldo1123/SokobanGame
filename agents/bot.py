from mesa import Agent


class Bot(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

        # Borrar
        self.wealth = 1

        # Visualización
        self.path = "assets/images/bot.png"
        self.layer = 0

    def step(self) -> None:
        self.move()
        # si no encuentra la bandera se sigue moviendo
        if self.wealth > 0:
            self.give_money()

    def give_money(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        if len(cellmates) > 1:
            other = self.random.choice(cellmates)
            other.wealth += 1
            self.wealth -= 1

    def move(self) -> None:

        # Orden = abajo, izquierda, arriba, derecha, ojo que cuando está en los bordes escoge el reflejo,
        # Tiene la posibilidad de devolver no solo la posición sino también el tipo de agente que está ahí.
        # Crea un método que detecte esto y elimine de las tuplas este error.
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=False, include_center=False
        )
        print("actual "+str(self.pos)+" posibles pasos "+str(possible_steps))
        # aquí se escoge de forma aleatoria cual paso va a tomar
        new_position = self.random.choice(possible_steps)

        # La estrategía se debe llamar aquí para tomar la decisión de adonde moverse
        self.model.grid.move_agent(self, new_position)
