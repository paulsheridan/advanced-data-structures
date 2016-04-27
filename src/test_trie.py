# -*- coding: utf-8 -*-
import pytest
IPSUM = '''Lorem ipsum dolor sit amet consectetur adipisicing elit sed do
           eiusmod tempor incididunt ut labore et dolore magna aliqua Ut enim
           ad minim veniam quis nostrud exercitation ullamco laboris nisi ut
           aliquip ex ea commodo consequat Duis aute irure dolor in
           reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
           pariatur Excepteur sint occaecat cupidatat non proident sunt in
           culpa qui officia deserunt mollit anim id est laborum'''
INSERT_CASES = [['', {}],
                ['w', {'w': {'$': {}}}],
                ['to', {'t': {'o': {'$': {}}}}],
                ['ha ha', {'h': {'a': {'$': {}}}}],
                ['it he', {'h': {'e': {'$': {}}}, 'i': {'t': {'$': {}}}}],
                ['broke broken',
                 {'b': {'r': {'o': {'k': {'e': {'$': {}, 'n': {'$': {}}}}}}}}],
                ['a as asd asdf asdfg asdfgh asdfghj',
                 {'a': {'$': {},
                        's': {'$': {},
                              'd': {'$': {},
                                    'f': {'$': {},
                                          'g': {'$': {},
                                                'h': {'$': {},
                                                      'j': {'$': {}}}}}}}}}],
                ["that's",
                 {'t': {'h': {'a': {'t': {"'": {'s': {'$': {}}}}}}}}],
                ["don't do done",
                 {'d': {'o': {'$': {}, 'n': {"'": {'t': {'$': {}}},
                  'e': {'$': {}}}}}}],
                ['same same same same same same same same same same same same',
                 {'s': {'a': {'m': {'e': {'$': {}}}}}}],
                ['right right right right right rigged right right right',
                 {'r': {'i': {'g': {'g': {'e': {'d': {'$': {}}}},
                  'h': {'t': {'$': {}}}}}}}],
                ['ba ab ba ab ba ab ba ab ba ab ba ab ba ab ba ab ba ab',
                 {'a': {'b': {'$': {}}}, 'b': {'a': {'$': {}}}}],
                ]


CONTAINS_CASES = [['w', 'w', True],
                  ['w', 'W', True],
                  ['to', 'to', True],
                  ['ha', 'he', False],
                  ['he', 'eh', False],
                  ['broke', 'broke', True],
                  ['asdfghj', 'regular', False],
                  ["that's", 'thats', False],
                  ["don't", "don't", True],
                  ['wrong', 'wright', False],
                  ['Bork', 'Bork', True],
                  ['W w', 'w', True],
                  ['holy shit', 'holy', True],
                  ['one two three', 'four', False],
                  ['smashing', 'SMASHING', True],
                  ['wood-elf', 'wood-elf', True],
                  ['', 'w', False],
                  ['', '', False]
                  ]


@pytest.fixture(scope='function')
def new_trie():
    from trie import Trie
    new_trie = Trie()
    return new_trie


@pytest.fixture(scope='function')
def full_trie():
    from trie import Trie
    full_trie = Trie()
    full_trie.insert(IPSUM)
    return full_trie


@pytest.fixture(scope='function')
def test_list():
    lorem_list = IPSUM.split()
    return lorem_list


def test_creation(new_trie):
    """Test new trie."""
    assert new_trie.root == {}


@pytest.mark.parametrize('case_in, case_out', INSERT_CASES)
def test_insert_edge_cases(new_trie, case_in, case_out):
    """
    Test various insert cases including
    empty string, single letter,
    repeat words etc.
    """
    new_trie.insert(case_in)
    assert new_trie.root == case_out


@pytest.mark.parametrize('case_one, case_two, bool', CONTAINS_CASES)
def test_contains(new_trie, case_one, case_two, bool):
    """Test contains after inserting."""
    new_trie.insert(case_one)
    assert new_trie.contains(case_two) == bool


def test_contains_with_multiple(new_trie):
    """Test contains in trie with mutliple branches."""
    new_trie.insert("multiple words")
    assert new_trie.contains("words") is True
    assert new_trie.contains("multiple") is True
    assert new_trie.contains("multiplewords") is False


def test_full_trie_contains(full_trie, test_list):
    """Test contains on a trie with one ipsum's worth of words"""
    for item in test_list:
        assert full_trie.contains(item)
