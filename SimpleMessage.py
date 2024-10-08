from typing import final

from Message import Message


class SimpleMessage(Message):
    @final
    def _displayLeftExtended(self) -> str:
        return ""

    @final
    def _displayRightExtended(self) -> str:
        return ""

    def __init__(self, text: str = ""):
        super().__init__(text)
