"""
prefix_to_postfix

Module containing a class for for converting a mathematical prefix expression 
to a postfix expression

Author: Rani Hinnawi
Date: 2023-07-04
"""
from typing import Set, Union
from lab1.stack import Stack


class PrefixToPostfix:
    """
    Class that holds valid operators for a prefix mathematical expression, and
    that converts from prefix to postfix ordering.
    """

    def __init__(self, valid_operators: Set[str]) -> None:
        """
        Initialize the PrefixToPostfix class with a set of valid operators.

        Args:
            valid_operators: A set of valid operators allowed in the expressions.
        """
        self._operators = valid_operators

    def convert(self, prefix: str) -> Union[str, ValueError]:
        """
        Function that takes in a mathematical prefix expression as a string and
        outputs the equivalent expression as a postfix. The expression may only
        contain valid operators and alphabetical operands

        Args:
            prefix: the prefix expression string
        """
        operands = Stack()
        for item in reversed(prefix):
            if (item in self._operators):
                first = operands.pop()
                second = operands.pop()

                # Error case: not enough operands. Operator needs two
                if (first is None or second is None):
                    error = "INVALID PREFIX: the expression contains too many"
                    error += " operators"
                    raise ValueError(error)

                expression = first + second + item
                operands.push(expression)
            elif (item.isalpha()):
                operands.push(item)
            else:
                # Error case: inputted character is invalid
                error = f"INVALID CHAR: the item '{item}' is an invalid"
                error += " character"
                raise ValueError(error)

        # Error case: no more operators, but more than one operand remains
        if (operands.size() != 1):
            error = "INVALID PREFIX: the expression contains too many operands"
            raise ValueError(error)

        # Return the postfix expression
        return operands.peek()
