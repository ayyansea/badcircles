from .accuracy import acc_Analyze, acc_setRanking
    

def plays_accAnalyze(plays: list) -> float:
    acc_score = 0
    for play in plays:
        acc = acc_Analyze(play.accuracy * 100)
        acc_score += acc[1]
        
    ranking = acc_setRanking(acc_score / len(plays)) 
    return ranking


        