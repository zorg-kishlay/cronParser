import unittest

from Exceptions.exceptions import InvalidCronExpressionException
from cron_parser import Parser


class TestCronParser(unittest.TestCase):
    def setUp(self):
        self.parse = Parser("*/15 0 1,15 * 1-2 /usr/bin/find")

    def test_parse(self):
        result = self.parse.parser()
        # ['Minute        0 15 30 45', 'Hour          0', 'Day           1 15', 'Month         1 2 3 4 5 6 7 8 9 10 11 12', 'Week          1 2 3 4 5', 'Command       /usr/bin/find']

        expected_result = 'Minute        0 15 30 45\nHour          0\nDay           1 15\nMonth         1 2 3 4 5 6 7 8 9 10 11 12\nWeek          1 2\nCommand       /usr/bin/find'
        self.assertEqual(result, expected_result)

    def test_invalid_cron(self):
        parse = Parser("*/15 0 1,15 * /usr/bin/find")
        with self.assertRaises(InvalidCronExpressionException):
            parse.parser()

    def test_invalid_range_cron(self):
        parse = Parser("*/15 0 1,60 * /usr/bin/find")
        with self.assertRaises(InvalidCronExpressionException):
            parse.parser()


if __name__ == '__main__':
    unittest.main()