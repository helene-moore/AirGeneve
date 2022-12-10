from aiogram import Bot, Dispatcher, executor, types
bot = Bot(token="5835501905:AAF6_uG3dvENPJDfB_d_jo9z4M8O8F4fa0U")
dp = Dispatcher(bot)
qualité = "mauvaise"


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.reply("Bienvenue sur AirGeneve.\n"
                        "Pour connaitre la qualité de l'air actuelle, tapez /air.\n"
                        "En cas de doute/question, n'hésitez pas à écrire /help\n"
                        "Si vous souhaitez aider à réduire la pollution de l'air, tapez /actions")


@dp.message_handler(commands=['help'])
async def welcome(message: types.Message):
    await message.reply("Pour connaitre la qualité de l'air actuelle, tapez /air\n"
                        "En cas de doute/question, n'hésitez pas à écrire /help\n"
                        "Si vous souhaitez aider à réduire la pollution de l'air, tapez /actions")

@dp.message_handler(commands=['actions'])
async def welcome(message: types.Message):
    await message.reply("Pour réduire la pollution de l'air, voici nos recommandations:\n"
                        "\t- Choisir et entretenir votre appareil de chauffage performant labellisé\n"
                        "\t- Privilégier les transports en commun, la marche ou le vélo\n"
                        "\t- Choisir un appareil de chauffage performant labellisé\n")
    await  message.reply("Pour plus d'informations/conseils, vous pouvez consulter le site suivant: https://www.airparif.asso.fr/agir-pour-la-qualite-de-lair/gestes-quotidiens-pour-reduire-son-impact-sur-la-pollution#:~:text=Privil%C3%A9giez%20les%20vaporisateurs%20aux%20bombes,pr%C3%A9f%C3%A9rez%20une%20a%C3%A9ration%20le%20matin.")

@dp.message_handler(commands=['air'])
async def air(message: types.Message):
    #qualité = "mauvais"
    if qualité == "bonne":
        await message.reply("La qualité de l'air est bonne")
        await message.answer_photo("https://github.com/helene-moore/AirGeneve/blob/main/mesure.png?raw=true")
    elif qualité == "mauvais":
        await message.reply("La qualité de l'air est mauvaise")
        await message.answer_photo(
            "https://github.com/helene-moore/AirGeneve/blob/main/Sans%20titre%20(2).png?raw=true")
        await message.reply(
            "Pour savoir comment se protéger, voici les recommandations de l'Office fédérale de l'environnement: https://www.bafu.admin.ch/bafu/fr/home/themes/air/info-specialistes/mesures-de-protection-de-l-air.html ")
    elif qualité == "moyenne":
        await message.reply("La qualité de l'air est moyenne")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("Nous n'avons pas compris votre questions. Merci d'utiliser les commandes /start, /help, /actions ou /air")

executor.start_polling(dp)