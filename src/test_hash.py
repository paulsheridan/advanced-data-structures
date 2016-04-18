# -*- coding: utf-8 -*-
import pytest
import os


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


def test_non_default_hash_exists(large_hash):
    assert large_hash


def test_full_hashtable():
    from hash import Hashtable
    hashtable = Hashtable(997)
    with open(FILE_PATH, 'r', buffering=1) as f:
        for line in f:
            hashtable.set(line, line)
            assert hashtable.get(line) == line


def test_key_error(new_hash):
