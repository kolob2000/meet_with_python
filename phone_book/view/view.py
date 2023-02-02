from aiogram.types import Message


async def view_result(data, message: Message):
    book = data.fetchall()
    if not len(book):
        await message.answer('Записей нет.')
    else:
        for i in book:
            await message.answer(f'{i[0]}  {i[1]}  {i[2]}  {i[3]}')
