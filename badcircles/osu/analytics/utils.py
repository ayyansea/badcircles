from typing import Tuple
from .criteria import ScoreCriteria


def get_ranking(value: float, criteria) -> str:
    for level in criteria:
        low = level.value[1][0]
        high = level.value[1][1]
        name = level.value[0]

        if value == high:
            return name

        if value >= low and value < high:
            return name


def get_score(value: str) -> int:
    for level in ScoreCriteria:
        letter = level.name
        score = level.value

        if value == letter:
            return score


def get_letter(value: float) -> str:
    for level in ScoreCriteria:
        letter = level.name
        score = level.value

        if value == score or value > score:
            return letter


def average_score(*scores: Tuple) -> float:
    average = 0

    for ranking in scores:
        average += scores[1]

    return average / len(scores)
