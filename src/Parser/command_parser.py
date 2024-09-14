from Parser.base_parser import BaseParser
from constants import OUTPUT_COLUMN_LENGTH


class CommandParser(BaseParser):
    def __init__(self):
        super().__init__(-1, -1, "Command")

    def parse(self, value: str):
        output = [self.name]
        for _ in range(len(self.name), OUTPUT_COLUMN_LENGTH):
            output.append(" ")
        output.append(value)
        return "".join(output)
