import config
import logging
from aiogram import Bot, Dispatcher, executor, types

# log level
logging.basicConfig(level=logging.INFO)

# bot init
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

# echo
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


# проверка плохих слов
'''@dp.message_handler()
async def filter_messages(message: types.Message):
    for w in config.LIST_BAD_WORDS:
        if w in message.text.lower():
            await message.delete()
            await message.answer(f'@{message.from_user.username} Ругаться нельзя!')'''


# run long-polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)