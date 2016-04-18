# get(key) return value at key
# set(key,val) store given value at given key
# _hash(key) hash the key provided
# keys may only be strings
# use buckets to store values that share a hash
# dont use dicts


class Hashtable(object):
    """Implement a hashtable."""

    def __init__(self, fixed_size=11):
        """Initialize table."""
        self.fixed_size = fixed_size

    def _hash(self, key):
        # value at key % 10
        int_key = self._str_to_bits(key)
        return int_key % self.fixed_size

    def _str_to_bits(self, string):
        """Convert unicode to integers."""
        result = []
        for letter in string:
            bits = bin(ord(letter))[2:]
            bits = '00000000'[len(bits):] + bits
            result.extend([int(bit) for bit in bits])
        return result

    def _bits_to_str(self, bits):
        """Convert bits to strings."""
        letters = []
        for bit in range(len(bits) / 8):
            byte = bits[bit * 8:(bit + 1) * 8]
            letters.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
        return ''.join(letters)
