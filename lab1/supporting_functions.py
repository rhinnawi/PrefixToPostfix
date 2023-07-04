"""
supporting_functions

This module contains wrapper and helper functions for running the conversion,
logging performance metrics, and outputting results to a text file.

Author: Rani Hinnawi
Date: 2023-07-04
"""
from typing import TextIO
from lab1.prefix_to_postfix import PrefixToPostfix
from lab1.performance import Performance


def generate_output(line_number: int, prefix: str, result: str, metrics: str,
                    error=False) -> str:
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

    write += f"{metrics}\n"

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
    performance = Performance()
    converter = PrefixToPostfix(valid_operators={'+', '-', '*', '/', '$'})

    with open(input_file, 'r', encoding="utf-8") as file, \
            open(output_file, 'w', encoding="utf-8") as out:
        # Counting lines for clean formatting
        line_counter = 1

        # Loop through input file expressions. Convert and send to output file
        for line in file:
            # Remove white spaces. Reset output params. Start runtime timer
            prefix_expression = line.strip()
            error = False
            result = 'Not run'
            performance.set_size(len(prefix_expression)).start()

            # Run converter. Account for error outputs
            try:
                result = converter.convert(prefix_expression)
            except ValueError as ve:
                result = ve.args[0]
                error = True
            finally:
                performance.stop()

                if (error):
                    performance.log_error()
                else:
                    performance.log_success()

                out.write(generate_output(line_counter, prefix_expression,
                                          result, str(performance), error=error))
                line_counter += 1

        out.write("\n")
        out.write(
            f"Total number of successes: {performance.get_num_successes()}\n")

        successes = performance.get_successes()
        for size in sorted(successes.keys()):
            runtime = successes[size]
            out.write(f"{size}: {runtime}\n")

        out.write(f"Total number of errors: {performance.get_num_errors()}\n")

        out.write("\n")

        errors = performance.get_errors()
        for size in sorted(errors.keys()):
            runtime = errors[size]
            out.write(f"{size}: {runtime}\n")

        out.write("Done")
