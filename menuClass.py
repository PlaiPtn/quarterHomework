import datetime
from logics import Logics


class Menu:
    """
    Класс, который реализует пункты меню
    """
    def __init__(self):
        self.animals_methods = Logics()

    def menu_new_animal(self):
        self.animals_methods.add_animals()
        return

    def menu_list_command(self):
        self.animals_methods.get_list_command()
        return

    def menu_new_command(self):
        self.animals_methods.add_command()

    def menu_get_list_animals(self):
        self.animals_methods.get_list_animals()
