from vkbottle.bot import Bot, Message
from vkbottle.dispatch.rules.base import CommandRule
from badcircles.settings import VK_TOKEN
from typing import Tuple
from badcircles.patterns import GreetingPatterns, MemePatterns, ReplyPatterns
from enum import Enum

import re

bot = Bot(token=VK_TOKEN)


async def patterncheck(message: Message, *patterns: Enum):
    """
    Проверка входящего сообщения на соответствие
    заданным наборам паттернов.
    """

    fragments = []
    answer = ""
    stripped_text = message.text.replace("\n", "")

    for patternset in patterns:
        for pattern in patternset:
            for regex in pattern.value[0]:
                compiled = re.compile(regex, re.IGNORECASE)
                if compiled.match(stripped_text):
                    fragments.append(pattern.value[1])

    if fragments:
        for item in fragments:
            answer += item + "\n"
        await message.reply(answer)


@bot.on.message(CommandRule("test", ["!", "/"], 1))
async def test_handler(message: Message, args: Tuple[str, int]):
    """
    Тестовый хендлер с правилом CommandRule.
    """

    answer = args[0]

    await patterncheck(message, MemePatterns)
    await message.reply(answer)


@bot.on.message()
async def any_message(message: Message):
    """
    Ловит любые сообщения, не попадающие
    под остальные хендлеры.
    """

    await patterncheck(message, MemePatterns, ReplyPatterns, GreetingPatterns)


def start():
    """
    Указание боту работать бесконечно,
    пока он не будет остановлен вручную.
    """

    bot.run_forever()
