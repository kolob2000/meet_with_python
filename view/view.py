import os


def clear():
    os.system('cls') if os.name == 'nt' else os.system('clear')


def continue_question():
    print('Для возврата в главное меню нажмите Enter. Выход q/quit. - ', end='')
    value = input().strip().lower()
    match value:
        case 'q' | 'quit' | 'й' | 'йгше':
            clear()
            exit()


def view_result(res):
    result = res.fetchall()
    if len(result) == 0:
        print('Записей нет.')
    else:
        print('\nРезультат: \n')
        for i in result:
            print(i)
        print()


def filter_input(value):
    return input(f'Введите {"фамилию/имя" if value == "2" else "город"} - ').strip().lower()


def get_id():
    while True:
        idx = input('Введите id записи или q для отмены - ')
        if idx.strip().isdigit() or idx.lower().strip() == 'q' or idx.lower().strip() == 'й':
            return idx
        print('Не верный ввод. Повторите.')


def get_new_data() -> dict:
    row = {'name': '', 'phone': '', 'city': ''}
    while not row['name']:
        row['name'] = input('Введите имя/фамилию (поле не может быть пустым) - ')
    while not row['phone']:
        row['phone'] = input('Введите номер телефона (поле не может быть пустым) - ')

        row['city'] = input('Введите номер город (необязательное поле - ')

    return row


def main_menu():
    print('__________ ТЕЛЕФОННЫЙ СПРАВОЧНИК __________\n')
    print('__________ ВВЕДИТЕ КОМАНДУ __________')
    print('1 - вывести все записи. 2 - фильтровать по имени/фамилии. 3 - фильтровать по городу. '
          '4 - добавить новую запись. 5 - удалить запись по id.  q/quit - выход.')
    return input().strip().lower()
