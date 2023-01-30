import datetime
import os
import pickle

import model.structures as structures
from view.view import get_employee_data, view_department_list


def init():
    if os.path.exists('employees.dat') and os.path.exists('department.dat') and os.path.exists('persons.dat'):
        with open('employees.dat', 'rb') as e:
            structures.employees = pickle.load(e)
        with open('department.dat', 'rb') as d:
            structures.departments = pickle.load(d)
        with open('persons.dat', 'rb') as p:
            structures.persons = pickle.load(p)


def get_next_id(file_name):
    if not os.path.exists(file_name):
        with open(file_name, 'w') as f:
            f.write('0')

    with open(file_name, 'r') as f:
        idx = int(f.read().strip())
        f.close()
        with open(file_name, 'w') as f:
            f.write(f'{idx + 1}')
        return idx + 1


def add_new_employee(data: dict):
    p = structures.Person(data['first_name'], data['last_name'], data['birth_at'])
    p_idx = get_next_id(structures.IDX_PERSON)
    structures.persons[p_idx] = p
    if data['dep_name'] not in structures.departments:
        d = structures.Department(data['dep_name'])
        structures.departments[data['dep_name']] = {}
        structures.departments[data['dep_name']]['dep'] = d
        structures.departments[data['dep_name']]['empls'] = []
    else:
        d = structures.departments[data['dep_name']]['dep']
    e = structures.Employee(p_idx, data['position'], d, data['profit'], datetime.date.today())
    e_idx = get_next_id(structures.IDX_EMPLOYEE)
    structures.employees[e_idx] = e
    structures.departments[data['dep_name']]['empls'].append(e_idx)
    with open('employees.dat', 'wb+') as e:
        with open('department.dat', 'wb+') as d:
            with open('persons.dat', 'wb+') as p:
                pickle.dump(structures.employees, e)
                pickle.dump(structures.departments, d)
                pickle.dump(structures.persons, p)


def get_all_employees():
    return structures.employees.values()


def get_department_list() -> list:
    return list(structures.departments.keys())


def get_employees_by_dep(dep_name: str) -> list | bool:
    if dep_name not in structures.departments:
        return False
    else:
        employees = []
        for i in structures.departments[dep_name]['empls']:
            employees.append(structures.employees[i])
        return employees


def get_person_by_id(idx):
    return structures.persons[idx]


if __name__ == '__main__':
    init()
    data = get_employee_data()
    add_new_employee(data)

    view_department_list(get_department_list())
    print(get_employees_by_dep(input('dep name - ')))
