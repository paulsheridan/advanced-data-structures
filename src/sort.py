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
        left = in_list[:mid]
        right = in_list[mid:]
        mergesort(left)
        mergesort(right)
        return(merge(left, right))


def merge(left, right):
    new = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            new.append(left.pop(0))
        elif right[0] < left[0]:
            new.append(right.pop(0))
        else:
            new.extend(right.pop(0), left.pop(0))
    if len(left) > 0:
        new.extend(left)
    elif len(right) > 0:
        new.extend(right)
    return new


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


if __name__ == '__main__':
    import timeit
    LIST_ONE = [1, 2, 3, 4]
    LIST_TWO = [random.randint(0, 1000000) for i in range(10000)]
    print("Insertion sort")
    print("Compares each item in the list to its neighbor.")
    print("It's stable and most efficient on small lists.")
    print("Input: [1, 2]")
    wrapped = wrapper(insertionsort, LIST_ONE)
    print('Runs: 500')
    print('Average time: ', timeit.timeit(wrapped, number=500))
    print("Input: [random.randint(0, 1000000) for i in range(10000)]")
    print('Runs: 500')
    wrapped = wrapper(insertionsort, LIST_TWO)
    print('Average time: ', timeit.timeit(wrapped, number=500))
