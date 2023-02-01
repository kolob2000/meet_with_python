import json
import time
from asyncio import sleep

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, Text, Filter
from aiogram.types import Message, ContentType, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from tic_tac_toe.filter import IsMoveFilter, LetsPlayFilter, DontPlayFilter
from tic_tac_toe.game_func import check_desk, reset_board
from tic_tac_toe.keyboard import create_keyboard

API_TOKEN: str = 'YOUR_TOKEN'
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()
board: list = [['.' for _ in range(3)] for _ in range(3)]

move = ['X']
count = [0]


@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nЯ бот!\n'
                         'Я умею играть в крестики-нолики. '
                         '\nСыграем? Да или нет?')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer('Чтобы сыграть введите любое сообщение \n'
                         '[ok, yes, да, ок, сыграем, давай]\n'
                         'либо команду /game.\n'
                         'для выхода из игры команда /cancel.')


@dp.message(Command(commands=['game']))
async def process_help_command(message: Message):
    await message.answer('Начинаем',
                         reply_markup=create_keyboard(board))


@dp.message(DontPlayFilter())
async def process_help_command(message: Message):
    time.sleep(1)
    reset_board(board)
    count[0] = 0
    move[0] = 'X'
    await message.answer('Жаль((. Но если, что зовите - поиграем :). ')


@dp.message(LetsPlayFilter())
async def process_help_command(message: Message):
    await message.answer('Начинаем',
                         reply_markup=create_keyboard(board))


@dp.callback_query(IsMoveFilter())
async def button_1(callback: CallbackQuery):
    i = int(callback.data[0])
    j = int(callback.data[1])
    if board[i][j] == '.':
        board[i][j] = move[0]
        count[0] += 1
        if check_desk(board, move[0]):
            time.sleep(1)
            reset_board(board)
            count[0] = 0
            move[0] = 'X'
            await callback.message.edit_text(f'Ура! Победил {move[0]}. Повторим?')
        else:
            if count[0] < 9:
                move[0] = 'X' if move[0] == 'O' else 'O'
                await callback.message.edit_text(f'Ходит {move[0]}', reply_markup=create_keyboard(board))
            else:
                time.sleep(1)
                await callback.message.edit_text('Ничья! Победила дружба). Повторим?')
                count[0] = 0
                move[0] = 'X'
                reset_board(board)
        await callback.answer()
    else:
        await callback.answer()


if __name__ == '__main__':
    dp.run_polling(bot)
