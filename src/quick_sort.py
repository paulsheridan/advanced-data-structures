import random


def quicksort(in_list):
    """Implement quick sort."""
    if len(in_list) <= 1:
        return in_list
    else:
        lower = []
        higher = []
        pivot_value = random.choice(in_list)
        for item in in_list:
            if item < pivot_value:
                lower.append(item)
            if item > pivot_value:
                higher.append(item)
        lower = quicksort(lower)
        higher = quicksort(higher)
        return lower + [pivot_value] * in_list.count(pivot_value) + higher


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


if __name__ == '__main__':
    import timeit
    LIST_ONE = [2, 1, 4, 3]
    LIST_TWO = [random.randint(0, 1000000) for i in range(10000)]
    print("Quick Sort")
    print("Quicksort divides into two smaller arrays on a pivot point\
and sorts on the two smaller arrays.")
    print("It's not a stable sort, and most efficient on small lists.")
    print("Input: [2, 1, 4, 3], Runs: 500")
    wrapped = wrapper(quicksort, LIST_ONE)
    print('Total time: ', timeit.timeit(wrapped, number=500))
    print("Input: [random.randint(0, 1000000) for i in range(10000)], Runs: 500")
    wrapped = wrapper(quicksort, LIST_TWO)
    print('Total time: ', timeit.timeit(wrapped, number=500))
