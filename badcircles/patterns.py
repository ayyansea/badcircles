from enum import Enum


class MemePatterns(Enum):
    BLUEZENITH = [["^.*727.*$"], "WYSI"]
    AZER = [["^.*azer.*$", "^.*азер.*$"], "Azer isn't so great? Are you kidding me?"]
    BRAINPOWER = [
        ["^.*brain power.*$", "^.*брейн павер.*$"],
        "O-oooooooooo AAAAE-A-A-I-A-U- JO-oooooooooooo AAE-O-A-A-U-U-A- E-eee-ee-eee AAAAE-A-E-I-E-A-JO-ooo-oo-oo-oo EEEEO-A-AAA-AAA",
    ]
    BELLYBUTTON = [["^.*пуп[к|о][кеиа|ов|ом|ам(и)?|ах]*$"], "где мое перо?"]


class ReplyPatterns(Enum):
    ONEMISS = [["^.*Hitcounts: (\d+\/)+1.*$"], "1 miss rip bruh"]


class GreetingPatterns(Enum):
    PRIVET = [["^прив(яу)?(ет)?(ик|ки)?и?$"], "привет привет"]
    ZDAROVA = [["^здарова$"], "здарова"]
