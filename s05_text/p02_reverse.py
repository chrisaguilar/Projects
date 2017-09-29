"""
Text 02: Reverse a String.

Enter a string and the program will reverse it and print it out.
"""


def reverse_string(string: str) -> str:
    """Reverse the given string."""
    # return ''.join(reversed(string))
    return string[::-1]


def main():
    """Test the reverse_string function."""
    with open('./file.txt') as file:
        text = file.read()
        print(reverse_string(text))


if __name__ == '__main__':
    main()
