from Parser.base_parser import BaseParser


class HourParser(BaseParser):
    def __init__(self):
        super().__init__(0, 23, "Hour")
