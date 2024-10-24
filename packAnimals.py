from animals import Animals


class PackAnimals(Animals):
    def __init__(self, name, command, birthday):
        super().__init__(name, command, birthday)


class Camel(PackAnimals):
    def __init__(self, name, command, birthday):
        super().__init__(name, command, birthday)

    def __str__(self):
        return f'Вид животного: верблюд, {super().__str__()}'


class Donkey(PackAnimals):
    def __init__(self, name, command, birthday):
        super().__init__(name, command, birthday)

    def __str__(self):
        return f'Вид животного: осел, {super().__str__()}'


class Horse(PackAnimals):
    def __init__(self, name, command, birthday):
        super().__init__(name, command, birthday)

    def __str__(self):
        return f'Вид животного: лошадь, {super().__str__()}'
