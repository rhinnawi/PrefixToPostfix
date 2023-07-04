"""
Module for converting a mathematical prefix expression to a postfix expression
"""
from lab1.stack import Stack


def convert_prefix_to_postfix(prefix: str, debug=False) -> str:
    """
    Function that takes in a mathematical prefix expression as a string and
    outputs the equivalent expression as a postfix.
    """
    operands = Stack()
    for char in prefix:
        if (char.isalnum()):
            operands.push(char)

    if (debug):
        print("DEBUGGING")

    return str(operands)
