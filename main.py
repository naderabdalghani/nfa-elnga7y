import sys
import re

from constansts import NUM_INPUT_ARGUMENTS
from pretty_printer import PrettyPrinter

printer = PrettyPrinter()


def validate_regex(regex):
    try:
        re.compile(regex)
    except re.error as error:
        printer("Invalid regular expression entered: " + error.msg, level=PrettyPrinter.ERROR)
        input("\n\nPress Enter to exit...")
        sys.exit(1)


def parse_regex(regex):
    pass


def construct_nfa(regex):
    pass


def main(regex):
    validate_regex(regex)


if __name__ == '__main__':
    if len(sys.argv) > NUM_INPUT_ARGUMENTS:
        printer("Too many input arguments", PrettyPrinter.ERROR)
        input("\n\nPress Enter to exit...")
        sys.exit(1)
    elif len(sys.argv) < NUM_INPUT_ARGUMENTS:
        printer("Too few input arguments. Please enter a single regular expression enclosed by single or double quotes"
                " e.g '01|23'", PrettyPrinter.ERROR)
        input("\n\nPress Enter to exit...")
        sys.exit(1)

    main(sys.argv[2])
