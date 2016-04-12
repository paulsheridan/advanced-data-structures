import pytest
import math
import random

TOTAL = list(range(100))
HALF = list(range(50))
EVEN = TOTAL[2::2]
ODD = TOTAL[1::2]
LESSER = TOTAL[:52]
GREATER = TOTAL[50:]
TEST_LIST = [9, 3, 22, 7, 1, 55]

TEST_TREE_LIST = [50, 30, 70, 20, 40,
                  60, 80, 75, 100,
                  76, 71, 73, 72, 74]


@pytest.fixture(scope='function')
def test_tree():
    from bst import Tree
    tree = Tree(5)
    return tree


@pytest.fixture(scope='function')
def empty_tree():
    from bst import Tree
    tree = Tree()
    return tree


@pytest.fixture(scope='function')
def test_trav_tree():
    from bst import Tree
    tree = Tree(5)
    for item in TEST_LIST:
        tree.insert(item)
    return tree


def insert_balanced(num):
    num_of_runs = num
    from bst import Tree
    tree = Tree(50)
    while num_of_runs > 0:
        left_num = LESSER[num_of_runs]
        right_num = GREATER[num_of_runs]
        tree.insert(left_num)
        tree.insert(right_num)
        num_of_runs -= 1
    return tree


def insert_unbalanced_left(num):
    num_of_runs = num
    from bst import Tree
    tree = Tree(50)
    while num_of_runs > 0:
        left_num = LESSER[num_of_runs]
        tree.insert(left_num)
        if num_of_runs % 2 == 0:
            right_num = GREATER[num_of_runs]
            tree.insert(right_num)
        num_of_runs -= 1
    return tree


def insert_unbalanced_right(num):
    num_of_runs = num
    from bst import Tree
    tree = Tree(50)
    while num_of_runs > 0:
        right_num = GREATER[num_of_runs]
        tree.insert(right_num)
        if num_of_runs % 2 == 0:
            left_num = LESSER[num_of_runs]
            tree.insert(left_num)
        num_of_runs -= 1
    return tree


@pytest.mark.parametrize('num', TOTAL)
def test_contains_true(num, empty_tree):
    empty_tree.insert(num)
    assert empty_tree.contains(num)


@pytest.mark.parametrize('odd', ODD)
@pytest.mark.parametrize('even', EVEN)
def test_contains_false(even, odd):
    from bst import Tree
    tree = Tree(216)
    tree.insert(even)
    assert not tree.contains(odd)


def test_tree_value(empty_tree):
    assert empty_tree


def test_empty_tree_value(test_tree):
    assert test_tree


def test_make_one_node_tree(test_tree):
    assert test_tree.contains(5) is True


def test_enter_second_node(test_tree):
    test_tree.insert(6)
    assert test_tree.right.data == 6


def test_null_left(test_tree):
    assert test_tree.left is None


def test_null_right(test_tree):
    assert test_tree.right is None


def test_test_tree_size(test_tree):
    assert test_tree.size() == 1


def test_first_entry_size(test_tree):
    test_tree.insert(8)
    assert test_tree.size() == 2


def test_insert_first_child(test_tree):
    test_tree.insert(10)
    assert test_tree.right.data == 10


@pytest.mark.parametrize('num', HALF)
def test_even_balance(num):
    if num > 2:
        balanced_tree = insert_balanced(num)
        assert balanced_tree.balance() == 0


@pytest.mark.parametrize('num', HALF)
def test_uneven_left(num):
    if num > 2 and num % 2 == 0:
        left_tree = insert_unbalanced_left(num)
        assert left_tree.balance() == math.ceil(num/2)


@pytest.mark.parametrize('num', HALF)
def test_uneven_right(num):
    if num > 2 and num % 2 == 0:
        right_tree = insert_unbalanced_right(num)
        assert right_tree.balance() == (math.ceil(num/2)) * -1


def test_in_order(test_trav_tree):
    return_val = [x for x in test_trav_tree.in_order()]
    assert return_val == [1, 3, 5, 7, 9, 22, 55]


def test_pre_order(test_trav_tree):
    return_val = [x for x in test_trav_tree.pre_order()]
    assert return_val == [5, 3, 1, 9, 7, 22, 55]


def test_post_order(test_trav_tree):
    return_val = [x for x in test_trav_tree.post_order()]
    assert return_val == [1, 3, 7, 55, 22, 9, 5]


@pytest.mark.parametrize('num', TOTAL)
def test_traversal_in_singe(num, test_tree):
    from bst import Tree
    tree = Tree(num)
    result = [x for x in tree.in_order()]
    assert result == [num]


@pytest.mark.parametrize('num', TOTAL)
def test_traversal_pre_single(num, test_tree):
    from bst import Tree
    tree = Tree(num)
    result = [x for x in tree.pre_order()]
    assert result == [num]


@pytest.mark.parametrize('num', TOTAL)
def test_traversal_post_single(num, test_tree):
    from bst import Tree
    tree = Tree(num)
    result = [x for x in tree.post_order()]
    assert result == [num]


@pytest.mark.parametrize('num', TOTAL)
def test_add_delete_one(num, empty_tree):
    empty_tree.insert(num)
    empty_tree.delete(num)
    assert not empty_tree.data


@pytest.mark.parametrize('num', TOTAL)
def test_add_delete_second(num, test_tree):
    test_tree.insert(num)
    test_tree.delete(num)
    assert not test_tree.left and not test_tree.right


@pytest.mark.parametrize('num', TEST_TREE_LIST)
def test_delete_from_tree(num, empty_tree):
    [empty_tree.insert(item) for item in TEST_TREE_LIST]
    empty_tree.delete(num)
    assert not empty_tree.contains(num)


@pytest.mark.parametrize('num', TEST_TREE_LIST)
def test_not_deleted_from_tree(num, empty_tree):
    [empty_tree.insert(item) for item in TEST_TREE_LIST]
    empty_tree.delete(num)
    for item_two in TEST_TREE_LIST:
        if item_two != num:
            assert empty_tree.contains(item_two)
