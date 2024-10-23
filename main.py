from menuClass import Menu


def menu():
    cl_menu = Menu()
    flag = True
    while flag:
        command = int(input(
            """
            Выберите номер пункта меню:
            1.Завести новое животное
            2.Список команд которые умеет выполнять животное
            3.Обучить животное новым командам
            0.Выход из программы
            """
        ))
        # 4.К-во животных определенного типа
        # 5.К-во животных определенного вида
        # 6.Общее к-во животных

        if command == 1:
            cl_menu.menu_new_animal()
        elif command == 2:
            cl_menu.menu_list_command()
        elif command == 3:
            cl_menu.menu_new_command()
        # elif command == 4:
        #     pass
        # elif command == 5:
        #     pass
        # elif command == 6:
            pass
        elif command == 0:
            flag = False
        else:
            print('Такой команды не существует, попробуйте еще раз')


if __name__ == '__main__':
    menu()
