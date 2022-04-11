from enum import Enum


class ScoreCriteria(Enum):
    SS = 6
    S = 5
    A = 4
    B = 3
    C = 2
    D = 1


class AccCriteria(Enum):
    """
    Rank = (Lower, Upper)
    """

    SS = ("SS", (99, 100))
    S = ("S", (98, 99))
    A = ("A", (96, 98))
    B = ("B", (94, 96))
    C = ("C", (90, 94))
    D = ("D", (1, 90))


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
