import datetime
from animals import Animals


class Menu:
    def __init__(self):
        self.animals_methods = Animals()

    def menu_new_animal(self):
        self.animals_methods.get_list_command()
        return

    def menu_list_command(self):
        self.animals_methods.get_list_command()
        return

    def menu_new_command(self):
        pass
