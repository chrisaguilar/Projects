"""
Text 06: Count Words in a String.

Counts the number of individual words in a string.
For added complexity read these strings in from a text file and generate a
summary.
"""

import re
from statistics import mean


def word_count(string: str) -> None:
    """Return word count of file."""
    with open(string) as file:
        lines = file.readlines()
        chars = [len(line) for line in lines]
        words = [len(re.split(r' ', line)) for line in lines]
        print(string)
        print(f'Total Lines: {len(lines)}')
        print(f'Total Characters: {sum(chars)}')
        print(f'Average Characters: {round(mean(chars), 2)}')
        print(f'Total Words: {sum(words)}')
        print(f'Average Words: {round(mean(words), 2)}')


def main():
    word_count('file.txt')


if __name__ == '__main__':
    main()
