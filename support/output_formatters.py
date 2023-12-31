"""
output_formatters

This module contains helper functions called to format strings intended to be
outputted to a text file.

Author: Rani Hinnawi
Date: 2023-07-25
"""
from support.performance import Performance


def format_conversion_results(line_number: int, prefix: str, result: str,
                              metrics: str, error=False) -> str:
    """
    Function that formats the inputted expression and the output given from the
    prefix to postfix conversion.

    Args:
        line_number (int): number for labelling lines in the output
        expression (str): prefix expression
        result (str): postfix expression OR error message
        metrics (str): string representation of Performance values (size, runtime)
        error (bool): indicator of whether result is an error message

    Returns:
        str: conditionally formatted results based off result type
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
        metrics (Performance): Performance object with logged metrics data

    Returns:
        str: logged successes and failures, formatted to suit a text file
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

    write += "\nFormat:\n\tstring_size: [runtime1, ..., runtimeN]"
    write += "\n\tNOTE: Runtimes measured in nanoseconds (ns)\n"
    return write
