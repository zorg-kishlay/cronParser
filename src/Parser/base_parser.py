from Exceptions.exceptions import InvalidCronExpressionException
from constants import OUTPUT_COLUMN_LENGTH
from logger_config import logger


class BaseParser:
    """
    Base class for all the valid values accepted as arguments like Day,Month,etc
    """
    def __init__(self, low, high, name, **kwargs):
        self.low = low
        self.high = high
        self.name = name

    def parse(self, value: str) -> str:
        """
        The main parse method that is suppose to traverse and parse the expression
        :param value: The Cron expression
        :return: Output as a string
        """
        logger.info(f"Starting parsing for {self.name} value {value}")
        output = [self.name]

        for _ in range(len(self.name), OUTPUT_COLUMN_LENGTH):
            output.append(" ")

        output.append(self.parse_operations(value))

        return "".join(output)

    def parse_operations(self, value: str)-> str:
        """
        This method take cares of the special character encounter and adds values accordingly
        It also internally validates the input expression
        :param value: The expression to be parsed
        :return:
        """
        if "," in value:
            return self.comma_input(value)

        elif "-" in value:
            return self.range_parser(value)

        elif "/" in value:
            return self.step_parser(value)

        elif "*" in value:
            return self.asterix_input(value)

        self.validate(value)
        return value

    def comma_input(self, value: str) -> str:
        """
        This method takes care of comma separated expressions
        :param value: The input expression
        :return: The split value as a string
        """
        params = value.split(",")
        output = []
        for param in params:
            output.append(self.parse_operations(param))
        return " ".join(output)

    def asterix_input(self, value: str) -> str:
        """
        This method takes care of * value in expression
        :param value: The input expression
        :return: The values inside the range as a string
        """
        output = []
        for idx in range(self.low, self.high+1):
            output.append(str(idx))

        return " ".join(output)

    def step_parser(self, value: str) -> str:
        """
        This method takes care of / value in expression
        :param value: The input expression
        :return: The range value as a string
        """
        output = []
        index = value.find("/")
        if value[index - 1] == '*':
            start = self.low
        else:
            self.validate(value[0:index])
            start = int(value[0:index])

        step = int(value[index + 1: len(value)])

        for idx in range(start, self.high + 1, step):
            output.append(str(idx))

        return " ".join(output)

    def range_parser(self, value: str) -> str:
        """
        This method takes care of - value in expression
        :param value: The input expression
        :return: The values inside the range as a string
        """
        length = len(value)
        index = value.find("-")
        output = []
        self.validate(value[0:index])
        self.validate(value[index + 1: length])

        start = int(value[0:index])
        end = int(value[index + 1: length])
        logger.info(f"Inside range parser start {start} and end is {end}")
        for idx in range(start, end + 1):
            output.append(str(idx))

        return " ".join(output)

    def validate(self, value: str) -> None:
        """
        This method validates the values in the expression based in their range
        :param value: The input expression
        :return:
        """
        try:
            integer_value = int(value)
            if self.low <= integer_value <= self.high:
                return

            raise InvalidCronExpressionException(f"{integer_value} not a correct value for {self.name}")

        except Exception as e:
            logger.info(f"Exception occured while validating {self.name}: {e}")
            raise e


