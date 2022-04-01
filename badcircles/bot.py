from vkbottle import VKAPIError
from vkbottle.bot import Bot, Message
from badcircles.settings import VK_TOKEN

bot = Bot(token = VK_TOKEN)

@bot.on.message(text = "слыш")
async def respond(message: Message):
    '''
    Ответ на заданное сообщение.
    '''

    try:
        await message.answer("за углом поссыш) че надо")
    except VKAPIError as e:
        print(f"Ошибка: {e.description} [{e.code}]")


def start():
    '''
    Указание боту работать бесконечно,
    пока он не будет остановлен вручную.
    '''

    bot.run_forever()