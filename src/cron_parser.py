from Exceptions.exceptions import InvalidCronExpressionException
from Parser.command_parser import CommandParser
from Parser.day_parser import DayParser
from Parser.hour_parser import HourParser
from Parser.minute_parser import MinuteParser
from Parser.month_parser import MonthParser
from Parser.week_parser import WeekParser
from texttable import Texttable


class Parser:
    """
    The Parser class visible to the consumer end
    """
    table = Texttable()
    table.add_row(["Minute", "Hour", "Day of Month", "Month", "Day of Week", "Command"])
    minuteParser = MinuteParser()
    hourParser = HourParser()
    dayParser = DayParser()
    monthParser = MonthParser()
    weekParser = WeekParser()
    commandParser = CommandParser()

    def __init__(self, expression):
        self.expression = expression

    def parser(self):
        """
        The core parser method that serves the client with the output
        and prints the output in a table format
        :return: The output as a string
        """
        value = self.expression
        params = value.split(" ")
        if len(params) != 6:
            raise InvalidCronExpressionException("Incorrect length of cron expression")

        output = []

        # TODO:- Fix this with a switch case maybe
        for idx, component in enumerate(params):
            if idx == 0:
                output.append(self.minuteParser.parse(component))
                continue

            elif idx == 1:
                output.append(self.hourParser.parse(component))
                continue
            elif idx == 2:
                output.append(self.dayParser.parse(component))
                continue

            elif idx == 3:
                output.append(self.monthParser.parse(component))
                continue

            elif idx == 4:
                output.append(self.weekParser.parse(component))
                continue

            elif idx == 5:
                output.append(self.commandParser.parse(component))
                continue

        self.table.add_row(output)
        output = "\n".join(output)
        print(output)
        print(self.table
              .draw())

        return output
