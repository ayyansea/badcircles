from typing import Tuple
from .criteria import RankingCriteria, AccCriteria


def acc_toInt(accuracy: float) -> int:
    return int(accuracy)


def acc_range(accuracy: int):
        for accrange in AccCriteria:
            high = accrange.value[1]    
            low = accrange.value[0]
        
            if accuracy < high and accuracy >= low:
                return accrange.name
   
            
def acc_calculateScore(accrange: str) -> int:
        finalscore = 0
    
        for rank in RankingCriteria:
            scorevalue = rank.value[1]
            if accrange == rank.name:
                finalscore = scorevalue
        
        return finalscore


def acc_setRanking(score: int) -> Tuple:    
        for criteria in RankingCriteria:
            number = criteria.value[1]
            
            if score == number or score > number:
                return (criteria.name, score)
    
            
def acc_Analyze(accuracy: float) -> Tuple:
    acc = acc_toInt(accuracy)
    accrange = acc_range(acc)
    score = acc_calculateScore(accrange)
    ranking = acc_setRanking(score)
    return ranking