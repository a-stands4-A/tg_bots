import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config import TOKEN
import random as rm

# Объект бота
bot = Bot(token=TOKEN)
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def start(message: types.Message):
    await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEKm85lOXwF6uvk4rmKcExKjAsynwN7WgACpRAAArRFoEpqI1qAWc6jRzAE")


# Хэндлер на команду /echo
@dp.message(Command("echo"))
async def cmd_test1(message: types.Message):
    await message.answer(text=message.text + ", GIT GUT, MATE")


# Хэндлер на команду /d
@dp.message(Command("d"))
async def cmd_roll_dice(message: types.Message):
    dice_dict = {
        0: "CAACAgIAAxkBAAEKm8NlOXJeNmTpAw84glP0wZ_ULOq6kgACdHMAAp7OCwAB3u2HBGcs9q0wBA",
        1: "CAACAgIAAxkBAAEKm7dlOXH5DEj69DiKGxh6mvsi4twDQwACBnMAAp7OCwABeRelZgnyaW4wBA",
        2: "CAACAgIAAxkBAAEKm7llOXIQphhQUd3zcpdRMtAri1V3_AACB3MAAp7OCwABHTuSAdZlD04wBA",
        3: "CAACAgIAAxkBAAEKm7tlOXIi5LQ7meU702qfCjpaGT7esQACCHMAAp7OCwABK3IbM1dVAtYwBA",
        4: "CAACAgIAAxkBAAEKm71lOXIv0W28OmYiilX0oNDsf3yuOQACCXMAAp7OCwAB_bjDE4sPJlcwBA",
        5: "CAACAgIAAxkBAAEKm79lOXI89ZAzMGqTalEFmQsnEjhlDwACCnMAAp7OCwABB1FnIcyJWCIwBA",
        6: "CAACAgIAAxkBAAEKm8FlOXJJejEOotg2F0hx9XIMXBIUUgACC3MAAp7OCwAB_nCt2sUm8FIwBA",
        7: "CAACAgIAAxkBAAEKm8VlOXJk2ZiKOrk9jvtAUdw0p83O2QAChHMAAp7OCwABZ0O6RhLu2lAwBA",
    }
    # await bot.send_sticker(message.from_user.id, sticker=dice_dict[0])
    random_dice = rm.randint(1, 7)
    # Запускаем таймер для удаления сообщения через 5 секунд
    await bot.send_chat_action(message.chat.id, "typing")  # Эмулируем "печатание"
    sent_message = await bot.send_sticker(message.from_user.id, sticker=dice_dict[random_dice])
    await asyncio.sleep(10)
    await message.delete()
    await sent_message.delete()


# Хэндлер на команду /re
@dp.message(Command("help"))
async def cmd_echo(message: types.Message):
    await message.reply(text="/help - help\n/d - roll the dice\n/echo - echo\n/start - cool sticker\nno command - echoV1")


@dp.message()
async def echo_message(message: types.Message):
    await message.reply(message.text)


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot, on_startup=start, skip_updates=True, )


if __name__ == "__main__":
    asyncio.run(main())
