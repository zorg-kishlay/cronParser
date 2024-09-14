from Parser.base_parser import BaseParser


class WeekParser(BaseParser):
    def __init__(self):
        super().__init__(0, 6, "Week")
