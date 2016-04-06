import pytest


# @pytest.mark.parametrize('')

def test_make_empty_tree():
    from bst import BinarySearchTree
    test_tree = BinarySearchTree()
    assert test_tree


def test_empty_tree_value():
    from bst import BinarySearchTree
    test_tree = BinarySearchTree()
    assert not test_tree.root


def test_make_one_node_tree():
    from bst import BinarySearchTree
    test_tree = BinarySearchTree([5])
    assert test_tree.root.val == 5


def test_enter_first_node():
    from bst import BinarySearchTree
    test_tree = BinarySearchTree()
    test_tree.insert(6)
    assert test_tree.root.val == 6


def test_first_node_children():
    from bst import BinarySearchTree
    test_tree = BinarySearchTree([7])
    assert test_tree.root.left is None
    assert test_tree.root.right is None


def test_empty_tree_size():
    from bst import BinarySearchTree
    test_tree = BinarySearchTree()
    assert test_tree.size == 0


def test_first_entry_size():
    from bst import BinarySearchTree
    test_tree = BinarySearchTree()
    test_tree.insert(8)
    assert test_tree.size == 1
