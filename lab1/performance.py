"""
performance

This module holds a class that logs metrics and performance

Author: Rani Hinnawi
Date: 2023-07-04
"""
from sys import stderr
from time import time_ns


class Performance:
    """
    Class for logging space and time performance based stored size and runtime.
    Methods that would otherwise return None instead return current instance to
    allow for method chaining.
    """

    def __init__(self) -> None:
        """
        Creates instance of Performance class that saves start time, stop time,
        and size of input
        """
        self._size = 0
        self._start_time = time_ns()
        self._stop_time = time_ns()

    def __str__(self):
        """
        Returns a string representation of the Performance class
        """
        return f"Size: {self._size}, Runtime: {self.get_runtime}"

    def set_size(self, size: int) -> 'Performance':
        """
        Setter method for size attribute

        Args:
            size: user-defined size of a process. Must be >= 0

        Returns:
            Current instance of Performance class with updated size attribute
        """
        if (size < 0):
            print("Invalid size. Must be >= 0. Automatically setting to 0.",
                  file=stderr)

        self._size = max(size, 0)
        return self

    def get_size(self) -> int:
        """
        Getter method for size attribute

        Args: None

        Returns:
            Stored size of current instance of Performance class
        """
        return self._size

    def start(self) -> 'Performance':
        """
        Setter method for start time. Essentially starts a timer in nanoseconds

        Args: None

        Returns: 
            Current instance of Performance class with updated _start_time
                attribute
        """
        self._start_time = time_ns()
        return self

    def stop(self) -> 'Performance':
        """
        Setter method for stop time. Essentially ends a timer in nanoseconds

        Args: None

        Returns: 
            Current instance of Performance class with updated _stop_time
                attribute
        """
        self._stop_time = time_ns()
        return self

    def get_runtime(self) -> int:
        """
        Returns runtime based off stored start and stop times. If start is
        stored after stop time, returns 0

        Args: None

        Returns:
            Difference between currently stored start and stop times or 0
        """
        return max(self._stop_time - self._start_time, 0)
