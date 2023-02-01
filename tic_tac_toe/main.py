import json
import time
from asyncio import sleep

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, Text
from aiogram.types import Message, ContentType, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from tic_tac_toe.game_func import check_desk, reset_board
from tic_tac_toe.keyboard import create_keyboard

API_TOKEN: str = '5662299299:AAFUectBCIxYz6die5bjaXnC04Heywo9qbY'
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()
board: list = [['.' for _ in range(3)] for _ in range(3)]

print(board[int('0')])
move = ['X']


@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nЯ бот!\n'
                         'Я умею играть в крестики-нолики. '
                         '\nСыграем? Да или нет?')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer('Напиши мне что-нибудь и в ответ '
                         'я пришлю тебе твое сообщение')


@dp.message(Command(commands=['game']))
async def process_help_command(message: Message):
    await message.answer('Начинаем',
                         reply_markup=create_keyboard(board))


@dp.callback_query()
async def button_1(callback: CallbackQuery, bot: Bot):
    i = int(callback.data[0])
    j = int(callback.data[1])
    if board[i][j] == '.':
        board[i][j] = move[0]
        print(board)
        if check_desk(board, move[0]):
            time.sleep(1)
            reset_board(board)
            await callback.message.edit_text(f'Ура! Победил {move[0]}')
        else:
            move[0] = 'X' if move[0] == 'O' else 'O'
            await callback.message.edit_text(f'Ходит {move[0]}', reply_markup=create_keyboard(board))

        await callback.answer()
    else:
        await callback.answer()


if __name__ == '__main__':
    dp.run_polling(bot)
