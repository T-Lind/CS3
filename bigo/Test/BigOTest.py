import random
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr


def sum_time(sort_function, n_sum=50, array_length=1000, sort=None):
    """
    Sum the time it takes to sort a list given an input function and set of parameters
    :param sort_function: the function to apply
    :param n_sum: the number of runs to sum
    :param array_length: the array length of the test case it generates
    :param sort: whether or not to pre-sort the data and if so in what order
    :return: a string describing the run
    """
    summed_time = 0

    for _ in range(n_sum):
        test_case = [random.randrange(0, array_length * 10) for _ in range(array_length)]

        if sort == "forward":
            test_case = sorted(test_case)
        elif sort == "reverse":
            test_case = sorted(test_case, reverse=True)

        before_time = time.time()
        sort_function(test_case)
        after_time = time.time()
        summed_time += (after_time - before_time)

    ret_str = f"{sort_function.__name__} ran {n_sum} times in {summed_time:.4f} seconds. "

    if sort == "forward":
        return ret_str + "The list was sorted."
    elif sort == "reverse":
        return ret_str + "The list was sorted in reverse order."
    return ret_str


# Expected BigO: O(n^2) for both algorithms for the average case!


# Selection Sort Test Cases:
print("Selection Sort Results:\n--------------------")

print(sum_time(selection_sort, sort="forward"))
print(sum_time(selection_sort))
print(sum_time(selection_sort, sort="reverse"))

# Insertion Sort Test Cases:
print("Insertion Sort Results:\n--------------------")

print(sum_time(insertion_sort, sort="forward"))
print(sum_time(insertion_sort))
print(sum_time(insertion_sort, sort="reverse"))

# Conclusion:

# selection_sort will sort a list in
# approximately the same time regardless
# of whether the list is sorted in forward,
# reverse, or not at all. This is due to the
# double for loops that always add the squared
# amount of time to run.

# selection_sort Big O table:
# best: O(n^2)
# rng: O(n^2)
# worst: O(n^2)

# insertion_sort will sort a list faster
# when it has already been sorted, and
# slower when it is in reverse sorted order.
# This is due to the while loop present, so the
# while loop won't execute at all if sorted causing
# it only to execute in a very small amount of time
# but conversely will execute significantly more if
# in reverse order

# insertion_sort Big O table:
# best: O(1)
# rng: O(n^2)
# worst: O(n^3)
