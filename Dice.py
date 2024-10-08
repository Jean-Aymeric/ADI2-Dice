from abc import ABC, abstractmethod
from random import randint
from typing import final


class Dice(ABC):
    __nbSides: int

    def __init__(self, nbSides: int = 6):
        self.__nbSides = nbSides

    @property
    def NbSides(self) -> int:
        return self.__nbSides

    @final
    def roll(self) -> int:
        return randint(1, self.__nbSides) + self._rollExtended()

    @abstractmethod
    def _rollExtended(self) -> int:
        pass
