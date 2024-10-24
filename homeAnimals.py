from animals import Animals


class HomeAnimals(Animals):
    def __init__(self, name, command, birthday):
        super().__init__(name, command, birthday)


class Cat(HomeAnimals):
    def __init__(self, name, command, birthday):
        super().__init__(name, command, birthday)

    def __str__(self):
        return f'Вид животного: кошка, {super().__str__()}'


class Dog(HomeAnimals):
    def __init__(self, name, command, birthday):
        super().__init__(name, command, birthday)

    def __str__(self):
        return f'Вид животного: собака, {super().__str__()}'


class Hamster(HomeAnimals):
    def __init__(self, name, command, birthday):
        super().__init__(name, command, birthday)

    def __str__(self):
        return f'Вид животного: хомяк, {super().__str__()}'
