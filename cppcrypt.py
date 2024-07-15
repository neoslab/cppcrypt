# coding: utf-8

# Import libraries
import os
import random
import re
import string
import sys
import argparse


# Class Builder
class CppCrypt:
    version = "1.0.1"

    # @name: __init__()
    # @description: Class initialization
    # @return: self values
    def __init__(self, scriptpath):
        """ Class initialization """
        self.filepath = scriptpath
        self.filebase, self.extension = os.path.splitext(os.path.basename(scriptpath))
        self.validexts = [".cpp", ".h"]

    # @name: namegenerator()
    # @description: Rename all variables and functions
    # @return: string
    def namegenerator(self, givenstring):
        """ Rename all variables and functions """
        varswords = {}
        exclcases = {"typedef", "unsigned"}
        index = 0
        newstring = ""
        splitcode = re.split('\"', givenstring)
        filtercode = re.findall(r"\w+\s+(?!main)\**([a-zA-Z_][a-zA-Z0-9_]*)", givenstring)

        for foundmatch in filtercode:
            if foundmatch not in exclcases and foundmatch not in varswords:
                varswords[foundmatch] = self.randstring(12)

        for section in splitcode:
            if index % 2 == 0:
                for entry in varswords:
                    restring = r"\b{}\b".format(re.escape(entry))
                    while True:
                        firstfound = re.search(restring, section)
                        if not firstfound:
                            break
                        start = firstfound.start(0)
                        end = firstfound.end(0)
                        section = section[:start] + varswords[entry] + section[end:]
            if index >= 1:
                newstring += "\"" + section
            else:
                newstring += section
            index += 1
        return newstring

    # @name: randstring()
    # @description: Generate a random string
    # @return: string
    @staticmethod
    def randstring(string_length=8):
        """ Generate a random string """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(string_length))

    # @name: cleanspaces()
    # @description: Remove whitespace
    # @return: string
    @staticmethod
    def cleanspaces(a):
        """ Remove whitespace """
        splits = re.split('\"', a)
        regexp = r"((\w+\s+)[a-zA-Z_*][a-zA-Z0-9_]*|#.*|return [a-zA-Z0-9_]*|\[\[.\]\]|else)"
        index = 0
        a = ""
        for s in splits:
            if index % 2 == 0:
                s_line = re.sub(r"\s+", "", s)
                s_code = re.findall(regexp, s)
                for code in s_code:
                    old = re.sub(r"\s+", "", code[0])
                    new = code[0]
                    if code[0][0] == '#':
                        new = code[0] + "\n"
                    elif "unsigned" in code[0] or "else" in code[0]:
                        new = code[0] + " "
                    s_line = s_line.replace(old, new)
            else:
                s_line = s

            if index >= 1:
                a += "\"" + s_line
            else:
                a += s_line
            index += 1
        return a

    # @name: cleancomment()
    # @description: Remove C++ comments
    # @return: string
    @staticmethod
    def cleancomment(givenstring):
        """ Remove C++ comments """
        givenstring = re.sub(r"//.*", "", givenstring)
        givenstring = re.sub(r"/\*.*?\*/", "", givenstring, flags=re.DOTALL)
        return givenstring

    # @name: obfuscatefile()
    # @description: Obfuscate the C++ source file
    # @return: string
    def obfuscatefile(self, output_path=None, output_filename=None):
        """ Obfuscate the C++ source file """
        try:
            with open(self.filepath) as file_data:
                filestring = file_data.read()
                filestring = self.cleancomment(filestring)
                filestring = self.namegenerator(filestring)
                filestring = self.cleanspaces(filestring)

                if output_path is None:
                    output_path = os.path.dirname(self.filepath)

                if output_filename is None:
                    output_filename = self.filebase + ".obf"

                output_file = os.path.join(output_path, output_filename + self.extension)

                with open(output_file, "w+") as f:
                    f.write(filestring)
                    print("Obfuscated file saved as: '{}'".format(output_file))
        except IOError as e:
            print("Error: {}".format(e))

    # @name: getversion()
    # @description: Return the script version
    # @return: string
    @staticmethod
    def getversion():
        return CppCrypt.version


# Custom Help Formatter
class CustomHelpFormatter(argparse.HelpFormatter):
    def _format_action_invocation(self, action):
        if not action.option_strings:
            return self._metavar_formatter(action, action.dest)(1)[0]
        parts = []

        if action.nargs == 0:
            parts.extend(action.option_strings)
        else:
            default = action.dest.upper()
            args_string = self._format_args(action, default)
            for option_string in action.option_strings:
                parts.append('%s %s' % (option_string, args_string))
        return ', '.join(parts).replace(' ,', ',')


# Menu function
def main():
    parser = argparse.ArgumentParser(description="CppCrypt - A C++ Source Code Obfuscator",
                                     formatter_class=CustomHelpFormatter)
    parser.add_argument('-p', '--path', type=str, metavar='',
                        help="Full path to the C++ file to be obfuscated.")
    parser.add_argument('-o', '--output', type=str, metavar='',
                        help="Full path for the output file, including the filename.")
    parser.add_argument('-v', '--version', action='store_true',
                        help="Display the current version of CppCrypt.")

    args = parser.parse_args()

    if args.version:
        print("CppCrypt version: {}".format(CppCrypt.getversion()))
        sys.exit(0)

    if args.path:
        if not os.path.isfile(args.path):
            print("Error: The specified path does not exist or is not a file.")
            sys.exit(1)

        obfuscator = CppCrypt(args.path)
        if args.output:
            output_dir = os.path.dirname(args.output)
            if not os.path.isdir(output_dir):
                print("Error: The specified output directory does not exist.")
                sys.exit(1)
            output_filename = os.path.basename(args.output)
            obfuscator.obfuscatefile(output_path=output_dir, output_filename=output_filename)
        else:
            obfuscator.obfuscatefile()
    else:
        parser.print_help()


# Callback
if __name__ == "__main__":
    main()
