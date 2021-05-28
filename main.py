import sys
import re

from constansts import NUM_INPUT_ARGUMENTS, OPERATORS, OPERATORS_PRECEDENCE, OPERATORS_REQUIRED_OPERANDS, EPSILON
from automaton import do_operation
from pretty_printer import PrettyPrinter

printer = PrettyPrinter()


def validate_regex(regex):
    try:
        re.compile(regex)
    except re.error as error:
        printer("Invalid regular expression entered: " + error.msg, level=PrettyPrinter.ERROR)
        input("\n\nPress Enter to exit...")
        sys.exit(1)


def has_lower_precedence(operator_1, operator_2):
    return OPERATORS_PRECEDENCE.get(operator_1, 0) <= OPERATORS_PRECEDENCE.get(operator_2, 0)


def insert_explicit_concat_operators(infix_tokens):
    if len(infix_tokens) == 1:
        return infix_tokens + ['.', EPSILON]
    infix_tokens_with_concat_symbol = []
    previous_token = None
    for current_token in infix_tokens:
        if previous_token is not None:
            if (current_token not in OPERATORS and previous_token not in OPERATORS) or \
                    (previous_token == '*' and (current_token not in OPERATORS or current_token == '(')) or \
                    (previous_token == ')' and (current_token == '(' or current_token not in OPERATORS)) or \
                    (previous_token not in OPERATORS and current_token == '('):
                infix_tokens_with_concat_symbol.append('.')
        infix_tokens_with_concat_symbol.append(current_token)
        previous_token = current_token
    return infix_tokens_with_concat_symbol


def parse_regex(regex):
    infix_regex = list(regex.strip())
    infix_regex = insert_explicit_concat_operators(infix_regex)
    postfix_regex = []
    operators_stack = []
    for token in infix_regex:
        if token in OPERATORS:
            if token == '(':
                operators_stack.append(token)
            elif token == ')':
                popped_token = operators_stack.pop()
                while popped_token != '(':
                    postfix_regex.append(popped_token)
                    popped_token = operators_stack.pop()
            else:
                while len(operators_stack) != 0 and has_lower_precedence(token, operators_stack[-1]):
                    postfix_regex.append(operators_stack.pop())
                operators_stack.append(token)
        else:
            postfix_regex.append(token)
    operators_stack.reverse()
    postfix_regex += operators_stack
    return postfix_regex


def construct_nfa(postfix_regex):
    operands_stack = []
    for token in postfix_regex:
        if token not in OPERATORS:
            operands_stack.append(token)
        else:
            num_required_operands = OPERATORS_REQUIRED_OPERANDS.get(token, 2)
            operands = []
            for i in range(num_required_operands):
                if len(operands_stack) == 0:
                    operands.append(EPSILON)
                    operands.reverse()
                    break
                operands.append(operands_stack.pop())
            operands.reverse()
            operands_stack.append(do_operation(operands, token))
    return operands_stack.pop()


def main(regex):
    validate_regex(regex)
    postfix_regex = parse_regex(regex)
    nfa = construct_nfa(postfix_regex)
    nfa.print_to_file()
    nfa.render_image()


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
