#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names Exercise

This script extracts baby names and their rankings from an HTML file.
It produces a list starting with the year, followed by name-rank pairs
sorted alphabetically.

Example:
['1990', 'Aaliyah 91', 'Aaron 57', 'Abigail 895', ...]

Suggested Steps:
- Extract the year and print it.
- Extract names and rank numbers, and print them.
- Get the names into a dictionary and sort them alphabetically.
- Build a list in the required format and print it.
- Enhance main() to handle multiple files and summary options.
"""
filename = "baby1990.html"
def extract_names(filename):
    """
    Extracts the year, names, and ranks from the given HTML file.

    Args:
        filename (str): The path to the HTML file.

    Returns:
        list: A list starting with the year, followed by name-rank pairs
              in alphabetical order.
    """
    names = []

    # Open and read the file
    with open(filename, 'rt', encoding='utf-8') as f:
        text = f.read()

    # Extract the year
    year_match = re.search(r'Popularity\sin\s(\d{4})', text)
    if not year_match:
        sys.stderr.write("Couldn't find the year!\n")
        sys.exit(1)
    year = year_match.group(1)
    names.append(year)

    # Extract names and ranks
    tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', text)
    names_to_rank = {}
    for rank, boy_name, girl_name in tuples:
        if boy_name not in names_to_rank:
            names_to_rank[boy_name] = rank
        if girl_name not in names_to_rank:
            names_to_rank[girl_name] = rank

    # Sort names alphabetically and format as "name rank"
    sorted_names = sorted(names_to_rank.keys())
    for name in sorted_names:
        names.append(f"{name} {names_to_rank[name]}")

    return names

def main():
    """
    Main function to handle command-line arguments and process files.
    """
    args = sys.argv[1:]

    if not args:
        print("usage: [--summaryfile] file [file ...]")
        sys.exit(1)

    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]

    for filename in args:
        names = extract_names(filename)
        text = '\n'.join(names)

        if summary:
            with open(filename + '.summary', 'w', encoding='utf-8') as outf:
                outf.write(text + '\n')
        else:
            print(text)

if __name__ == '__main__':
    main()
