import pytest


TOTAL = list(range(100))
EVEN = TOTAL[2::2]
ODD = TOTAL[1::2]


@pytest.mark.parametrize('even', EVEN)
def test_contains_true(even):
    from bst import Tree
    tree = Tree(4)
    tree.insert(even)
    assert tree.contains(even)


@pytest.mark.parametrize('odd', ODD)
@pytest.mark.parametrize('even', EVEN)
def test_contains_false(even, odd):
    from bst import Tree
    tree = Tree(216)
    tree.insert(even)
    assert not tree.contains(odd)


@pytest.fixture(scope='function')
def test_tree():
    from bst import Tree
    tree = Tree(5)
    return tree


def test_null_tree_error():
    from bst import Tree
    with pytest.raises(TypeError):
        Tree()


def test_test_tree_value(test_tree):
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
