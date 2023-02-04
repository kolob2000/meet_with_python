from aiogram.fsm.state import StatesGroup, State


class ContactForm(StatesGroup):
    GET_NAME = State()
    GET_PHONE = State()
    GET_CITY = State()
    GET_NAME_FOR_SEARCH = State()
    GET_CITY_FOR_SEARCH = State()
    GET_ID_FOR_REMOVE = State()
