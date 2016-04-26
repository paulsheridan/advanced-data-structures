# alphabet, ( ' ), ( $ )


class Trie(object):
    """Implementation of Trie class."""

    def __init__(self):
        """Initialize."""
        self.root = dict()

    def insert(self, input_str):
        """Insert token into trie."""
        tokens = input_str.split()
        for token in tokens:
            current = self.root
            for letter in token:
                current = current.setdefault(letter, {})
            current.setdefault('$', {})

    def contains(self, token):
        """Return True if token in trie."""
        current = self.root
        try:
            for letter in token:
                current = current[letter]
            return current['$'] == {}
        except KeyError:
            return False
