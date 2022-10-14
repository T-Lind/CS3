from timeit import Timer
import random

def linear_search(iterable, item):
    """
    Can be in any order. O(n) solution time
    :param iterable: The iterable to search
    :param item: The item to search for
    :return: The index of the item to search for. -1 if no such item is found
    """
    for i in range(len(iterable)):
        if iterable[i] == item:
            return i
    return -1


def __perform_binary_search(iterable, item, start, end):
    if end >= start:
        mid = (end + start) // 2
        if iterable[mid] == item:
            return mid

        elif iterable[mid] > item:
            return __perform_binary_search(iterable, item, start, mid - 1)
        else:
            return __perform_binary_search(iterable, item, mid + 1, end)

    else:
        return -1


def binary_search(iterable, item):
    """
    Must be already sorted! O(log2(n)) solution
    :param iterable: The iterable to check
    :param item: The item to look for
    :return: The index of the item. -1 if no such item is found.
    """
    return __perform_binary_search(iterable, item, 0, len(iterable))


example_list = sorted([random.randint(0, 1000)]*10000)

t1 = Timer("linear_search(example_list, max(example_list))", "from __main__ import linear_search, example_list")
t2 = Timer("binary_search(example_list, max(example_list))", "from __main__ import binary_search, example_list")

print(f"Linear search after 10000 iterations: {t1.timeit(number=10000):15.2f} seconds")
print(f"Binary search after 10000 iterations: {t2.timeit(number=10000):15.2f} seconds")

