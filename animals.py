import datetime
from homeAnimals import Cat, Dog, Hamster
from packAnimals import Camel, Donkey, Horse


class Animals:

    list_animals = []
    dict_animal_species = {
        'Кошка': Cat,
        'Собака': Dog,
        'Хомяк': Hamster,
        'Верблюд': Camel,
        'Осел': Donkey,
        'Лошадь': Horse
    }

    def add_animals(self, name, command, birthday, animal_species):
        while True:
            name = input('Введите кличку животного, с большой буквы:> ')
            if name.istitle() and name.isalpha():
                break
            print('Кличка должна начинаться с большой буквы и состоять из букв')
        command = input('Введите команды которые умеет животное, через запятую:>').split(',')

        while True:
            birthday_input = input('Введите дату дня рождения животного, формат dd-mm-yyyy:> ')
            try:
                birthday = datetime.datetime.strptime(birthday_input, "%d-%m-%Y")
                break
            except:
                print('Дата должна быть формат dd-mm-yyyy:> ')

        while True:
            animal_species = input('Напишите к какому виду относится животное: \n'
                                   'Кошка, Собака, Хомяк, Верблюд, Осел, Лошадь:> ')
            if animal_species.istitle() in self.dict_animal_species:
                animal_species = self.dict_animal_species[animal_species.istitle()]
                break
            print('Такого вида животного нет в списке попробуйте еще раз')

        self.list_animals.append(animal_species(name, command, birthday))

        print('Животное добавлено')
        return

    def get_list_command(self):
        data_animals = input('Введите вид животного (Кошка, Собака, Хомяк, Верблюд, Осел, Лошадь) и '
                                 'кличку что бы получить список команд (с большой буквы):> ').split()
        if data_animals[0] not in self.dict_animal_species:
            print('Такого вида животного нет в списке')
            return
        else:
            for animal in self.list_animals:
                if animal.get_name == data_animals[1]:
                    print(f'Список команд {animal.get_name}{", ".join(str(x) for x in animal.get_command())}')
                    return
            print('Животного с такой кличкой нет в списке')



    def add_command(self, name, command, birthday):
        pass
