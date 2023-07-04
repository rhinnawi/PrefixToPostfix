"""
run_conversions

This module contains the primary function for running the conversion, logging
performance metrics, and outputting results to a text file. It also inclues
helper functions for error-checking the IO

Author: Rani Hinnawi
Date: 2023-07-04
"""
from typing import TextIO
from lab1.prefix_to_postfix import PrefixToPostfix
from lab1.performance import Performance
from lab1.output_formatters import format_conversion_results, \
    format_performance_report


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
        out.write("-------Conversion Results-------\n")

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
