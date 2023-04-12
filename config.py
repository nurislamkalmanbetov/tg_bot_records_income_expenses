from  aiogram import  Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage



TOKEN = '6092765427:AAHCnmSNTq106K9dRtDRJXZzhjrbKOSJuWQ'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


