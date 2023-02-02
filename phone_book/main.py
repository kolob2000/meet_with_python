from aiogram import Dispatcher, Bot
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State
from aiogram.types import Message
from phone_book.model.model import select_all, init

from phone_book.forms import add_new_contact, get_name, get_phone_number, get_city, get_name_for_search, search_by_name, \
    search_by_city, get_city_for_search, remove_by_id, get_id_for_remove, get_all_book, get_csv
from phone_book.main_menu import set_main_menu
from phone_book.state_forms import ContactForm

API_TOKEN: str = '5662299299:AAGzX_k5LCFx24VyISLsxbB1X_ZLsuxZO78'
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nЯ бот телефонная книга!\n'
                         'введи команду /help, чтобы узнать, что я умею.')


@dp.message(Command(commands=["help"]))
async def process_start_command(message: Message):
    await message.answer('''
    Справка по боту "Телефонный справочник":
    Все эти команды дублируются в меню!
    Начать работу боту - /start,
    Справка по работе бота - /help,
    Добавить контакт - /add_contact,
    Вывести всю книгу - /all_contacts,
    Поиск по имени - /search_by_name,
    Поиск по городу - /search_by_city,
    Удалить запись по id - /remove_by_id,
    Отменить ввод - /cancel,
    ''')


@dp.message(Command(commands=['cancel']))
async def reset_state(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('Операция отменена.')


dp.message.register(get_all_book, Command(commands=["all_contacts"]))
dp.message.register(get_csv, Command(commands=["get_csv"]))

dp.message.register(add_new_contact, Command(commands=['add_contact']))
dp.message.register(get_name, ContactForm.GET_NAME)
dp.message.register(get_phone_number, ContactForm.GET_PHONE)
dp.message.register(get_city, ContactForm.GET_CITY)

dp.message.register(search_by_name, Command(commands='search_by_name'))
dp.message.register(get_name_for_search, ContactForm.GET_NAME_FOR_SEARCH)

dp.message.register(search_by_city, Command(commands='search_by_city'))
dp.message.register(get_city_for_search, ContactForm.GET_CITY_FOR_SEARCH)

dp.message.register(remove_by_id, Command(commands='remove_by_id'))
dp.message.register(get_id_for_remove, ContactForm.GET_ID_FOR_REMOVE)


@dp.startup()
async def on_startup(bot: Bot):
    print('Bot working...')
    await set_main_menu(bot)


@dp.shutdown()
async def on_shutdown(bot: Bot):
    print('Bot stop working!')


if __name__ == '__main__':
    dp.run_polling(bot)
