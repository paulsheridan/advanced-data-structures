# -*- coding: utf-8 -*-
import random


def insertionsort(in_list):
    for idx in range(1, len(in_list)):
        while idx > 0 and in_list[idx] < in_list[idx - 1]:
            in_list[idx], in_list[idx - 1] = in_list[idx - 1], in_list[idx]
            idx -= 1
    return in_list


def mergesort(in_list):
    if len(in_list) > 1:
        mid = len(in_list)//2
        left = mergesort(in_list[:mid])
        right = mergesort(in_list[mid:])
        return(merge(left, right))
    else:
        return in_list


def merge(left, right):
    new = []
    while left and right:
        if left[0] < right[0]:
            new.append(left.pop(0))
        elif right[0] < left[0]:
            new.append(right.pop(0))
        else:
            new.append(left.pop(0))
            new.append(right.pop(0))
    if left:
        new.extend(left)
    elif right:
        new.extend(right)
    return new

print(mergesort([99, 4, 6, 2, 7, 1, 4, 2, 13]))


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


# if __name__ == '__main__':
#     import timeit
#     LIST_ONE = [1, 2, 3, 4]
#     LIST_TWO = [random.randint(0, 1000000) for i in range(10000)]
#     print("Insertion sort")
#     print("Compares each item in the list to its neighbor.")
#     print("It's stable and most efficient on small lists.")
#     print("Input: [1, 2]")
#     wrapped = wrapper(insertionsort, LIST_ONE)
#     print('Runs: 500')
#     print('Average time: ', timeit.timeit(wrapped, number=500))
#     print("Input: [random.randint(0, 1000000) for i in range(10000)]")
#     print('Runs: 500')
#     wrapped = wrapper(insertionsort, LIST_TWO)
#     print('Average time: ', timeit.timeit(wrapped, number=500))
