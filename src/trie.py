# alphabet, ( ' ), ( $ )


class Trie(object):
    """Implementation of Trie class."""

    def __init__(self):
        """Initialize."""
        self.root = dict()

    def insert(self, token):
        """Insert token into trie."""
        split_token = token.split()
        for word in split_token:
            current = self.root
            for letter in word:
                current = current.setdefault(letter, {})

    def contains(self, token):
        """Return True if token in trie."""
        pass

t = Trie()
t.insert('to')
