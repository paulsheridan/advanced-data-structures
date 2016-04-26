# advanced-data-structures
[![Build Status](https://travis-ci.org/paulsheridan/advanced-data-structures.svg?branch=hashtable)](https://travis-ci.org/paulsheridan/advanced-data-structures)

A new data structures repo, brimming with some higher-level data structures.

## Trie
 Trie, also called digital tree and sometimes radix tree or prefix tree (as they can be searched by prefixes), is an ordered tree data structure that is used to store a dynamic set or associative array where the keys are usually strings.
  Our Trie class has two methods, insert and contains. Insert takes a word or words into the Trie and stores them by letter. Contains takes a word and returns True if the word is in the Trie or False if the word is not in the Trie.
  
  
## Binary Search Tree
Binary search trees (BST) are a particular type of containers: data structures that store "items" (such as numbers, names etc.) in memory. They allow fast lookup, addition and removal of items, and can be used to implement either dynamic sets of items, or lookup tables that allow finding an item by its key (e.g., finding the phone number of a person by name).
  Our BST uses one class and has insert(val), balance(), depth(), contains(val), and size() methods. When starting the BST, initialize it   with one value ex. Tree(10); the 10 will be the base value of the tree.


## Hash table
A Hash Table a data structure used to implement an associative array, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.
Source: Wikipedia
