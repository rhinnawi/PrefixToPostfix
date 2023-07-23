"""
prefix_to_postfix

Module containing a class for for converting a mathematical prefix expression 
to a postfix expression

Author: Rani Hinnawi
Date: 2023-07-25
"""
from typing import Set, Tuple, Union
from support.stack import Stack


class PrefixToPostfix:
    """
    Class that holds valid operators for a prefix mathematical expression, and
    that converts from prefix to postfix ordering.
    """

    def __init__(self, valid_operators: Set[str], iterative: bool)\
            -> None:
        """
        Initialize the PrefixToPostfix class with a set of valid operators.

        Args:
            valid_operators (Set[char]): A set of valid operators allowed in
                the expressions.
            iterative (bool): True for iterative implementation, false for
                recursive

        Returns:
            current instance of PrefixToPostfix converter class
        """
        self._operators = valid_operators
        self._iterative = iterative

    def convert(self, prefix: str) -> str:
        """
        Wrapper method that converts a mathematical prefix expression to a
        postfix one. It runs an iterative or a recursive implementation based
        on current instance of PrefixToPostfix object's 'recursive' property.

        Args:
            prefix (str): the prefix expression

        Returns:
            str: The postfix expression if successful conversion is possible.
        """
        if (self._iterative):
            return self._convert_iterative(prefix)

        return self._convert_recursive(prefix)

    def _convert_recursive(self, prefix: str) -> str:
        """
        Method that takes in a mathematical prefix expression as a string and
        outputs the equivalent expression as a postfix. The expression may only
        contain valid operators and alphabetical operands. This method
        implements a recursive algorithm for the conversion

        Args:
            prefix (str): the prefix expression string

        Returns:
            str: The postfix expression if successful conversion is possible.

        Raises:
            ValueError: If there are any invalid cases, too many operators, or
                too many operands in an invalid prefix expression.
        """
        # TODO: incorporate recursive depth limiter
        def helper(i=0, num_operands=0) -> Tuple[Union[str, None], int, int]:
            if (i >= len(prefix)):
                return None, i, num_operands

            item = prefix[i]

            if (item.isalpha()):
                return item, i, num_operands + 1
            elif (item in self._operators):
                first, i, num_operands = helper(i + 1, num_operands)
                second, i, num_operands = helper(i + 1, num_operands)

                if (first is None or second is None):
                    error = "INVALID PREFIX: the expression contains too many"
                    error += " operators"
                    raise ValueError(error)

                return first + second + item, i, num_operands - 1
            else:
                # Error case: inputted character is invalid
                error = f"INVALID CHAR: the item '{item}' is an invalid"
                error += " character"
                raise ValueError(error)

        # Run conversion
        if (len(prefix) == 0):
            # Case: Valid empty string passed in
            return prefix

        postfix, _, num_operands = helper()
        if num_operands != (len(postfix) - len(prefix) + 1):
            # Error cases: no more operators, but more than one operand remains
            #   OR incorrect operator-operand ordering
            error = "INVALID PREFIX: the expression contains too many operands"
            error += " OR operands and operators are out of order."
            raise ValueError(error)

        return postfix

    def _convert_iterative(self, prefix: str) -> str:
        """
        Function that takes in a mathematical prefix expression as a string and
        outputs the equivalent expression as a postfix. The expression may only
        contain valid operators and alphabetical operands. This uses the Stack,
        or iterative implementation of the conversion algorithm.

        Args:
            prefix (str): the prefix expression string

        Returns:
            str: The postfix expression if successful conversion is possible.

        Raises:
            ValueError: If there are any invalid cases, too many operators, or
                too many operands in an invalid prefix expression.
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
