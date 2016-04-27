# -*- coding: utf-8 -*-


class Trie(object):
    """Implementation of Trie class."""

    def __init__(self):
        """Initialize."""
        self.root = dict()

    def _validate(self, token):
        """Check for valid input."""
        if not isinstance(token, str):
            raise TypeError('Only strings plz')
        if "$" in token:
            raise ValueError('Do not include $ in the token')

    def insert(self, input_str):
        """Insert token into trie."""
        self._validate(input_str)
        tokens = input_str.lower().split()
        for token in tokens:
            current = self.root
            for letter in token:
                current = current.setdefault(letter, {})
            current.setdefault('$', {})

    def contains(self, input_str):
        """Return True if token in trie."""
        self._validate(input_str)
        token = input_str.lower()
        current = self.root
        try:
            for letter in token:
                current = current[letter]
            return current['$'] == {}
        except KeyError:
            return False

    def traverse(self, start=None, word=''):
        """Traverse trie and return generator of all words."""
        if not start:
            start = self.root
        for key in start.keys():
            if key == '$':
                yield word
            else:
                for each in self.traverse(start[key], word + key):
                    yield each

    def autocomplete(self, prefix):
        """Autocomplete given a prefix."""
        result = []
        current = self.root
        for letter in prefix:
            if letter not in current:
                return []
            current = current[letter]
        output = self.traverse(current)
        for item in output:
            result.append(prefix + item)
        return result
