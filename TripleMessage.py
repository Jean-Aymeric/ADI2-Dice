from typing import final

from Message import Message


class TripleMessage(Message):
    @final
    def _displayLeftExtended(self) -> str:
        return self.Text

    @final
    def _displayRightExtended(self) -> str:
        return self.Text

    def __init__(self, text: str = ""):
        super().__init__(text)
