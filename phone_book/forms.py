import time

from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile

from phone_book.state_forms import ContactForm
from phone_book.model.model import init, add_row, select_by_filter, delete_row, select_all, export_to_csv

from phone_book.view.view import view_result

cur, con = init()


async def get_all_book(message: Message):
    book = select_all(cur)
    await view_result(book, message)


# -------------------------------------------------------------

async def add_new_contact(message: Message, state: FSMContext):
    await message.answer('Добавление контакта.\n'
                         'Введите имя - ')
    await state.set_state(ContactForm.GET_NAME)


async def get_name(message: Message, state: FSMContext):
    await message.answer(f'Отлично! Имя - {message.text}.\n'
                         f'Введите номер телефона - ')
    await state.update_data(name=message.text)
    await state.set_state(ContactForm.GET_PHONE)


async def get_phone_number(message: Message, state: FSMContext):
    await message.answer(f'Отлично! Номер - {message.text}.\n'
                         f'Введите город - ')
    await state.update_data(phone=message.text)
    await state.set_state(ContactForm.GET_CITY)


async def get_city(message: Message, state: FSMContext):
    await message.answer(f'Отлично! Город - {message.text}.')
    await state.update_data(city=message.text)
    data = await state.get_data()
    add_row(cur, data, con)
    await message.answer('Запись добавлена')
    await state.clear()


# -------------------------------------------------------------
async def search_by_name(message: Message, state: FSMContext):
    await message.answer('Поиск по имени.\n'
                         'Введите имя и/или фамилию - ')
    await state.set_state(ContactForm.GET_NAME_FOR_SEARCH)


async def get_name_for_search(message: Message, state: FSMContext):
    await message.answer(f'Отлично! Имя - {message.text}.\n'
                         f'Начинаю поиск...')
    book = select_by_filter(cur, message.text.lower(), "2")
    await view_result(book, message)
    await state.clear()


# --------------------------------------------------------------
async def search_by_city(message: Message, state: FSMContext):
    await message.answer('Поиск по городу.\n'
                         'Введите город - ')
    await state.set_state(ContactForm.GET_CITY_FOR_SEARCH)


async def get_city_for_search(message: Message, state: FSMContext):
    await message.answer(f'Отлично! Город - {message.text}.\n'
                         f'Начинаю поиск... ')
    book = select_by_filter(cur, message.text.lower(), "3")
    await view_result(book, message)
    await state.clear()


# --------------------------------------------------------------
async def remove_by_id(message: Message, state: FSMContext):
    await message.answer('Удаление записи по id.\n'
                         'Введите id записи - ')
    await state.set_state(ContactForm.GET_ID_FOR_REMOVE)


async def get_id_for_remove(message: Message, state: FSMContext):
    await message.answer(f'Отлично! Id записи - {message.text}.\n'
                         f'Удаляю... ')
    try:
        delete_row(cur, con, message.text)
        time.sleep(1)
        await message.answer('Удалил')
    except:
        await message.answer('Нет такой записи!')
    await state.clear()


# --------------------------------------------------------------

async def get_csv(message: Message):
    export_to_csv(select_all(cur))
    file = FSInputFile('phonebook.csv')
    await message.answer_document(file)
