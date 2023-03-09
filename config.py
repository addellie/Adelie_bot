from aiogram import Dispatcher, Bot
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

TOKEN = config('TOKEN')


ADMIN = (506455928)
bot = Bot(TOKEN)
db = Dispatcher(bot=bot, storage=storage)
