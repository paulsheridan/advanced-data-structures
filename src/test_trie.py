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
NUM_SYMBOL = 963
BOOL_SYMBOL = False
LIST_SYMBOL = ['string']
DICT_SYMBOL = {'this': 'dict'}
NOT_STR = [123, 12345666, 0, True, False,
           NUM_SYMBOL, BOOL_SYMBOL, LIST_SYMBOL,
           DICT_SYMBOL, [4, 5, 6, 'string'], {}]
HAS_DOLLAR_SIGN = ['venia$m', '$quis', 'nos$trud',
                   'exercitation$', '$ullamco$',
                   'l$aboris', '$$$$$$$$']
TRAV_CASES = ['a',
              'paul',
              'carnivale',
              'spinmove'
              'this is the first one',
              'this is one of the second ones',
              'no wait that was the only second one',
              "well now we've skipped the third one",
              'wait where did four go?',
              'you know what',
              'forget it',
              "I'm going to the pub"]
AUTOCOMPLETE_CASES = [['bears beets battlestar galactica', 'b',
                       ['battlestar', 'bears', 'beets']],
                      ['bears beets battlestar galactica', 'ba',
                       ['battlestar']],
                      ['bears beets battlestar galactica', 'be',
                       ['bears', 'beets']],
                      ['bears beets battlestar galactica', 'bea',
                       ['bears']],
                      ['bears beets battlestar galactica', 'g',
                       ['galactica']],
                      ['bears beets battlestar galactica', '',
                       ['bears', 'beets', 'battlestar', 'galactica']],
                      ['', '', []],
                      ['store stick stanza street stop', 's',
                       ['store', 'stick', 'stanza', 'street', 'stop']],
                      ['word word word words', 'w',
                       ['word', 'words']],
                      [IPSUM, 'c', ['cillum',
                                    'commodo',
                                    'consectetur',
                                    'consequat',
                                    'culpa',
                                    'cupidatat']],
                      ['c c c c c c c c c c c c c c c c', 'c', ['c']],
                      ['cat cats caterpillar caterpillars', 'cat',
                       ['cat', 'caterpillar', 'caterpillars', 'cats']],
                      ['cat cats caterpillar caterpillars', 'cats',
                       ['cats']],
                      ['cat cats caterpillar caterpillars', 'catse',
                       []],
                      ['cat cats caterpillar caterpillars', 'bats',
                       []],
                      ['cat cats caterpillar caterpillars', 'caterl',
                       []],
                      ['''i have been completely unable to maintain
                       any semblance of relationship on any level''', 'omp',
                       []],
                      ['''i have been a bastard to the people who have
                       actively attempted to deliver me from peril''', 'a',
                       ['a', 'actively', 'attempted']],
                      ['''i have been acutely undeserving of the ear that
                       listen up and lip that kiss me on the temple''', 'li',
                       ['listen', 'lip']],
                      ['''i have been accustomed to a
                       stubborn disposition that admits
                       its history disassembled''', 'dis',
                       ['disposition', 'disassembled']],
                      ['''i have been a hypocrit in sermonizing tolerance
                       while skimming for a ministry to pretzel''', 'skiming',
                       []],
                      ['''i have been unfairly resentful of
                       those who i wish had acted differently
                       when the bidding was essential''', 'i',
                       ['i']],
                      ['''i have been a terrible communicator prone to
                       isolation over sympathy for devils''', 'terr',
                       ['terrible']],
                      ['''i have been my own worst enemy since the
                       very genesis of rebels''', 'verif',
                       []]]


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


@pytest.mark.parametrize('case', NOT_STR)
def test_validator_not_str(new_trie, case):
    with pytest.raises(TypeError):
        new_trie._validate(case)


@pytest.mark.parametrize('case', HAS_DOLLAR_SIGN)
def test_validator_dollar_sign(new_trie, case):
    with pytest.raises(ValueError):
        new_trie._validate(case)


@pytest.mark.parametrize('case', NOT_STR)
def test_non_str_insert(new_trie, case):
    with pytest.raises(TypeError):
        new_trie.insert(case)


@pytest.mark.parametrize('case', HAS_DOLLAR_SIGN)
def test_insert_dollar_sign(new_trie, case):
    with pytest.raises(ValueError):
        new_trie.insert(case)


@pytest.mark.parametrize('case', TRAV_CASES)
def test_basic_traverse(new_trie, case):
    new_trie.insert(case)
    assert any(map(lambda v: v in new_trie.traverse(), case.split()))


def test_redundant_input_traverse(new_trie):
    new_trie.insert('same same same same same same same same same')
    result = []
    [result.append(item) for item in new_trie.traverse()]
    assert result == ['same']


def test_autocomplete_output(new_trie):
    new_trie.insert('Hello')
    assert list(new_trie.autocomplete('P')) == []
    assert list(new_trie.autocomplete('H')) == ['hello']


@pytest.mark.parametrize('words, search, result', AUTOCOMPLETE_CASES)
def test_autocomplete_multiple(new_trie, words, search, result):
    new_trie.insert(words)
    autocomp = new_trie.autocomplete(search)
    for item in autocomp:
        assert item in result
    assert len(autocomp) <= 4
