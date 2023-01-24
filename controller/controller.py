import sqlite3

import model.model as m
import view.view as v


def main():
    cur, con = m.init()
    m.create_table(cur, con)
    while True:
        v.clear()
        value = v.main_menu()
        match value:
            case 'q' | 'quit' | 'й' | 'йгше':
                v.clear()
                exit()
            case '1':
                v.clear()
                v.view_result(m.select_all(cur))
                v.continue_question()
            case '2':
                filter_p = v.filter_input(value)
                v.view_result(m.select_by_filter(cur, filter_p, value))
                v.continue_question()
            case '3':
                filter_p = v.filter_input(value)
                v.view_result(m.select_by_filter(cur, filter_p, value))
                v.continue_question()
            case '4':
                while True:
                    try:
                        row = v.get_new_data()
                        m.add_row(cur, row, con)
                        break
                    except sqlite3.IntegrityError:
                        v.clear()
                        print('\nТакой номер уже существует.')
                        print('Повторите ввод.')

                print('\nНовая запись добавлена.\n')
                v.continue_question()
            case '5':
                idx = v.get_id()
                if idx.strip().isdigit():
                    m.delete_row(cur, con, idx)
                    print('Запись удалена.')
                    v.continue_question()
            case _:
                print("Неверный выбор!")
