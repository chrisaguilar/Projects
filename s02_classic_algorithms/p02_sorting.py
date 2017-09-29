"""
Classic Algorithm 02: Sorting.

Implement two type of sorting algorithms: Merge sort and bubble sort.
"""

from numpy.random import random_integers


def merge(left, right):
    """Merge the left list with the right list."""
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    while left:
        result.append(left[0])
        left = left[1:]
    while right:
        result.append(right[0])
        right = right[1:]
    return result


def merge_sort(lst):
    """Sort lst with the merge sort algorithm."""
    if len(lst) <= 1:
        return lst

    split: int = len(lst) // 2
    left = merge_sort(lst[0:split])
    right = merge_sort(lst[split:])

    return merge(left, right)


def bubble_sort(lst):
    """Sort lst with the bubble sort algorithm."""
    old_n = len(lst)
    while old_n != 0:
        new_n = 0
        for i in range(1, old_n):
            if lst[i - 1] > lst[i]:
                lst[i - 1], lst[i] = lst[i], lst[i - 1]
                new_n = i
        old_n = new_n
    return lst


print(merge_sort(random_integers(100, size=10)))
print(bubble_sort(random_integers(100, size=10)))
print(bubble_sort([x for x in range(1000, 0, -1)]))
