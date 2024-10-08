from typing import final

from Message import Message


class PrettyMessage(Message):
    @final
    def _displayLeftExtended(self) -> str:
        return "-" * (len(self.Text) + 4) + "\n" + "| "

    @final
    def _displayRightExtended(self) -> str:
        return " |\n" + "-" * (len(self.Text) + 4)

    def __init__(self, text: str = ""):
        super().__init__(text)
