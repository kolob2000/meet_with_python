from model.model import init, add_new_employee, get_employees_by_dep, get_department_list, get_all_employees, \
    get_person_by_id
from view.view import get_employee_data, view_department_list, clear, main_menu, continue_question, success, \
    print_employees, get_dep_name


def main():
    init()
    while True:
        clear()
        value = main_menu()
        match value:
            case 'q' | 'quit' | 'й' | 'йгше':
                clear()
                exit()
            case '1':
                print_employees(get_all_employees(), get_person_by_id)
                continue_question()
            case '2':
                view_department_list(get_department_list())
                continue_question()
            case '3':
                dep_name = get_dep_name()
                print_employees(get_employees_by_dep(dep_name), get_person_by_id)
                continue_question()
            case '4':
                data = get_employee_data()
                add_new_employee(data)
                success()
                continue_question()
            case _:
                print("Неверный выбор!")
