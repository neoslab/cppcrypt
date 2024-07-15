# CppCrypt

CppCrypt is a Python script designed to obfuscate C++ source code by renaming variables and functions, removing comments, and cleaning up whitespace. This can be useful for protecting intellectual property or simply making the code harder to read and reverse-engineer.

* * *

## Features

- **Variable and Function Renaming**: Automatically generates random names for variables and functions, making the code harder to understand.
- **Comment Removal**: Strips out all comments from the C++ code.
- **Whitespace Cleanup**: Removes unnecessary whitespace while preserving the readability of certain elements like preprocessor directives and certain keywords.

## Installation

Ensure you have Python installed on your system. This script does not require any external dependencies.

## Usage

1. Save the script as `cppcrypt.py`.
2. Run the script with Python:

```shell
python cppcrypt.py
```

3. Follow the prompts to provide the path to the C++ source file you want to obfuscate.
4. Specify the output path and filename when prompted, or leave blank to use the default options.

## Example

```shell
$ python cppcrypt.py
Path to C++ Source File: /path/to/your/file.cpp
Enter the output path (leave blank for current directory): 
Enter the output filename (without extension): obfuscated_file
Obfuscated file saved as: '/path/to/your/obfuscated_file.cpp'
```

## Script Details

### Class: `CppCrypt`

**Attributes:**
- `filepath`: Path to the C++ source file.
- `filebase`: Base name of the file.
- `extension`: File extension.
- `validexts`: List of valid file extensions for C++ source files.

**Methods:**

- `__init__(self, scriptpath)`: Initializes the class with the given file path.
- `namegenerator(self, givenstring)`: Renames all variables and functions in the given string.
- `randstring(string_length=8)`: Generates a random string of lowercase letters.
- `cleanspaces(a)`: Removes unnecessary whitespace from the given string.
- `cleancomment(givenstring)`: Removes all C++ comments from the given string.
- `obfuscatefile(self)`: Main method to obfuscate the C++ source file.

### Method Details

- **`__init__`**: 
  Initializes the `CppCrypt` class with the path to the C++ source file. Splits the file path into the base name and extension, and checks for valid extensions.

- **`namegenerator`**:
  - Splits the input code by quotes to handle string literals separately.
  - Finds all variable and function names using regular expressions, excluding certain keywords.
  - Replaces these names with randomly generated strings.

- **`randstring`**:
  Generates a random string of a specified length (default is 8 characters).

- **`cleanspaces`**:
  - Splits the input code by quotes to handle string literals separately.
  - Removes unnecessary whitespace while preserving the format of preprocessor directives and certain keywords.

- **`cleancomment`**:
  Removes both single-line (`//`) and multi-line (`/* ... */`) comments from the code.

- **`obfuscatefile`**:
  - Reads the input file.
  - Cleans comments, renames variables and functions, and removes unnecessary whitespace.
  - Writes the obfuscated code to the specified output file.

## Building an Executable

To build an executable from the script, follow these steps:

1. Install the required dependencies:

```shell
python -m pip install -r requirements.txt
```

2. Run the `builder.py` script:

```shell
python builder.py --output <name>
```

## Notes

- This script is intended for obfuscation purposes only. It is not designed to improve or optimize code performance.
- Ensure you have backups of your original code before using this tool, as the obfuscation process is irreversible.
- The script handles basic C++ syntax and common coding patterns but may not cover all edge cases. Review the obfuscated code to ensure it still functions as expected.