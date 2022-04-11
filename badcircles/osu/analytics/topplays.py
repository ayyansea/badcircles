from .criteria import AccCriteria, LengthCriteria
from .utils import get_ranking, get_score, get_letter, average_score


def plays_accAnalyze(plays: list) -> float:
    acc_score = 0
    for play in plays:
        accuracy = int(play.accuracy * 100)
        score = get_ranking(accuracy, AccCriteria)
        acc_score += get_score(score)

    return acc_score / len(plays)


def plays_lengthAnalyze(plays: list):
    length_score = 0

    for play in plays:
        length = play.beatmap.total_length
        rank = get_ranking(length, LengthCriteria)
        length_score += get_score(rank)

    return length_score / len(plays)


def plays_Analyze(plays: list):
    acc_score = plays_accAnalyze(plays)
    length_score = plays_lengthAnalyze(plays)
    avg_score = average_score(acc_score, length_score)
    rank = get_letter(avg_score)

    return rank, avg_score
