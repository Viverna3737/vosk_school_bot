
from src.bot import dp, bot
from aiogram.dispatcher.filters.state import StatesGroup, State




class Machine(StatesGroup):
    homework = State()
    s_u_m = State()

