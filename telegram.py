from aiogram import Bot,Dispatcher, executor, types
bot = Bot(token="5835501905:AAF6_uG3dvENPJDfB_d_jo9z4M8O8F4fa0U")
dp = Dispatcher(bot)
qualité = ""

@dp.message_handler(commands=['start','help'])
async def welcome(message: types.Message):
    await message.reply("Bienvenue sur AirGeneve. Pour connaitre la qualité de l'air actuelle, tapez /air")

@dp.message_handler(commands=['air'])
async def air(message: types.Message):
    qualité = "bonne"
    if qualité == "bonne":
        await message.reply("La qualité de l'air est bonne")
        await message.answer_photo("https://github.com/helene-moore/AirGeneve/blob/main/mesure.png?raw=true")
    else:
        await message.reply("La qualité de l'air est mauvaise")
        await message.answer_photo("https://github.com/helene-moore/AirGeneve/blob/main/Sans%20titre%20(2).png?raw=true")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

executor.start_polling(dp)