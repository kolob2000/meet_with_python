from aiogram import Bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, BotCommand


def create_keyboard() -> InlineKeyboardMarkup:
    b_reset = InlineKeyboardButton(text='>>', callback_data='C')
    b_clear = InlineKeyboardButton(text='C', callback_data='clear')
    b_empty = InlineKeyboardButton(text=' ', callback_data='empty')
    b1 = InlineKeyboardButton(text='1', callback_data='1')
    b2 = InlineKeyboardButton(text='2', callback_data='2')
    b3 = InlineKeyboardButton(text='3', callback_data='3')
    b4 = InlineKeyboardButton(text='4', callback_data='4')
    b5 = InlineKeyboardButton(text='5', callback_data='5')
    b6 = InlineKeyboardButton(text='6', callback_data='6')
    b7 = InlineKeyboardButton(text='7', callback_data='7')
    b8 = InlineKeyboardButton(text='8', callback_data='8')
    b9 = InlineKeyboardButton(text='9', callback_data='9')
    b0 = InlineKeyboardButton(text='0', callback_data='0')
    b_plus = InlineKeyboardButton(text='+', callback_data='+')
    b_minus = InlineKeyboardButton(text='-', callback_data='-')
    b_mult = InlineKeyboardButton(text='*', callback_data='*')
    b_div = InlineKeyboardButton(text='/', callback_data='/')
    b_sign = InlineKeyboardButton(text='+/-', callback_data='sign')
    b_dot = InlineKeyboardButton(text='.', callback_data='.')
    b_equal = InlineKeyboardButton(text='=', callback_data='=')

    return InlineKeyboardMarkup(
        inline_keyboard=[

            [b_clear, b_reset, b_empty, b_div],
            [b1, b2, b3, b_mult],
            [b4, b5, b6, b_minus],
            [b7, b8, b9, b_plus],
            [b_sign, b0, b_dot, b_equal]
        ]
    )


main_menu_commands = [
    BotCommand(command='/start', description='Начать работу боту'),
    BotCommand(command='/help', description='Справка по работе бота'),
    BotCommand(command='/calculator', description='Начать вычисления'),
    BotCommand(command='/cancel', description='Отменить ввод'),
]


async def set_main_menu(bot: Bot):
    await bot.set_my_commands(main_menu_commands)
