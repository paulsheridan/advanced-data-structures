import pytest


@pytest.fixture(scope='function')
def new_trie():
    from trie import Trie
    new_trie = Trie()
    return new_trie


def test_creation(new_trie):
    """Test new trie."""
    assert new_trie.root == {}


def test_insert_letter(new_trie):
    """Test inser letter."""
    new_trie.insert('w')
    assert new_trie.root == {'w': {}}


def test_insert_word(new_trie):
    """Test word insert."""
    new_trie.insert('to')
    assert new_trie.root == {'t': {'o': {}}}


def test_insert_same(new_trie):
    """Test insert same token."""
    new_trie.insert('ha ha')
    assert new_trie.root == {'h': {'a': {}}}


def test_insert_space(new_trie):
    """Test insert same token."""
    new_trie.insert('it he')
    assert new_trie.root == {'h': {'e': {}}, 'i': {'t': {}}}
