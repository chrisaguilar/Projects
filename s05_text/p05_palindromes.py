"""
Text 05: Check if Palindrome.

Checks if the string entered by the user is a palindrome.
That is that it reads the same forwards as backwards like “racecar”
"""

import re


def palindrome(string: str) -> bool:
    """Return True if the given string is a palindrome, False otherwise."""
    string = re.sub(r'\W', '', string).upper()
    return string == string[::-1]


def main():
    """Run the palindrome function against some test strings."""
    tests = [
        'Able was I ere I saw Elba', 'A man, a plan, a canal - Panama!',
        'Doc, note: I dissent. A fast never prevents a fatness. I diet on cod',
        'Madam, I\'m Adam', 'Never odd or even', 'racecar',
        'T. Eliot, top bard, notes putrid tang emanating, is sad; I\'d assign \
        it a name: gnat dirt upset on drab pot toilet.'
    ]

    for sentence in tests:
        print(palindrome(sentence))

    with open('./file.txt') as file:
        text = re.split(r'\s', file.read())
        for word in text:
            if (palindrome(word)):
                print(word)


if __name__ == '__main__':
    main()
