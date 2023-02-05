from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from calculator.keyboard import create_keyboard
from states import CalculateForm
from calculator.functions import simple_calculate, print_message, clear_state

operands_db: dict = {}


async def start_calculation(message: Message, state: FSMContext):
    if f'{message.from_user.id}' not in operands_db:
        operands_db[f'{message.from_user.id}'] = {
            'state': '',
            'length': 0,
            'first_op': ['', ''],
            'second_op': ['', ''],
            'operand': ''
        }
    if operands_db[f'{message.from_user.id}']['state'] == '':
        operands_db[f'{message.from_user.id}']['state'] = 'first_op'
        await message.answer('res >\ninp >', reply_markup=create_keyboard())
        await state.set_state(CalculateForm.FIRST_OPERAND)


async def cancel_calculation(message: Message, state: FSMContext, bot: Bot):
    clear_state(operands_db[f'{message.from_user.id}'], '')
    await state.clear()
    await bot.delete_message(message.chat.id, message.message_id - 1)
    await message.answer('Вычисление отменено.')


async def calculator(callback: CallbackQuery):
    operands = operands_db[f'{callback.from_user.id}']
    if callback.data == 'clear':
        clear_state(operands)
        await callback.message.delete()
        await callback.message.answer(f'res >\ninp >', reply_markup=create_keyboard())
    elif callback.data == 'empty':
        await callback.answer()
    elif callback.data == '=':
        if len(operands['first_op'][1]) and len(operands['second_op'][1]):
            if float(operands['second_op'][1]) == 0 and operands['operand'] == '/':
                await callback.answer('На ноль делить нельзя!')
            else:
                result = simple_calculate(operands['first_op'][0] + operands['first_op'][1],
                                          operands['second_op'][0] + operands['second_op'][1], operands['operand'])
                await callback.message.edit_text(f'res >  {result}\ninp >', reply_markup=create_keyboard())
                clear_state(operands)
        elif len(operands['first_op'][1]):
            await callback.message.edit_text(f'res >   {operands["first_op"][1]}\ninp >',
                                             reply_markup=create_keyboard())
            clear_state(operands)
        await callback.answer()
    elif callback.data in ['+', '-', '*', '/'] and len(operands[operands['state']][1]) != 0:
        if operands['state'] == 'first_op':
            operands['state'] = 'second_op'
            operands['length'] = 0
            operands['operand'] = callback.data
            await print_message(callback, operands, create_keyboard)
        else:
            if float(operands['second_op'][1]) == 0 and operands['operand'] == '/':
                await callback.answer('На ноль делить нельзя!')
            else:
                result = simple_calculate(operands['first_op'][0] + operands['first_op'][1],
                                          operands['second_op'][0] + operands['second_op'][1], operands['operand'])
                if result < 0:
                    operands['first_op'][0] = '-'
                    operands['first_op'][1] = str(abs(result))
                else:
                    operands['first_op'][0] = ''
                    operands['first_op'][1] = str(result)
                operands['second_op'] = ['', '']
                operands['length'] = 0
                operands['operand'] = callback.data
                await print_message(callback, operands, create_keyboard)
        await callback.answer()
    else:
        if callback.data == '.' and '.' in operands[operands['state']][1]:
            await callback.answer()
        # ###############################
        else:
            if callback.data == 'sign':
                operands[operands['state']][0] = '' if (operands[operands['state']][0] == '-') else '-'
            # ###############################
            if callback.data == 'C':
                if len(operands[operands['state']][1]) < 2:
                    operands[operands['state']][1] = ''
                    operands[operands['state']][0] = ''
                else:
                    operands[operands['state']][1] = operands[operands['state']][1][:-1]
                    operands['length'] -= 1
            elif callback.data not in ['+', '-', '*', '/', 'C', 'sign', '=']:
                if callback.data == '.' and len(operands[operands['state']][1]) == 0:
                    operands[operands['state']][1] = '0.'
                    operands['length'] += 2
                else:
                    operands[operands['state']][1] += str(callback.data)
                    operands['length'] += 1
            if operands['length'] > 0:
                if operands[operands['state']][1] == '':
                    operands['length'] -= 1
                await print_message(callback, operands, create_keyboard)
            await callback.answer()
