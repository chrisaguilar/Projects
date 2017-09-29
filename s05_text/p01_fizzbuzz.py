"""
Text 01: Fizz Buzz.

Write a program that prints the numbers from 1 to 100.
But for multiples of three print “Fizz” instead of the number and for the
multiples of five print “Buzz”. For numbers which are multiples of both three
and five print “FizzBuzz”.
"""

from typing import List, Union


def to_fizzbuzz(num: int) -> Union[int, str]:
    """Decide whether num is a Fizz, Buzz, FizzBuzz, or none."""
    if not isinstance(num, int):
        return 'Invalid!'
    elif not num % 3 and not num % 5:
        return 'FizzBuzz'
    elif not num % 3:
        return 'Fizz'
    elif not num % 5:
        return 'Buzz'
    else:
        return num


def fizzbuzz(start: int, end: int) -> List[Union[int, str]]:
    """Solve the FizzBuzz problem between start and end."""
    return [to_fizzbuzz(i) for i in range(start, end + 1)]


print(fizzbuzz(1, 100))
