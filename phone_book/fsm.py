from aiogram import Bot, Dispatcher
from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

API_TOKEN: str = 'TELEGRAM_TOKEN'
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

from aiogram.fsm.state import StatesGroup, State


class ContactForm(StatesGroup):
    GET_NAME = State()
    GET_PHONE = State()


# @dp.message_handler(Command(commands=['lets_go'])) - не работает
@dp.message(Command(commands=['cancel']))
async def cancel_state(message: Message, state: FSMContext):
    await message.answer('Отмена ввода.')
    await state.clear()


@dp.message(ContactForm.GET_NAME)
async def get_name(message: Message, state: FSMContext):
    await message.answer(f'Имя - {message.text}.\nТеперь введите номер телефона - ')
    await state.update_data(name=message.text)
    await state.set_state(ContactForm.GET_PHONE)


async def get_phone(message: Message, state: FSMContext):
    await message.answer(f'Номер телефона - {message.text}')
    await state.update_data(phone=message.text)
    data = await state.get_data()
    await message.answer(str(data))
    await state.clear()


dp.message.register(get_phone, ContactForm.GET_PHONE)


@dp.message(Command(commands=['lets_go']))
async def lets_go(message: Message, state: FSMContext):
    await message.answer('Начинаем ввод данных.\n Введите имя -  ')
    await state.set_state(ContactForm.GET_NAME)


# dp.message_handler_register(Command(commands=['lets_go'])) - не работает


@dp.message(Text(text='Валера'))
async def echo(message: Message):
    await message.reply('handler только для Валеры')


@dp.message()
async def echo(message: Message):
    await message.reply(message.text)


if __name__ == '__main__':
    dp.run_polling(bot)
