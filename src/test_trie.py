import pytest

INSERT_CASES = [['', {}],
              ['w', {'w': {'$': {}}}],
              ['to', {'t': {'o': {'$': {}}}}],
              ['ha ha', {'h': {'a': {'$': {}}}}],
              ['it he', {'h': {'e': {'$': {}}}, 'i': {'t': {'$': {}}}}],
              ['broke broken', {'b': {'r': {'o': {'k': {'e': {'$': {}, 'n': {'$': {}}}}}}}}],
              ['a as asd asdf asdfg asdfgh asdfghj',
               {'a': {'$': {},
                      's': {'$': {},
                            'd': {'$': {},
                                  'f': {'$': {},
                                        'g': {'$': {},
                                              'h': {'$': {},
                                                    'j': {'$': {}}}}}}}}}],
              ["that's", {'t': {'h': {'a': {'t': {"'": {'s': {'$': {}}}}}}}}],
              ["don't do done", {'d': {'o': {'$': {}, 'n': {"'": {'t': {'$': {}}}, 'e': {'$': {}}}}}}],
              ['same same same same same same same same same same same same', {'s': {'a': {'m': {'e': {'$': {}}}}}}],
              ['right right right right right rigged right right right', {'r': {'i': {'g': {'g': {'e': {'d': {'$': {}}}}, 'h': {'t': {'$': {}}}}}}}],
              ['ba ab ba ab ba ab ba ab ba ab ba ab ba ab ba ab ba ab', {'a': {'b': {'$': {}}}, 'b': {'a': {'$': {}}}}],
              ]


@pytest.fixture(scope='function')
def new_trie():
    from trie import Trie
    new_trie = Trie()
    return new_trie


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
