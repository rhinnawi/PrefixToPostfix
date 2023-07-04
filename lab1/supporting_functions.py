"""
supporting_functions

This module contains wrapper and helper functions for running the conversion
and outputting results to a text file.

Author: Rani Hinnawi
Date: 2023-07-04
"""
from typing import TextIO
from lab1.convert_prefix_to_postfix \
    import convert_prefix_to_postfix as converter


def run_conversions(input_file: TextIO, output_file: TextIO) -> None:
    """
    Wrapper function for running prefix to postfix converter using data from an
    input file. Returns results to output file.

    Args:
        input_file: text file from which prefix expressions will be read
        output_file: text file to which results will be written

    Returns:
        None
    """
    with open(input_file, 'r', encoding="utf-8") as file, \
            open(output_file, 'w', encoding="utf-8") as out:
        for line in file:
            expression = line.strip()
            write = f"Prefix: {expression}\n"
            write += f"\tPostfix result: {converter(expression)}\n"
            out.write(write + "\n")

        out.write("Done")
