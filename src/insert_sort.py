import random


def insertionsort(in_list):
    """Implement insertion sort."""
    for idx in range(1, len(in_list)):
        while idx > 0 and in_list[idx] < in_list[idx - 1]:
            in_list[idx], in_list[idx - 1] = in_list[idx - 1], in_list[idx]
            idx -= 1
    return in_list


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


if __name__ == '__main__':
    import timeit
    LIST_ONE = [2, 1, 4, 3]
    LIST_TWO = [random.randint(0, 1000000) for i in range(10000)]
    print("Insertion sort")
    print("Compares each item in the list to its neighbor.")
    print("It's stable and most efficient on small lists.")
    print("Input: [2, 1, 4, 3], Runs: 500")
    wrapped = wrapper(insertionsort, LIST_ONE)
    print('Total time: ', timeit.timeit(wrapped, number=500))
    print("Input: [random.randint(0, 1000000) for i in range(10000)], Runs: 500")
    wrapped = wrapper(insertionsort, LIST_TWO)
    print('Total time: ', timeit.timeit(wrapped, number=500))
