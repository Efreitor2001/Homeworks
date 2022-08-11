from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot('TOKEN')
dp = Dispatcher(bot)


# 1. Напишите бота, удаляющего из текста все слова, содержащие "абв".
@dp.message_handler(content_types=['text'])
async def abv(message):
    s = 'абв'
    s1 = message.text.split()
    res = []
    for i in s1:
        if s not in i:
            res.append(i)
    message.text = ' '.join(res)
    if message.text == '':
        await bot.send_message(message.chat.id, 'Empty message')
    else:
        await bot.send_message(message.chat.id, message.text)


print('run')
executor.start_polling(dp)
