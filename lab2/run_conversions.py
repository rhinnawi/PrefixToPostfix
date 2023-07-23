"""
run_conversions

This module contains the primary function for running the conversion. It
assumes valid I/O and determines which operators are valid. While calling the
converter, it logs performance metrics. All results are written to the output
file.

Author: Rani Hinnawi
Date: 2023-07-04
"""
from sys import stderr
from typing import TextIO
from lab2.prefix_to_postfix import PrefixToPostfix
from support.performance import Performance
from support.output_formatters import format_conversion_results, \
    format_performance_report


def run_conversions(input_file: TextIO, output_file: TextIO, iterative=False,
                    debug=False) -> None:
    """
    Wrapper function for running prefix to postfix converter using data from an
    input file. Returns results to output file.

    Args:
        input_file (TextIO): text file from which prefix expressions will be
            read
        output_file (TextIO): text file to which results will be written
        iterative (bool, optional): True for iterative implementation. Defaults
            to False for recursive implementation of conversion.
        debug (bool, optional): True to activate debugging functionality during
            run. Defaults to False.

    Returns:
        None
    """
    performance = Performance()
    converter = PrefixToPostfix(valid_operators={'+', '-', '*', '/', '$'},
                                iterative=iterative, debug=debug)

    with open(input_file, 'r', encoding="utf-8") as file, \
            open(output_file, 'w', encoding="utf-8") as out:
        out.write("-------Conversion Results-------\n")

        # Counting lines for clean formatting
        line_counter = 1

        # Loop through input file expressions. Convert and send to output file
        for line in file:
            # Remove white spaces. Reset output params. Start runtime timer
            prefix_expression = line.strip()

            # Case: empty line in input. Ignore and move onto the next one
            if (len(prefix_expression) == 0):
                continue

            error = False
            result = 'Not run'
            performance.set_size(len(prefix_expression)).start()

            # Run converter. Account for error outputs
            try:
                result = converter.convert(prefix_expression)
            except ValueError as ve:
                result = ve.args[0]
                error = True

                if (debug):
                    error_message = f"{line_counter}. Prefix: "
                    error_message += f"{prefix_expression} | ERROR - {result}"
                    print(error_message, file=stderr)
            finally:
                # Stop timer. Log error / success. Write results to output file
                performance.stop()

                if (error):
                    performance.log_error()
                else:
                    performance.log_success()

                out.write(format_conversion_results(line_counter, prefix_expression,
                                                    result, str(performance), error=error))
                line_counter += 1

        # Log final metrics
        out.write(format_performance_report(performance))

        out.write("\nDone")
