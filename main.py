from menuClass import Menu


def menu():
    """
    Основное меню
    :return:
    """
    cl_menu = Menu()
    flag = True
    while flag:
        command = input(
            "Выберите номер пункта меню:\n1.Завести новое животное\n2.Список команд которые умеет выполнять животное\n"
            "3.Обучить животное новым командам\n4.Вывести список всех животных\n0.Выход из программы\n:> "
        )

        if command == '1':
            cl_menu.menu_new_animal()
        elif command == '2':
            cl_menu.menu_list_command()
        elif command == '3':
            cl_menu.menu_new_command()
        elif command == '4':
            cl_menu.menu_get_list_animals()
        elif command == '0':
            flag = False
        else:
            print('Такой команды не существует, попробуйте еще раз')


if __name__ == '__main__':
    menu()
