from Parser.base_parser import BaseParser


class DayParser(BaseParser):
    def __init__(self):
        super().__init__(1, 31, "Day")
