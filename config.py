from  aiogram import  Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage



TOKEN = '6016862759:AAHTnhgyT6bCpaiMgRaOo-FrKW3n5Phvq1o'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


