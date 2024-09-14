from Parser.base_parser import BaseParser


class MinuteParser(BaseParser):
    def __init__(self):
        # self.low = 0
        # self.high = 59
        # self.name = "Minute"
        super().__init__(low=0,high=59,name="Minute")
