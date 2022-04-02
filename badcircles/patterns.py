from enum import Enum


class MemePatterns(Enum):
    BLUEZENITH = [["^.*727.*$"], "WHEN YOU FUCKING SEE IT"]
    AZER = [["^.*azer.*$", "^.*азер.*$"], "Azer isn't so great? Are you kidding me?"]
    BRAINPOWER = [
        ["^.*brain power.*$", "^.*брейн павер.*$"],
        "O-oooooooooo AAAAE-A-A-I-A-U- JO-oooooooooooo AAE-O-A-A-U-U-A- E-eee-ee-eee AAAAE-A-E-I-E-A-JO-ooo-oo-oo-oo EEEEO-A-AAA-AAA",
    ]
