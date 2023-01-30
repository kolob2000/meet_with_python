import os

from model.structures import Employee, Person


def clear():
    os.system('cls') if os.name == 'nt' else os.system('clear')


def get_dep_name():
    return input('Введите название отдела - ')


def get_employee_data() -> dict:
    first_name: str = input('Имя - ')
    last_name: str = input('Фамилия - ')
    birth_at: list = list(map(int, input('Дата рождения: гггг-мм-дд - ').replace(' ', '').split('-')))
    dep_name: str = input('Название отдела - ')
    position: str = input('Должность - ')
    profit: float = float(input('Оклад - '))
    return {
        'first_name': first_name,
        'last_name': last_name,
        'birth_at': birth_at,
        'dep_name': dep_name,
        'position': position,
        'profit': profit
    }


def view_department_list(dep_list: list):
    for i, dep in enumerate(dep_list, 1):
        print(f'{i}. {dep}')


def continue_question():
    print('Для возврата в главное меню нажмите Enter. Выход q/quit. - ', end='')
    value = input().strip().lower()
    match value:
        case 'q' | 'quit' | 'й' | 'йгше':
            clear()
            exit()


def success():
    print('Операция успешно выполнена.')


def print_employees(employees: list[Employee], cb_get_person_by_id):
    for e in employees:
        p: Person = cb_get_person_by_id(e.person_idx)
        print(f'Номер: {e.person_idx} Имя: {p.first_name} '
              f'Фамилия: {p.last_name} Год рождения: {p.birth_at[0]} '
              f'Должность: {e.position} '
              f'Отдел: {e.department.name} Оклад: {e.profit} Нанят с: {e.hired_from}')


def main_menu():
    print('__________ База персонала __________\n')
    print('__________ ВВЕДИТЕ КОМАНДУ __________')
    print(
        '1 - вывести всех служащих. 2. вывести список отделов.\n'
        '3 - фильтровать по отделу. 4 - добавить сотрудника.  q/quit - выход.')
    return input().strip().lower()
