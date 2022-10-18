from timeit import Timer
import random
import matplotlib.pyplot as plt


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


def non_recursive_binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1

        # means x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1


example_list = None

t1 = Timer("linear_search(example_list, max(example_list))", "from __main__ import linear_search, example_list")
t2 = Timer("non_recursive_binary_search(example_list, max(example_list))",
           "from __main__ import non_recursive_binary_search, example_list")

# print(f"Linear search after 10000 iterations: {t1.timeit(number=10000):15.2f} seconds")
# print(f"Binary search after 10000 iterations: {t2.timeit(number=10000):15.2f} seconds")
time = []
linear_search_data = []
binary_search_data = []
for i in range(20000):
    example_list = sorted([random.randint(0, 10000)] * i)

    try:
        linear_search_data.append(t1.timeit(number=100))
        binary_search_data.append(t2.timeit(number=100))
        time.append(i)
    except Exception as e:
        pass

plt.plot(time, linear_search_data, color="red", label="Linear Search", alpha=0.5)
plt.plot(time, binary_search_data, color="blue", label="Binary Search", alpha=0.5)
plt.title("Linear vs. Binary Search Timing")
plt.xlabel("Size of list to search")
plt.ylabel("Time to search (s)")
plt.legend()
plt.show()
