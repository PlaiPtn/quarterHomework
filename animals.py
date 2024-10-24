class Animals:
    def __init__(self, name, command, birthday):
        self.__name = name
        self.__command = command
        self.__birthday = birthday

    def get_name(self):
        return self.__name

    def get_command(self):
        return self.__command

    def __str__(self):
        return f'Кличка: {self.__name}, Команды: {", ".join(self.__command)}, Дата рождения: {self.__birthday}'

