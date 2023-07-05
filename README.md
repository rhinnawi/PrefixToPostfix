# Lab 1

This is a self-contained Python package that converts mathematical prefix
expressions into postfix expressions. It does so by leveraging the Stack data
structure to iteratively convert a user-provided strings. Prefix expressions
must be placed line-by-line in an input text file. Results, including
performance metrics, are outputted to a user-specified output file.

## Running Lab 1

1. Download and install Python on your computer
2. Navigate to [this](.) directory (containing the README.md)
3. Run the program as a module: `python -m lab1 -h`. This will print the help message.
4. Run the program as a module (with real inputs): `python -m lab1 <some_input_file> <some_output_file>`
   - Example: `python -m lab1 resources/input/in.txt output.txt`
   - Optional - run the program as a module with errors outputted to stderr:
     `python -m lab1 <some_input_file> <some_output_file> --debug`

Output will be written to the specified output file after processing the input file.

### Lab 1 Usage:

```commandline
usage: python -m lab1 [-h] in_file out_file [--debug]

positional arguments:
  in_file     Input File Pathname
  out_file    Output File Pathname

optional arguments:
  --debug     Toggles debug mode to log errors to stderr
  -h, --help  show this help message and exit
```

Usage statements reference

| Symbol        | Meaning                                                                                                            |
| ------------- | ------------------------------------------------------------------------------------------------------------------ |
| [var]         | variable var is optional.                                                                                          |
| var           | variable var is required. All positional arguments are required.                                                   |
| -v, --version | This refers to a flag. One dash + one letter OR two dashes and a whole word. Some flags take one or more arguments |
| +             | This argument consumes 1 or more values                                                                            |
| \*            | This argument consumes 0 or more values                                                                            |

### Project Layout

- [PrefixToPostfix/](.): The parent or "root" folder containing all of these files
  - [README.md](README.md):
    The guide you're reading.
  - [lab1](lab1):
    This is the _package_.
    - [`__init__.py`](lab1/__init__.py)
      This contains the functionality that is automatically run when importing the package
    - [`__main__.py`](lab1/__main__.py)
      This file is the entrypoint to the Lab 1 package when run as a program
    - `*.py`
      These are python scripts that do the actual work
  - [I/O](resources)
    - `*_input.txt`
      These are the required and custom input files for testing code
    - `*_output.txt`
      These are the output files for data and metrics from input files with same name

### Python Version

3.10.x

### IDE / Editor

Visual Studio Code (WSL: Ubuntu)
