"""
Module for converting a mathematical prefix expression to a postfix expression
"""
from lab1.stack import Stack


def convert_prefix_to_postfix():
    """
    Function that takes in a mathematical prefix expression as a string and
    outputs the equivalent expression as a postfix.
    """
    temp = Stack()
    temp.push(1)
    temp.push(2)
    print(temp.is_empty())
    print(temp)
    temp.push(3)
    temp.push(4)
    print(temp)
    temp.pop()
    print(temp)
    print('OK')
    return
