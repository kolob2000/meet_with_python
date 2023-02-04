from aiogram import Bot
from aiogram.types import BotCommand

main_menu_commands = [
    BotCommand(command='/start', description='Начать работу боту'),
    BotCommand(command='/help', description='Справка по работе бота'),
    BotCommand(command='/get_csv', description='Экспорт книги в csv файл'),
    BotCommand(command='/add_contact', description='Добавить контакт'),
    BotCommand(command='/all_contacts', description='Вывести всю книгу'),
    BotCommand(command='/search_by_name', description='Поиск по имени'),
    BotCommand(command='/search_by_city', description='Поиск по городу'),
    BotCommand(command='/remove_by_id', description='Удалить запись по id'),
    BotCommand(command='/cancel', description='Отменить ввод'),
]


async def set_main_menu(bot: Bot):
    # Создаем список с командами для кнопки menu
    await bot.set_my_commands(main_menu_commands)
