"""
This is the entry point for the lab1 package. It runs when explicity called and
not by default when the package is imported.
"""
from pathlib import Path
import argparse
from lab1 import convert_prefix_to_postfix as converter

# Set up command line argument parsing
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("--in_file", type=str, help="Input File Pathname")
arg_parser.add_argument("--out_file", type=str, help="Output File Pathname")
arg_parser.add_argument("--debug", action="store_true",
                        help="Toggles debug mode for development work")
args = arg_parser.parse_args()

# Convert file names into paths
in_path = Path(args.in_file)
# out_path = Path(args.out_file)

# Run main program
with open(in_path, 'r', encoding="utf-8") as in_file:
    for line in in_file:
        expression = line.strip()
        print(expression, ':', converter(line.strip(), debug=args.debug))
