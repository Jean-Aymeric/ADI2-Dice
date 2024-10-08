from abc import ABC, abstractmethod
from typing import final


class Message(ABC):
    __text: str

    @property
    def Text(self) -> str:
        return self.__text

    @Text.setter
    def Text(self, text: str) -> None:
        self.__text = text

    def __init__(self, text: str = ""):
        self.__text = text

    @final
    def display(self) -> None:
        print(self._displayLeftExtended() + self.__text + self._displayRightExtended())

    @abstractmethod
    def _displayLeftExtended(self) -> str:
        pass

    @abstractmethod
    def _displayRightExtended(self) -> str:
        pass
