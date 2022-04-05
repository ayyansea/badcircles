from .accuracy import acc_Analyze, acc_setRanking
from .criteria import LengthCriteria
from .utils import get_ranking, average_ranking


def plays_accAnalyze(plays: list) -> float:
    acc_score = 0
    for play in plays:
        acc = acc_Analyze(play.accuracy * 100)
        acc_score += acc[1]

    ranking = acc_setRanking(acc_score / len(plays))
    return ranking


def plays_lengthAnalyze(plays: list):
    length_score = 0

    for play in plays:
        length = play.beatmap.total_length
        for criteria in LengthCriteria:
            high = criteria.value[1][1]
            low = criteria.value[1][0]
            ranking = criteria.name
            if length < high and length >= low:
                length_score += get_ranking(ranking)

    ranking = get_ranking(length_score / len(plays))
    return ranking


def plays_Analyze(plays: list):
    acc, length = plays_accAnalyze(plays), plays_lengthAnalyze(plays)
    return average_ranking(acc, length)
