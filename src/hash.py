# -*- coding: utf-8 -*-
class Hashtable(object):
    """Implement a hashtable."""

    def __init__(self, size=11):
        """Initialize table."""
        self.size = size
        self.table = [[] for x in range(self.size)]

    def set(self, key, value):
        """Store value at given key."""
        if isinstance(key, str):
            bucket = self.table[self._hash(key)]
            for item in bucket:
                if item[0] == key:
                    bucket.remove(item)
            # bucket = [item for item in bucket if item[0] != key]
            bucket.append((key, value))
        else:
            raise TypeError("Please input a string as your key")

    def get(self, key):
        """Return value stored at key."""
        if isinstance(key, str):
            for item in self.table[self._hash(key)]:
                if item[0] == key:
                    return item[1]
            raise KeyError("Key not in hash.")
        else:
            raise TypeError("Please input a string as your key")

    def _hash(self, key):
        """Determine index by hashing key."""
        int_key = self._str_to_bits(key)
        return int_key % self.size

    def _str_to_bits(self, string):
        """
        Convert string to intiger by converting the string
        to binary and summing the result.
        """
        result = []
        for letter in string:
            bits = bin(ord(letter))[2:]
            bits = '00000000'[len(bits):] + bits
            result.extend([int(bit) for bit in bits])
        result = sum(result)
        return result
