from typing import Tuple
from .criteria import AccCriteria
from .utils import get_ranking, get_score


def acc_Analyze(accuracy: float) -> Tuple:
    acc = int(accuracy)
    rank = get_ranking(acc, AccCriteria)
    score = get_score(rank)

    return rank, score
