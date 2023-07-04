"""
This is the entry point for the lab1 package. It runs when explicity called and
not by default when the package is imported.
"""
from sys import stderr
from pathlib import Path
import argparse
from lab1 import run_conversions

# Set up command line argument parsing
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("input_file", type=str, help="Input File Pathname")
arg_parser.add_argument("output_file", type=str, help="Output File Pathname")
arg_parser.add_argument("--debug", action="store_true",
                        help="Toggles debug mode for development work")
args = arg_parser.parse_args()

# Convert file names into paths
in_file = Path(args.input_file)
out_file = Path(args.output_file)

# Run main program
if (not in_file.exists()):
    # ERROR: invalid input path name
    error = f"ERROR: input file path {in_file} does not exist"

    if (out_file.parent.exists()):
        with open(out_file, 'w', encoding="utf-8") as file:
            file.write(error)
    else:
        error += f". The output file path {out_file} is also invalid."
        print(error, file=stderr)
elif (not out_file.parent.exists()):
    print(f"ERROR: output file path {out_file} is invalid", file=stderr)
else:
    run_conversions(input_file=in_file, output_file=out_file)
