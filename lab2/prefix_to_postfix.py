"""
prefix_to_postfix

Module containing a class for for converting a mathematical prefix expression 
to a postfix expression

Author: Rani Hinnawi
Date: 2023-07-04
"""
from typing import Set, Union
from support.stack import Stack


class PrefixToPostfix:
    """
    Class that holds valid operators for a prefix mathematical expression, and
    that converts from prefix to postfix ordering.
    """

    def __init__(self, valid_operators: Set[str], recursive: bool) -> None:
        """
        Initialize the PrefixToPostfix class with a set of valid operators.

        Args:
            valid_operators: A set of valid operators allowed in the expressions.

        Returns:
            current instance of PrefixToPostfix converter class
        """
        self._operators = valid_operators
        self._recursive = recursive

    def convert(self, prefix: str) -> Union[str, ValueError]:
        """
        Wrapper method that converts a mathematical prefix expression to a
        postfix one. It runs an iterative or a recursive implementation based
        on current instance of PrefixToPostfix object's 'recursive' property.

        Args:
            prefix: the prefix expression string

        Returns:
            str: The postfix expression if successful conversion is possible.
        """
        if (self._recursive):
            return self._convert_recursive(prefix)

        return self._convert_iterative(prefix)

    def _convert_recursive(self, prefix: str) -> Union[str, ValueError]:
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
        # TODO: Fix and finish implementation
        # TODO: incorporate recursive depth limiter

        def helper(i=0) -> Union[str, ValueError]:
            """
            Helper function that takes in a starting index i and recursively 
            converts a substring of the prefix expression into a postfix
            expression. The function is expected to parse an 
            operator-operand-operand or just an operand substring. Only call
            when prefix is non-empty string.

            Args:
                i (int, optional): starting index for a substring of the prefix
                    expression to be parsed. Defaults to 0 if not provided.

            Returns:
                str: The postfix expression if successful conversion is
                    possible.

            Raises:
                ValueError: If an invalid character is passed in or if there
                    are too many operators
            """
            if (i >= len(prefix)):
                # Error case: not enough operands. Operator needs two
                error = "INVALID PREFIX: the expression contains too many"
                error += " operators"
                raise ValueError(error)

            item = prefix[i]

            # Convert
            if (item.isalpha()):
                return item
            elif (item in self._operators):
                first = helper(i + 1)
                second = helper(len(first) + 1)
                return first + second + item
            else:
                # Error case: inputted character is invalid
                error = f"INVALID CHAR: the item '{item}' is an invalid"
                error += " character"
                raise ValueError(error)

        # Run conversion
        if (len(prefix) == 0):
            # Case: Valid empty string passed in
            return prefix

        postfix = helper()
        if (len(postfix) < len(prefix)):
            # Error case: operands remain after initial operators are visited,
            # meaning there are too many operands
            error = "INVALID PREFIX: the expression contains too many operands"
            raise ValueError(error)

        return postfix

    def _convert_iterative(self, prefix: str) -> Union[str, ValueError]:
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
