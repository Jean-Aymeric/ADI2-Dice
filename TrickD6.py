from random import randint

from D6 import D6


class TrickD6(D6):
    def __init__(self):
        super().__init__()

    def roll(self) -> int:
        return randint(5, 6)
