# Part 1 - a small "find" tool (like a simplified `grep`).
#
# This is a COMMAND-LINE program: you run it from the terminal and pass it
# arguments, e.g.   python find.py apple sample.txt
#
# The argument parser is started for you. Finish the TODOs below.

import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Print the lines of a file that contain a given pattern.")
    parser.add_argument("pattern", help="the text to look for")
    parser.add_argument("filename", help="the file to search")
    parser.add_argument("-i", "--ignore-case", action="store_true")

    args = parser.parse_args() 

    with open(args.filename, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if args.ignore_case:
                if args.pattern.lower() in line.lower():
                    print(f"{line_number}: {line.strip()}")
                else:
                    match = args.pattern in line
                if match:
                    print(f"{line_number}: {line.strip()}")


    
    # TODO: open args.filename and read its lines. For each line, numbered starting
    #   at 1, print "<number>: <line>" when the line contains args.pattern.
    #   If the --ignore-case flag was given, match without caring about upper/lower
    #   case (hint: compare the lowercased versions of both).


if __name__ == "__main__":
    main()
