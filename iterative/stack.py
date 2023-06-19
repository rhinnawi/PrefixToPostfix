from typing import List, Optional, TypeVar

# Set up generic type for stack to remain type-agnostic
T = TypeVar('T')


class Stack:
    """
    Stack class implementing the stack ADT, including several optional methods.
    The underlying data structure is a Python List. As a stylistic choice,
    methods that would otherwise return None will return self, allowing for 
    method chaining. 
    """

    def __init__(self) -> None:
        """
        Instantiate an empty stack
        """
        self._stack: List[Optional[T]] = []

    def push(self, item: T) -> 'Stack':
        """"
        Push an item to the top of the stack. 

        Args:
            item: A new item to be placed at the top of the stack

        Returns:
            self: The current stack instance. 
        """
        self._stack.append(item)
        return self

    def pop(self) -> Optional[T]:
        """
        Remove and return the item at the top of the stack.

        Args: None

        Returns:
            None if stack is empty. Otherwise, the top item from the stack
        """
        if (self._stack):
            return self._stack.pop()

        return None

    def peek(self) -> Optional[T]:
        """
        Displays the item at the top of the stack.

        Args: None

        Returns:
            None if stack is empty, otherwise the item at the top of the stack.
        """
        if (self._stack):
            return self._stack[-1]

        return None

    def size(self) -> int:
        """
        Return the total number of items on the stack. 

        Args: None

        Returns:
            Number of items on the stack
        """
        return len(self._stack)

    def is_empty(self) -> bool:
        """
        Checks if stack contains any items.

        Args: None

        Returns:
            True for empty stack or False for stack of size >= 1
        """
        return len(self._stack) == 0
