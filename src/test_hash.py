# -*- coding: utf-8 -*-
import pytest


FILE_PATH = '/usr/share/dict/words'


@pytest.fixture(scope='function')
def new_hash():
    from hash import Hashtable
    hashtable = Hashtable()
    return hashtable


@pytest.fixture(scope='function')
def large_hash():
    from hash import Hashtable
    hashtable = Hashtable(1024)
    return hashtable


def test_empty_hash_exists(new_hash):
    assert new_hash


def test_init(new_hash):
    assert len(new_hash.table) == 11


def test_non_default_hash_exists(large_hash):
    assert large_hash


def test_single_insert(new_hash):
    new_hash.set('test', 'value')
    assert new_hash.get('test') == 'value'


def test_same_key_insert(new_hash):
    new_hash.set('test', 'farts')
    new_hash.set('test', 'value')
    assert new_hash.get('test') == 'value'


def test_full_hashtable(large_hash):
    f = open(FILE_PATH, 'r')
    for line in f.read().splitlines():
        large_hash.set(line, line)
        assert large_hash.get(line) == line


def test_key_error(new_hash):
    """
    Verify that the correct TypeError is raised
    when any incorrect keys are entered.
    """
    cat = 2 + 6
    with pytest.raises(TypeError):
        assert new_hash.set(123, "potato")
        assert new_hash.set(cat, "dog")
        assert new_hash.get(4.56, "seven, eight, nine")
        assert new_hash.get(True, "so many")


def test_hash(new_hash):
    """Test hashing function returns correct hash for key."""
    assert new_hash._hash("key") == 3


def test_string_to_bits(new_hash):
    """Test string to bits function."""
    assert new_hash._str_to_bits("key") == 14


def test_nonexistent_keys(new_hash):
    """
    Test negative response when the
    key doesn't exist in the table
    """
    new_hash.set('test key', 'test value')
    with pytest.raises(KeyError):
        assert new_hash.get('some other key')


def test_set(new_hash):
    """
    Test set method all by itself.
    """
    new_hash.set('test', 'value')
    assert ('test', 'value') in new_hash.table[new_hash._hash('test')]
