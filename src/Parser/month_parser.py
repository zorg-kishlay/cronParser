from Parser.base_parser import BaseParser


class MonthParser(BaseParser):
    def __init__(self):
        super().__init__(1, 12, "Month")
