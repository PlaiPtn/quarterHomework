import datetime
from homeAnimals import Cat, Dog, Hamster
from packAnimals import Camel, Donkey, Horse
from counter import Counter


class Logics:
    """
    Логика действий пунктов меню
    """
    def __init__(self):
        self.count = Counter()
        self.list_animals = []
        self.dict_animal_species = {
            'Кошка': Cat,
            'Собака': Dog,
            'Хомяк': Hamster,
            'Верблюд': Camel,
            'Осел': Donkey,
            'Лошадь': Horse
        }

    def check_animal_species(self, animal_species):
        if animal_species.strip().title() in self.dict_animal_species:
            return True
        else:
            return False

    def add_animals(self):
        """
        Функция добавления нового животного
        :return:
        """
        with self.count as count:
            while True:
                animal_species = input('Напишите к какому виду относится животное: \n'
                                       'Кошка, Собака, Хомяк, Верблюд, Осел, Лошадь:> ')
                if self.check_animal_species(animal_species):
                    animal_species = self.dict_animal_species[animal_species.strip().title()]
                    break
                print('Такого вида животного нет в списке попробуйте еще раз')

            while True:
                name = input('Введите кличку животного, с большой буквы:> ')
                if name.istitle() and name.isalpha():
                    break
                print('Кличка должна начинаться с большой буквы и состоять из букв')
            command = input('Введите команды которые умеет животное, через пробел:> ').split()

            while True:
                birthday_input = input('Введите дату дня рождения животного, формат dd-mm-yyyy:> ')
                try:
                    birthday = datetime.datetime.strptime(birthday_input, "%d-%m-%Y")
                    break
                except Exception:
                    print('Дата должна быть формат dd-mm-yyyy:> ')
            if all([bool(name), bool(command), bool(birthday)]):
                self.list_animals.append(animal_species(name.strip(), command, birthday))
                print(count.add())
                print('Животное добавлено')
            return

    def get_list_command(self):
        """
        Функция, выводит команды, которые умеет конкретное животное
        :return:
        """
        animal_species = input('Введите вид животного чьи навыки хотим посмотреть '
                               '(Кошка, Собака, Хомяк, Верблюд, Осел, Лошадь):> ')
        if not self.check_animal_species(animal_species):
            print('Такого вида животного нет в списке')
            return
        else:
            name = input('Введите кличку (с большой буквы):> ')
            for animal in self.list_animals:
                if animal.get_name() == name.title():
                    print(f'Список команд {animal.get_name()}: {", ".join(str(x) for x in animal.get_command())}')
                    return
            print('Животного с такой кличкой нет в списке')
            return

    def add_command(self):
        """
        Функция изучения новых команд животному
        :return:
        """
        animal_species = input('Введите вид животного которое хотим обучить '
                               '(Кошка, Собака, Хомяк, Верблюд, Осел, Лошадь):> ')
        if not self.check_animal_species(animal_species):
            print('Такого вида животного нет в списке')
            return
        else:
            name = input('Введите кличку (с большой буквы):> ')
            for animal in self.list_animals:
                if animal.get_name() == name.title():
                    new_command = input('Введите команды через пробел которыми хотите обучить:> ').split()
                    old_commands = animal.get_command()
                    for command in new_command:
                        if command in old_commands:
                            print(f'Такой команде животное {animal.get_name()} уже обучено')
                        else:
                            old_commands.append(command)
                            print(f'Животное {animal.get_name()} обучено команде {command}')
                    return
            print('Животного с такой кличкой нет в списке')
            return

    def get_list_animals(self):
        """
        Функция, которая выводит на экран список всех животных
        :return:
        """
        for animal in self.list_animals:
            print(animal)
        return


