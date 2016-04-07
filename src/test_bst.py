import pytest


# @pytest.mark.parametrize('')

@pytest.fixture(scope='function')
def empty_tree():
    from bst import BinarySearchTree
    empty = BinarySearchTree()
    return empty


@pytest.fixture(scope='function')
def test_tree():
    from bst import BinarySearchTree
    test = BinarySearchTree([5])
    return test


def test_make_empty_tree(empty_tree):
    assert empty_tree


def test_empty_tree_value(empty_tree):
    assert not empty_tree.root


def test_make_one_node_tree(test_tree):
    assert test_tree.root.val == 5


def test_enter_first_node(empty_tree):
    empty_tree.insert(6)
    assert empty_tree.root.val == 6


def test_first_node_children(test_tree):
    # result = test_tree.root._left
    # assert result is None
    assert test_tree.root.left is None
    assert test_tree.root.right is None


def test_empty_tree_size(empty_tree):
    assert empty_tree.size() == 0


def test_first_entry_size(empty_tree):
    empty_tree.insert(8)
    assert empty_tree.size() == 1


def test_insert_first_child(test_tree):
    # import pdb; pdb.set_trace()
    test_tree.insert(10)
    assert test_tree.root.right.val == 10
