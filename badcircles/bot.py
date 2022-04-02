from vkbottle.bot import Bot, Message
from vkbottle.dispatch.rules.base import CommandRule, RegexRule
from badcircles.settings import VK_TOKEN
from typing import Tuple
from badcircles.patterns import MemePatterns
from enum import Enum

import re

bot = Bot(token=VK_TOKEN)


async def patterncheck(message: Message, *patterns: Enum):
    """
    Проверка входящего сообщения на соответствие
    заданным наборам паттернов.
    """

    for patternset in patterns:
        for pattern in patternset:
            for regex in pattern.value[0]:
                compiled = re.compile(regex, re.IGNORECASE)
                if compiled.match(message.text):
                    await message.answer(pattern.value[1])


@bot.on.message(CommandRule("test", ["!", "/"], 1))
async def test_handler(message: Message, args: Tuple[str, int]):
    """
    Тестовый хендлер с правилом CommandRule.
    """

    answer = args[0]

    await patterncheck(message, MemePatterns)
    await message.answer(answer)


@bot.on.message(RegexRule("^.*$"))
async def any_message(message: Message):
    """
    Ловит любые сообщения, не попадающие
    под остальные хендлеры.
    """

    await patterncheck(message, MemePatterns)


def start():
    """
    Указание боту работать бесконечно,
    пока он не будет остановлен вручную.
    """

    bot.run_forever()
