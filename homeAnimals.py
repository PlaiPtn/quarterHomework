from animals import Animals


class HomeAnimals(Animals):
    def __init__(self, name, command, birthday):
        super().__init__()
        self.__name = name
        self.__command = command
        self.__birthday = birthday


    def get_name(self):
        name = self.__name
        return name

    def get_command(self):
        command = self.__command
        return command


class Cat(HomeAnimals):
    def __init__(self, name, command, birthday):
        super().__init__(name, command, birthday)


class Dog(HomeAnimals):
    def __init__(self, name, command, birthday):
        super().__init__(name, command, birthday)


class Hamster(HomeAnimals):
    def __init__(self, name, command, birthday):
        super().__init__(name, command, birthday)
