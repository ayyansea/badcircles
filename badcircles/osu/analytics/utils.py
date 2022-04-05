from typing import Tuple
from .criteria import RankingCriteria


def get_ranking(value):
    for criteria in RankingCriteria:
        number = criteria.value[1]
        letter = criteria.name

        if type(value) is float:
            return get_ranking(int(value))

        if type(value) is int:
            if value == number or value > number:
                return (criteria.name, value)

        if type(value) is str:
            if value == letter:
                return number


def average_ranking(*rankings: Tuple):
    average = 0

    for ranking in rankings:
        average += ranking[1]

    return get_ranking(average / len(rankings))
