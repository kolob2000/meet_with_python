from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from environs import Env

from keyboard import set_main_menu
from states import start_calculation, cancel_calculation, calculator
from states import CalculateForm

env = Env()
env.read_env()

API_TOKEN = env('TELEGRAM_TOKEN')
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


@dp.message(Command(commands=['help']))
async def get_help(message: Message):
    await message.answer('Справка.\n'
                         'Для начала вычислений введите команду   <b>/calculator.</b>\n'
                         'Для отмены вычислений команду   <b>/cancel</b>', parse_mode='HTML')


dp.message.register(cancel_calculation, Command(commands=['cancel']))

dp.message.register(start_calculation, Command(commands=['calculator']))
dp.callback_query.register(calculator, CalculateForm.FIRST_OPERAND)


@dp.message(Command(commands=['start']))
async def start(message: Message):
    await message.answer('Привет. Я бот-калькулятор.\n'
                         'Умею работать с вещественными числами.\n'
                         'В будущем буду и с комплексными. Наверное.'
                         'Но пока работаю только с двумя операндами.\n'
                         'Для деталей наберите команду   <b>/help</b>', parse_mode='HTML')


@dp.startup()
async def on_start():
    await set_main_menu(bot)
    print('Bot is working...')


@dp.shutdown()
async def on_finish():
    print('Bot is stopped.')


if __name__ == '__main__':
    dp.run_polling(bot)
