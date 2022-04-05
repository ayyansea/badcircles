from enum import Enum


class RankingCriteria(Enum):
    """
    Rank = (Name, Score)
    """

    SS = ("SS", 6)
    S = ("S", 5)
    A = ("A", 4)
    B = ("B", 3)
    C = ("C", 2)
    D = ("D", 1)


class AccCriteria(Enum):
    """
    Rank = (Lower, Upper)
    """

    SS = (99, 100)
    S = (98, 99)
    A = (96, 98)
    B = (94, 96)
    C = (90, 94)
    D = (1, 90)


class LengthCriteria(Enum):
    """
    Length = (Name, (Lower, Upper))
    """

    SS = ("SS", (300, 6000))
    S = ("S", (240, 300))
    A = ("A", (180, 240))
    B = ("B", (120, 180))
    C = ("C", (60, 120))
    D = ("D", (0, 60))
