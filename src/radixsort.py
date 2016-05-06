import random


def radixsort(in_list):
    """Implement Radix Sort."""
    if not in_list:
        return []
    radix = 10
    for iteration in range(len(str(max(in_list)))):
        buckets = [[] for x in range(10)]
        for item in in_list:
            buckets[(item % radix) // (radix // 10)].append(item)
        radix *= 10
        in_list = [item for li in buckets for item in li]
    return in_list


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


if __name__ == '__main__':
    import timeit
    LIST_ONE = [2, 1, 4, 3]
    LIST_TWO = [random.randint(0, 1000000) for i in range(10000)]
    print("Radix Sort")
    print("Radix sort is a non-comparative integer sorting algorithm that sorts\
data with integer keys by grouping keys by the individual digits which share\
 the same significant position and value.")
    print("It's a stable sort, and most efficient depending on radix assumptions\
 made.")
    print("Input: [2, 1, 4, 3], Runs: 500")
    wrapped = wrapper(radixsort, LIST_ONE)
    print('Total time: ', timeit.timeit(wrapped, number=500))
    print("Input: [random.randint(0, 1000000) for i in range(10000)], Runs: 500")
    wrapped = wrapper(radixsort, LIST_TWO)
    print('Total time: ', timeit.timeit(wrapped, number=500))
