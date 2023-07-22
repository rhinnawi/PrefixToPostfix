"""
is_valid_io

This module contains the function that checks for validating the user-provided
input and output file paths. Python typing initially assumes that arguments
are TextIO types, so the function body validates that the paths exist. The
input file must already exist as output depends on its values. Output files
may be newly written, and so only the parent directory must already exist.

Author: Rani Hinnawi
Date: 2023-07-04
"""
from typing import TextIO, Union


def is_valid_io(in_file: TextIO, out_file: TextIO) -> \
        Union[bool, FileNotFoundError]:
    """
    Function that validates that the input and the path to the output exist

    Args:
        in_file: input text file
        out_file: output text file

    Return:
        True if file paths are valid. Otherwise, FileNotFoundError
    """
    error_message = ""
    error = False

    # Validate input path
    if (not in_file.exists()):
        error_message = \
            f"The input file path {in_file} does not exist."
        error = True

    # Validate output path. Incorporate into preexisting error message
    if (not out_file.parent.exists()):
        if (error):
            error_message += " "
        else:
            error = True

        error_message += "The parent directory path to the output file "
        error_message += f"{out_file} does not exist."

    # Raise error if either file is invalid. Otherwise, return True
    if (error):
        raise FileNotFoundError("ERROR: " + error_message)

    return True
