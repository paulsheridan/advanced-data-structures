import pytest
import random


EDGE_CASES = [[[100, 100, 100, 100, 100], [100, 100, 100, 100, 100]],
              [[999999999999999, 0], [0, 999999999999999]],
              [[1000000000, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1000000000]],
              [[], []],
              [[1, 100, 1, 100, 1, 100, 1, 100, 1, 100],
               [1, 1, 1, 1, 1, 100, 100, 100, 100, 100]],
              [[1, 4, -2, -6, 3, 5], [-6, -2, 1, 3, 4, 5]],
              [['c', 'b', 'q', 'a', 'f', 'd'], ['a', 'b', 'c', 'd', 'f', 'q']]]


RADIX_CASES = [[[100, 100, 100, 100, 100], [100, 100, 100, 100, 100]],
               [[999999999999999, 0], [0, 999999999999999]],
               [[1000000000, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1000000000]],
               [[], []],
               [[1, 100, 1, 100, 1, 100, 1, 100, 1, 100],
               [1, 1, 1, 1, 1, 100, 100, 100, 100, 100]],
               [[1, 4, -2, -6, 3, 5], [1, 3, 4, -6, 5, -2]],
               ]


@pytest.fixture(scope='function')
def unsorted():
    unsorted_list = [random.randint(0, 1000000) for i in range(1000)]
    return unsorted_list


@pytest.fixture(scope='function')
def empty():
    empty_list = []
    return empty_list


def test_insertion_sort(unsorted):
    from sort import insertionsort
    sort_list = insertionsort(unsorted)
    for ii in range(1, len(unsorted) - 1):
        assert sort_list[ii] >= sort_list[ii - 1]


def test_insertion_empty(empty):
    from sort import insertionsort
    assert insertionsort(empty) == []


@pytest.mark.parametrize('unsorted, sorted', EDGE_CASES)
def test_insertion_edge_cases(unsorted, sorted):
    from sort import insertionsort
    assert insertionsort(unsorted) == sorted


def test_merge_sort(unsorted):
    from sort import mergesort
    sort_list = mergesort(unsorted)
    for ii in range(1, len(unsorted) - 1):
        assert sort_list[ii] >= sort_list[ii - 1]


def test_merge_empty(empty):
    from sort import mergesort
    assert mergesort(empty) == []


@pytest.mark.parametrize('unsorted, sorted', EDGE_CASES)
def test_merge_edge_cases(unsorted, sorted):
    from sort import mergesort
    assert mergesort(unsorted) == sorted


def test_quick_sort(unsorted):
    from sort import quicksort
    sort_list = quicksort(unsorted)
    for ii in range(1, len(unsorted) - 1):
        assert sort_list[ii] >= sort_list[ii - 1]


def test_quick_empty(empty):
    from sort import quicksort
    assert quicksort(empty) == []


@pytest.mark.parametrize('unsorted, sorted', EDGE_CASES)
def test_quick_edge_cases(unsorted, sorted):
    from sort import quicksort
    assert quicksort(unsorted) == sorted


def test_radix_sort(unsorted):
    from sort import radixsort
    sort_list = radixsort(unsorted)
    for ii in range(1, len(unsorted) - 1):
        assert sort_list[ii] >= sort_list[ii - 1]


def test_radixradix_empty(empty):
    from sort import radixsort
    assert radixsort(empty) == []


@pytest.mark.parametrize('unsorted, sorted', RADIX_CASES)
def test_radix_edge_cases(unsorted, sorted):
    from sort import radixsort
    assert radixsort(unsorted) == sorted
