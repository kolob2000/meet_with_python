from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery


class IsMove(BaseFilter):
    async def __call__(self, callback: CallbackQuery):
        try:
            moves = ['00', '01', '02', '10', '11', '12', '20', '21', '22']
            return callback
        except:
            return False
