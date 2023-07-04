"""
convert_prefix_to_postfix

Module for converting a mathematical prefix expression to a postfix expression

Author: Rani Hinnawi
Date: 2023-07-04
"""
from lab1.stack import Stack

operators = {'+', '-', '*', '/', '$'}


def convert_prefix_to_postfix(prefix: str, debug=False) -> str:
    """
    Function that takes in a mathematical prefix expression as a string and
    outputs the equivalent expression as a postfix.
    """
    operands = Stack()
    for item in reversed(prefix):
        if (item in operators):
            first = operands.pop()
            second = operands.pop()

            # Error case: not enough operands. Operator needs two
            if (first is None or second is None):
                return "INVALID PREFIX: the expression contains too many operators"

            expression = first + second + item
            operands.push(expression)
        elif (item.isalpha()):
            operands.push(item)
        else:
            # Error case: inputted character is invalid
            return f"INVALID CHAR: the item '{item}' is an invalid character."

    if (debug):
        print("DEBUGGING")

    # Error case: no more operators, but more than one operand remains
    if (operands.size() != 1):
        return "INVALID PREFIX: the expression contains too many operands"

    # Return the postfix expression
    return operands.peek()
