import datetime
from dataclasses import dataclass

IDX_PERSON = 'idx_p.txt'
IDX_EMPLOYEE = 'idx_e.txt'
IDX_DEPARTMENT = 'idx_d.txt'


@dataclass
class Person:
    first_name: str
    last_name: str
    birth_at: datetime.date


@dataclass
class Department:
    name: str


@dataclass
class Employee:
    person_idx: int
    position: str
    department: Department
    profit: float
    hired_from: datetime.date


persons: dict = {}
departments: dict = {}
employees: dict = {}
dep_empls: dict = {}
