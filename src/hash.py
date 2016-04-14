# get(key) return value at key
# set(key,val) store given value at given key
# _hash(key) hash the key provided
# keys may only be strings
# use buckets to store values that share a hash

class Hashtable(Object):
    """Implement a hashtable."""

    def __init__(self, fixed_size=11):

