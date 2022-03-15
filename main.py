import config
import logging
from aiogram import Bot, Dispatcher, executor, types

# log level
logging.basicConfig(level=logging.INFO)

# bot init
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(content_types=["new_chat_members"])
async def new_user(message: types.Message):
    first_name, last_name, username = ('', '', '')
    for new_user in message.new_chat_members:
        first_name = new_user.first_name
        last_name = ' ' + new_user.last_name if new_user.last_name not in (None, 'None') else ''
        username = ' ' + new_user.username if new_user.username not in (None, 'None') else ''
    await message.answer(f'🍀 К нам присоединился космополит {first_name}{last_name}{username}!')


# проверка плохих слов
@dp.message_handler()
async def filter_messages(message: types.Message):
    for w in config.LIST_BAD_WORDS:
        if w in message.text.lower():
            await message.delete()
            await message.answer(f'@{message.from_user.username} Ругаться нельзя!')

@dp.message_handler(commands=["!start"])
async def filter_messages(message: types.Message):
    await message.answer('Немезида на связе')


# run long-polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)