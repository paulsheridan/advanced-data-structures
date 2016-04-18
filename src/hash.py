# get(key) return value at key
# set(key,val) store given value at given key
# _hash(key) hash the key provided
# keys may only be strings
# use buckets to store values that share a hash
# dont use dicts


class Hashtable(object):
    """Implement a hashtable."""

    def __init__(self, size=11):
        """Initialize table."""
        self.size = size
        self.table = [[] for x in range(self.size)]

    def set(self, key, value):
        """Store value at given key."""
        hashed_key = self._hash(key)
        self.table[hashed_key].append((key, value))


    def get(self, key):
        """Return value stored at key."""
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


h = Hashtable()
h.set("First", "Awwwww yeeeaaa")
print(h.table)
