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
            hashed_key = self._hash(key)
            self.table[hashed_key].append((key, value))
        else:
            raise KeyError("Hey, Idiort. Inpork STring 4 key plz")

    def get(self, key):
        """Return value stored at key."""
        if isinstance(key, str):
            hashed_key = self._hash(key)
            for item in self.table[hashed_key]:
                if item[0] == key:
                    return item[1]
        else:
            raise KeyError("Hey, Idiort. Inpork STring 4 key plz")
        pass

    def _hash(self, key):
        """Hash key and determine index."""
        int_key = self._str_to_bits(key)
        return int_key % self.size

    def _str_to_bits(self, string):
        """Convert unicode to integers."""
        result = []
        for letter in string:
            bits = bin(ord(letter))[2:]
            bits = '00000000'[len(bits):] + bits
            result.extend([int(bit) for bit in bits])
        result = sum(result)
        return result

    def _bits_to_str(self, bits):
        """Convert bits to strings."""
        letters = []
        for bit in range(len(bits) / 8):
            byte = bits[bit * 8:(bit + 1) * 8]
            letters.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
        return ''.join(letters)
