"""
Text 03: Pig Latin.

Pig Latin is a game of alterations played on the English language game.
To create the Pig Latin form of an English word the initial consonant sound is
transposed to the end of the word and an ay is affixed (Ex.: "banana" would
yield anana-bay). Read Wikipedia for more information on rules.
"""

import re


def piglatin(word: str) -> str:
    """Convert the given word to Pig Latin."""
    piggy: str = ''.join(reversed(re.split(r'^([^aeiou]{1,})', word)))
    if re.match(r'.*[!?,.].*', word):
        return re.sub(r'(\w*)([!?,.])(\w*)', r'\1\3ay\2', piggy)
    else:
        return piggy + 'ay'


def pig_sentence(string: str) -> str:
    """Convert given sentence to Pig Latin."""
    return ' '.join([piglatin(word)
                     for word in string.split(' ')]).capitalize()


def main() -> None:
    """Test the Pig Latin function."""
    with open('./file.txt') as file:
        text = file.readlines()
        for line in text:
            print(pig_sentence(line.strip()))


if __name__ == '__main__':
    main()
