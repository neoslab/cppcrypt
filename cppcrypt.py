# coding: utf-8

# Import libraries
import os
import re
import random
import string
import argparse
import sys


# Class CPPCrypt
class CPPCrypt:

    # @name: __init__()
    # @description: Class initialization
    # @return: self values
    def __init__(self):
        """ Class initialization """
        self.version = "1.0.3"
        self.pattern = r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'
        self.cppkeys = {"alignas", "alignof", "and", "and_eq", "asm", "atomic_cancel", "atomic_commit",
                        "atomic_noexcept", "auto", "bitand", "bitor", "bool", "break", "case", "catch", "char",
                        "char8_t", "char16_t", "char32_t", "class", "compl", "concept", "const", "consteval",
                        "constexpr", "const_cast", "continue", "co_await", "co_return", "co_yield", "decltype",
                        "default", "delete", "do", "double", "dynamic_cast", "else", "enum", "explicit", "export",
                        "extern", "false", "float", "for", "friend", "goto", "if", "inline", "int", "long",
                        "mutable", "namespace", "new", "noexcept", "not", "not_eq", "nullptr", "operator", "or",
                        "or_eq", "private", "protected", "public", "register", "reinterpret_cast", "requires",
                        "return", "short", "signed", "sizeof", "static", "static_assert", "static_cast", "struct",
                        "switch", "synchronized", "template", "this", "thread_local", "throw", "true", "try",
                        "typedef", "typeid", "typename", "union", "unsigned", "using", "virtual", "void",
                        "volatile", "wchar_t", "while", "xor", "xor_eq"}
        self.cpplibs = {"abort",
                        "accumulate",
                        "adjacent_find",
                        "advance",
                        "AF_INET",
                        "AF_INET6",
                        "algorithm",
                        "all_of",
                        "any_of",
                        "array",
                        "async",
                        "at_quick_exit",
                        "atexit",
                        "atomic",
                        "back_inserter",
                        "begin",
                        "binary_search",
                        "bind",
                        "bitset",
                        "bsearch",
                        "c_str",
                        "calloc",
                        "cbegin",
                        "cend",
                        "cerr",
                        "char_traits",
                        "chdir",
                        "chrono",
                        "cin",
                        "clamp",
                        "clearenv",
                        "clock",
                        "clog",
                        "complex",
                        "condition_variable",
                        "copy",
                        "count",
                        "count_if",
                        "cout",
                        "crbegin",
                        "crend",
                        "decay",
                        "default_random_engine",
                        "deque",
                        "difftime",
                        "dirpath",
                        "distance",
                        "domain_error",
                        "duration_cast",
                        "enable_if",
                        "end",
                        "endl",
                        "equal",
                        "EVP_DigestFinal_ex",
                        "EVP_DigestInit_ex",
                        "EVP_DigestUpdate",
                        "EVP_MAX_MD_SIZE",
                        "EVP_md5",
                        "EVP_MD_CTX",
                        "EVP_MD_CTX_create",
                        "EVP_MD_CTX_destroy",
                        "EVP_MD_CTX_init",
                        "exception",
                        "exit",
                        "experimental",
                        "false_type",
                        "fenv",
                        "find",
                        "find_end",
                        "find_first_of",
                        "find_if",
                        "for_each",
                        "forward",
                        "forward_list",
                        "free",
                        "freeifaddrs",
                        "function",
                        "future",
                        "generate",
                        "generate_n",
                        "getenv",
                        "getifaddrs",
                        "getline",
                        "gets",
                        "gmtime",
                        "greater",
                        "hash",
                        "hex",
                        "ifa_addr",
                        "ifa_name",
                        "ifa_next",
                        "ifaddrs",
                        "INET6_ADDRSTRLEN",
                        "INET_ADDRSTRLEN",
                        "inet_ntop",
                        "iota",
                        "is_heap",
                        "is_sorted",
                        "isfinite",
                        "isnan",
                        "iter_swap",
                        "latch",
                        "launch",
                        "lexicographical_compare",
                        "list",
                        "localtime",
                        "lock",
                        "lock_guard",
                        "lower_bound",
                        "main",
                        "make_pair",
                        "make_shared",
                        "malloc",
                        "map",
                        "max",
                        "max_element",
                        "memset",
                        "min",
                        "min_element",
                        "minmax",
                        "minmax_element",
                        "mismatch",
                        "mkdir",
                        "mktime",
                        "move",
                        "mt19937",
                        "mutex",
                        "namespace",
                        "next",
                        "next_permutation",
                        "none_of",
                        "now",
                        "nth_element",
                        "numeric_limits",
                        "ofstream",
                        "ostream",
                        "overflow_error",
                        "packaged_task",
                        "pair",
                        "partial_sort",
                        "partial_sort_copy",
                        "partial_sum",
                        "partition",
                        "partition_copy",
                        "permutation",
                        "perror",
                        "piecewise_construct",
                        "placeholders",
                        "plus",
                        "printf",
                        "priority_queue",
                        "promise",
                        "puts",
                        "qsort",
                        "queue",
                        "rand",
                        "random_device",
                        "ratio",
                        "realloc",
                        "recursive_mutex",
                        "reduce",
                        "ref",
                        "reference_wrapper",
                        "regex",
                        "remove",
                        "remove_copy",
                        "remove_copy_if",
                        "remove_if",
                        "rename",
                        "reverse",
                        "reverse_copy",
                        "rmdir",
                        "rotate",
                        "rotate_copy",
                        "runtime_error",
                        "sa_family",
                        "scanf",
                        "scoped_lock",
                        "seconds",
                        "set",
                        "set_difference",
                        "set_intersection",
                        "set_symmetric_difference",
                        "set_union",
                        "setenv",
                        "shared_future",
                        "shared_lock",
                        "shared_mutex",
                        "shared_ptr",
                        "shuffle",
                        "sin6_addr",
                        "sin_addr",
                        "sleep",
                        "snprintf",
                        "sockaddr_in",
                        "sockaddr_in6",
                        "sort",
                        "sort_heap",
                        "span",
                        "sprintf",
                        "srand",
                        "stable_partition",
                        "stable_sort",
                        "stack",
                        "stacktrace",
                        "stacktrace_entry",
                        "static_pointer_cast",
                        "std",
                        "stod",
                        "stof",
                        "stoi",
                        "stol",
                        "stold",
                        "stoll",
                        "stoul",
                        "strftime",
                        "string",
                        "string_literals",
                        "strlen",
                        "swap",
                        "system",
                        "system_clock",
                        "system_error",
                        "thread",
                        "throw_with_nested",
                        "time",
                        "time_point",
                        "time_since_epoch",
                        "time_t",
                        "tm",
                        "to_chars",
                        "to_string",
                        "to_wstring",
                        "transform",
                        "tuple",
                        "type_index",
                        "type_info",
                        "type_traits",
                        "unique",
                        "unique_copy",
                        "unordered_map",
                        "unordered_set",
                        "unsetenv",
                        "upper_bound",
                        "variant",
                        "vector",
                        "weak_ptr",
                        "wstring"}
        self.cppexts = ".obf.cpp"
        self.filemap = {}

    # @name: obfuscatefile()
    # @description: Return obfuscated file
    # @return: string
    def obfuscatefile(self, filepath, fullpath=None, pathfile=None):
        """ Return obfuscated file """
        if not os.path.isfile(filepath):
            print(f"Error: {filepath} is not a valid file path.")
            return
        obflines = []
        with open(filepath, 'r') as file:
            for line in file:
                if line.strip().startswith("#include") or \
                        line.strip().startswith("#ifdef") or \
                        line.strip().startswith("#else") or \
                        line.strip().startswith("#endif") or \
                        line.strip().startswith("#define"):
                    obflines.append(line)
                    continue
                obfentry = self.obfuscateline(line)
                obflines.append(obfentry)
        if not fullpath:
            fullpath = os.path.dirname(filepath)
        if not pathfile:
            pathfile = os.path.splitext(os.path.basename(filepath))[0] + self.cppexts
        finalpath = os.path.join(fullpath, pathfile)
        with open(finalpath, 'w') as outputfile:
            outputfile.writelines(obflines)
        print(f"Obfuscated file saved as: {finalpath}")

    # @name: obfuscateline()
    # @description: Return obfuscated line
    # @return: string
    def obfuscateline(self, line):
        """ Return obfuscated line """
        if line.strip().startswith("#include") or \
                line.strip().startswith("#ifdef") or \
                line.strip().startswith("#else") or \
                line.strip().startswith("#endif") or \
                line.strip().startswith("#define"):
            return line
        line = self.cleancomment(line)
        segments = re.split(r'(".*?")', line)
        for i, segment in enumerate(segments):
            if i % 2 == 0:  # only clean and obfuscate code, not string literals
                segment = self.cleanspaces(segment)
                segment = self.obfuscatecode(segment)
            segments[i] = segment
        return ''.join(segments)

    # @name: obfuscate_code()
    # @description: Return obfuscated code
    # @return: string
    def obfuscatecode(self, segment):
        """ Return obfuscated code """

        def replace(match):
            word = match.group(0)
            if word in self.cppkeys or word in self.cpplibs:
                return word
            if word in self.filemap:
                return self.filemap[word]
            else:
                newname = self.namegenerator()
                self.filemap[word] = newname
                return newname

        return re.sub(self.pattern, replace, segment)

    # @name: namegenerator()
    # @description: Rename all variables and functions
    # @return: string
    @staticmethod
    def namegenerator():
        part1 = ''.join(random.choice(string.ascii_lowercase) for _ in range(1))
        part2 = ''.join(random.choice(string.digits) for _ in range(6))
        part3 = ''.join(random.choice(string.ascii_lowercase) for _ in range(2))
        part4 = ''.join(random.choice(string.digits) for _ in range(1))
        return f"ox{part1}{part2}{part3}{part4}"

    # @name: cleancomment()
    # @description: Remove C++ comments
    # @return: string
    @staticmethod
    def cleancomment(gstring):
        """ Remove C++ comments """
        gstring = re.sub(r"//.*", "", gstring)
        gstring = re.sub(r"/\*.*?\*/", "", gstring, flags=re.DOTALL)
        return gstring

    # @name: cleanspaces()
    # @description: Remove whitespace
    # @return: string
    @staticmethod
    def cleanspaces(line):
        """ Remove whitespace """
        line = line.strip()
        line = re.sub(r'[ \t]+', ' ', line)
        line = re.sub(r'\s*([=+\-*/<>|&%!])\s*', r'\1', line)
        line = re.sub(r'\s*([()\[\]{},;:])\s*', r'\1', line)
        return line

    # @name: getversion()
    # @description: Return the script version
    # @return: string
    @staticmethod
    def getversion():
        return CPPCrypt().version


# Class CustomHelpFormatter
class CustomHelpFormatter(argparse.HelpFormatter):

    # @name: _format_action_invocation()
    # @description: Reformat invocation
    # @return: string
    def _format_action_invocation(self, action):
        """ Reformat invocation """
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


# Main function
def main():
    parser = argparse.ArgumentParser(description="CPPCrypt - A C++ Source Code Obfuscator",
                                     formatter_class=CustomHelpFormatter)
    parser.add_argument('-p', '--path', type=str, metavar='', help="Full path to the C++ file to be obfuscated.")
    parser.add_argument('-o', '--output', type=str, metavar='',
                        help="Full path for the output file, including the filename.")
    parser.add_argument('-v', '--version', action='store_true', help="Display the current version of CPPCrypt.")
    args = parser.parse_args()
    if args.version:
        print("CPPCrypt version: {}".format(CPPCrypt.getversion()))
        sys.exit(0)
    if args.path:
        if not os.path.isfile(args.path):
            print("Error: The specified path does not exist or is not a file.")
            sys.exit(1)
        obfuscator = CPPCrypt()
        if args.output:
            output_dir = os.path.dirname(args.output)
            if not os.path.isdir(output_dir):
                print("Error: The specified output directory does not exist.")
                sys.exit(1)
            pathfile = os.path.basename(args.output)
            obfuscator.obfuscatefile(args.path, fullpath=output_dir, pathfile=pathfile)
        else:
            obfuscator.obfuscatefile(args.path)
    else:
        parser.print_help()


# Example usage:
if __name__ == "__main__":
    main()
