import pytest
import random


@pytest.fixture(scope='session')
def unsorted():
    unsorted_list = [random.randint(0, 1000000) for i in range(1000)]
    return unsorted_list


def test_insertion_sort(unsorted):
    from sort import insertionsort
    sort_list = insertionsort(unsorted)
    for ii in range(1, len(unsorted) - 1):
        assert sort_list[ii] >= sort_list[ii - 1]


def test_insertion_stable(unsorted):
    pass
