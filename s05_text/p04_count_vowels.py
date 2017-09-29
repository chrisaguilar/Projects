"""
Text 04: Count Vowels.

Enter a string and the program counts the number of vowels in the text.
For added complexity have it report a sum of each vowel found.
"""

import re


def count_vowels(string: str) -> int:
    """Count the vowels in a string using a regular expression."""
    return len(re.findall(f'[aeiou]', string, re.IGNORECASE))


def main() -> None:
    """Run the count_vowels function against some test strings."""
    with open('./file.txt') as file:
        text = file.read()
        print(count_vowels(text))


if __name__ == '__main__':
    main()
