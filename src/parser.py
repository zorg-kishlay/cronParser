import sys

from cron_parser import Parser

if __name__ == '__main__':
    arg_count = len(sys.argv)
    if arg_count == 1:
        raise Exception("Please pass the cron expression as argument")
    expression = sys.argv[1]
    # "*/15 0 1,15 * 1-5 /usr/bin/find"
    parser = Parser(expression)
    #parser= Parser("*/15 0 1,15 * 1-5 /usr/bin/find")
    parser.parser()
