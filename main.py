import sys

from constansts import NUM_INPUT_ARGUMENTS
from pretty_printer import PrettyPrinter

printer = PrettyPrinter()


def main():
    pass


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

    regular_expression = sys.argv[2]
