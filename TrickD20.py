from random import randint

from D20 import D20


class TrickD20(D20):
    def __init__(self):
        super().__init__()

    def roll(self) -> int:
        return randint(15, 20)
