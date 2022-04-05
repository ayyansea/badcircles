from ossapi import User
from .osuapi import api


def get_user(id):
    """
    Получить объект юзера.
    """

    return api.user(id)


def get_stats(user: User):
    """
    Получить информацию о юзере.
    """

    stats = {
        "Никнейм": user.username,
        "ПП": str(int(user.statistics.pp)) + "pp",
        "Точность": str(user.statistics.hit_accuracy) + "%",
        "Страна": user.country.name + f" ({user.country.code})",
        "Место в мире": "#" + str(user.statistics.global_rank),
        "Место в стране": "#" + str(user.statistics.country_rank),
        "Плейкаунт": user.statistics.play_count,
        "Плейтайм": user.statistics.play_time,
        "Максимальное комбо": str(user.statistics.maximum_combo) + "x",
    }

    return stats


def get_top_plays(id: int):
    return api.user_scores(id, "best", limit=10)


def format_stats(stats: dict):
    """
    Собрать из информации текст.
    """

    info = ""

    for stat, value in stats.items():
        info += f"> {stat}: {value}\n"

    return info[:-1]
