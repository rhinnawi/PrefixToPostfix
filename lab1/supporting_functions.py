"""
supporting_functions

This module contains wrapper and helper functions for running the conversion
and outputting results to a text file.

Author: Rani Hinnawi
Date: 2023-07-04
"""
from typing import TextIO
from lab1.prefix_to_postfix import PrefixToPostfix


def generate_output(line_number: int, prefix: str, result: str, error=False) -> str:
    """
    Function that formats the inputted expression and the output given from the
    prefix to postfix conversion.

    Args:
        line_number: integer for labelling lines in the output
        expression: prefix expression string
        result: postfix expression string OR error message
        error: boolean indicating whether result is an error message

    Returns:
        string conditionally formatted based off result type
    """

    write = f"{line_number}. Prefix: {prefix}"

    if (error):
        write += f"\n\tERROR - {result}\n"
    else:
        write += f" || Postfix: {result}\n"

    return write + '\n'


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
    converter = PrefixToPostfix(valid_operators={'+', '-', '*', '/', '$'})

    with open(input_file, 'r', encoding="utf-8") as file, \
            open(output_file, 'w', encoding="utf-8") as out:
        # Counting lines for clean formatting
        line_counter = 1

        # Loop through input file expressions. Convert and send to output file
        for line in file:
            # Remove white spaces and set up output string
            prefix_expression = line.strip()

            try:
                postfix: str = converter.convert(prefix_expression)
                out.write(generate_output(
                    line_counter, prefix_expression, postfix))
            except ValueError as ve:
                error_message = ve.args[0]
                out.write(generate_output(line_counter,
                          prefix_expression, error_message, error=True))
            finally:
                line_counter += 1

        out.write("Done")
