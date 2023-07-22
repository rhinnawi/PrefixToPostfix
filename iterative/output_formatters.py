"""
output_formatters

This module contains helper functions called to format strings intended to be
outputted to a text file.

Author: Rani Hinnawi
Date: 2023-07-23
"""
from iterative.performance import Performance


def format_conversion_results(line_number: int, prefix: str, result: str,
                              metrics: str, error=False) -> str:
    """
    Function that formats the inputted expression and the output given from the
    prefix to postfix conversion.

    Args:
        line_number: integer for labelling lines in the output
        expression: prefix expression string
        result: postfix expression string OR error message
        metrics: string representation of Performance values (size, runtime)
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


def format_performance_report(metrics: 'Performance') -> str:
    """
    Function that formats the size and runtime data logged for each success and
    failure into a report. Runtimes are outputted by size in order from 
    smallest to largest.

    Args:
        metrics: instance of the Performance class with logged metrics data

    Returns:
        string of logged successes and failures, formatted to suit a text file
    """
    write = "\n-------Performance Report-------\n"

    # Note total number of successes and successes per size
    write += f"Total number of successes: {metrics.get_num_successes()}\n"

    successes = metrics.get_successes()
    for size in sorted(successes.keys()):
        runtime = sorted(successes[size])
        write += f"{size}: {runtime}\n"

    write += "\n"

    # Note total number of errors and errors per size
    write += f"Total number of errors: {metrics.get_num_errors()}\n"

    errors = metrics.get_errors()
    for size in sorted(errors.keys()):
        runtime = sorted(errors[size])
        write += f"{size}: {runtime}\n"

    return write
