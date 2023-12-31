"""
__main__

This is the entry point for the prefix_to_postfix package. It runs when explicity 
called and not by default when the package is imported. It can be called by the
command: python -m prefix_to_postfix input_file output_file [--debug]

The primary functionality lies in the package modules, and not directly in the
main module here.

Author: Rani Hinnawi
Date: 2023-07-25
"""
from sys import stderr
from pathlib import Path
import argparse
from prefix_to_postfix import run_conversions
from support.is_valid_io import is_valid_io

# Set up command line argument parsing
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("input_file", type=str, help="Input File Pathname")
arg_parser.add_argument("output_file", type=str, help="Output File Pathname")
arg_parser.add_argument("--debug", action="store_true",
                        help="Toggles debug mode to log errors to stderr")
arg_parser.add_argument("--iterative", action="store_true",
                        help="Toggles iterative implementation for prefix to \
                        postfix conversion. Default is recursive.")
args = arg_parser.parse_args()

# Convert file names into paths
in_file = Path(args.input_file)
out_file = Path(args.output_file)

# Validate file paths then run main program
try:
    is_valid_io(in_file, out_file)
    run_conversions(in_file, out_file,
                    iterative=args.iterative, debug=args.debug)
except FileNotFoundError as fnfe:
    error_message = fnfe.args[0]
    if (args.debug):
        print(error_message, file=stderr)
