from aiogram.fsm.state import State, StatesGroup


class CalculateForm(StatesGroup):
    FIRST_OPERAND = State()
    # SECOND_OPERAND = State()
    # OPERATOR = State()
