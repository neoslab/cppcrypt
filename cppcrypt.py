import os
import random
import re
import string


class CppCrypt:

    def __init__(self, scriptpath):
        """ Class initialization """
        self.filepath = scriptpath
        self.filebase, self.extension = os.path.splitext(os.path.basename(scriptpath))
        self.validexts = [".cpp", ".h"]

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

    @staticmethod
    def randstring(string_length=8):
        """ Generate a random string """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(string_length))

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

    @staticmethod
    def cleancomment(givenstring):
        """ Remove C++ comments """
        givenstring = re.sub(r"//.*", "", givenstring)
        givenstring = re.sub(r"/\*.*?\*/", "", givenstring, flags=re.DOTALL)
        return givenstring

    def obfuscatefile(self):
        """ Obfuscate the C++ source file """
        try:
            with open(self.filepath) as file_data:
                filestring = file_data.read()
                filestring = self.cleancomment(filestring)
                filestring = self.namegenerator(filestring)
                filestring = self.cleanspaces(filestring)

                output_path = input("Enter the output path (leave blank for current directory): ").strip()
                if not output_path:
                    output_path = os.path.dirname(self.filepath)

                output_filename = input("Enter the output filename (without extension): ").strip()
                if not output_filename:
                    output_filename = self.filebase + ".obf"

                output_file = os.path.join(output_path, output_filename + self.extension)

                with open(output_file, "w+") as f:
                    f.write(filestring)
                    print("Obfuscated file saved as: '{}'".format(output_file))
        except IOError as e:
            print("Error: {}".format(e))


if __name__ == "__main__":
    filepath = input('Path to C++ Source File: ')
    obfuscator = CppCrypt(filepath)
    obfuscator.obfuscatefile()
