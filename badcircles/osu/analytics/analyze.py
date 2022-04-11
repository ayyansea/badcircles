from . import criteria
from . import utils
from .. import stats
from typing import Tuple


class Analysis:
    """
    Общий класс для хранения аналитических
    сведений о профиле.
    """
    
    def __init__(self, user):
        self.acc = self.analyze_acc(user.statistics.hit_accuracy)
        self.maxcombo = self.analyze_combo(user.statistics.maximum_combo)
        self.topplays = self.analyze_plays(stats.get_top_plays(user.id))
    
    
    def analyze_acc(self, acc: float) -> Tuple:
        acc = int(acc)
        rank = utils.get_ranking(acc, criteria.AccCriteria)
        score = utils.get_score(rank)

        return rank, score
    
    
    def analyze_plays(self, plays: list) -> Tuple:
        acc_score = 0
        length_score = 0
        
        for play in plays:
            accuracy = int(play.accuracy * 100)
            length = play.beatmap.total_length
            
            acc_rank = utils.get_ranking(accuracy, criteria.AccCriteria)
            acc_score += utils.get_score(acc_rank)
            
            length_rank = utils.get_ranking(length, criteria.LengthCriteria)
            length_score += utils.get_score(length_rank)

        length_value = length_score / len(plays)
        acc_value = acc_score / len(plays)
        
        score = utils.average_score(length_value, acc_value)
        rank = utils.get_letter(score)
        
        return rank, score
    
    
    def analyze_combo(self, maxcombo):
        rank = utils.get_ranking(maxcombo, criteria.ComboCriteria)
        score = utils.get_score(rank)
    
        return rank, score
        

    def get_analysis(self):
        
        analysis = ""
        analysis += f"Акка: {self.acc[0]}" + "\n"
        analysis += f"Комбо: {self.maxcombo[0]}" + "\n"
        analysis += f"Топ плеи: {self.topplays[0]}" + "\n"
        
        return analysis
        