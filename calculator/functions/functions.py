from aiogram.types import CallbackQuery


def simple_calculate(op_1: str, op_2: str, operator: str):
    op_1 = float(op_1)
    op_2 = float(op_2)
    match operator:
        case '+':
            return op_1 + op_2
        case '-':
            return op_1 - op_2
        case '*':
            return op_1 * op_2
        case '/':
            return op_1 / op_2


async def print_message(callback_query: CallbackQuery, operands: dict, cb_keyboard):
    await callback_query.message.edit_text(
        f"res >  {operands['first_op'][0] + operands['first_op'][1]}\n"
        f"inp >  {operands[operands['state']][0] + operands[operands['state']][1]}",
        reply_markup=cb_keyboard())


def clear_state(operands: dict, state='first_op'):
    operands['state'] = state
    operands['length'] = 0
    operands['first_op'] = ['', '']
    operands['second_op'] = ['', '']
    operands['operand'] = ''
