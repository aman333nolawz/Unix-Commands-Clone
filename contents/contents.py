#!/usr/bin/env python3
import argparse
from string import ascii_letters, digits, punctuation

parser = argparse.ArgumentParser(description="Display printable strings in file.")
parser.add_argument(
    "filename", type=str, help="Filename of the file you want to get the contents."
)
parser.add_argument(
    "-n",
    metavar="min_len",
    type=int,
    default=4,
    help="Locate & print any NUL-terminated sequence of at least <N> amount of characters (default 4).",
)
args = parser.parse_args()

allowed = digits + ascii_letters + punctuation + " \t"


def strings(filename, min_len=4):
    with open(filename, errors="ignore") as file:
        content = file.read()

    result = ""

    for c in content:
        if c in allowed:
            result += c
            continue

        if len(result) >= min_len:
            yield result.strip()

        result = ""

    if len(result) >= min_len:
        if result.strip() != "":
            yield result
        else:
            yield ""


result = list(strings(args.filename, args.n))
result = "\n".join(result)
print(result)
