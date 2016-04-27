# advanced-data-structures
[![Build Status](https://travis-ci.org/paulsheridan/advanced-data-structures.svg?branch=hashtable)](https://travis-ci.org/paulsheridan/advanced-data-structures)

A new data structures repo, brimming with some higher-level data structures.

## Trie
 Trie, also called digital tree and sometimes radix tree or prefix tree (as they can be searched by prefixes), is an ordered tree data structure that is used to store a dynamic set or associative array where the keys are usually strings.
  Our Trie class has two methods, insert and contains. Insert takes a word or words into the Trie and stores them by letter. Contains takes a word and returns True if the word is in the Trie or False if the word is not in the Trie.

## Insert Sort
Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.
    Our insertion sort compares the index values one-by-one to determine placement.

##Merge Sort
Merge sort is an efficient, general-purpose, comparison-based sorting algorithm. Most implementations produce a stable sort, which means that the implementation preserves the input order of equal elements in the sorted output. Mergesort is a divide and conquer algorithm.
    Our merge sort splits an array of values into single value arrays then remerges and compares the new arrays to other arrays until the origin aray is sorted.

##Quick Sort
Quicksort is a comparison sort, meaning that it can sort items of any type for which a "less-than" relation (formally, a total order) is defined. In efficient implementations it is not a stable sort, meaning that the relative order of equal sort items is not preserved. Quicksort can operate in-place on an array, requiring small additional amounts of memory to perform the sorting.
    Our quick sort utilizes a random pivot value in the list and begins comparison and reordering from that value. It runs recursively until the list is sorted.

##Radix Sort
Radix sort is a non-comparative integer sorting algorithm that sorts data with integer keys by grouping keys by the individual digits which share the same significant position and value. A positional notation is required, but because integers can represent strings of characters (e.g., names or dates) and specially formatted floating point numbers, radix sort is not limited to integers.
    Our radix sort takes each item in a list, and depending on the size of our sort bin, we place each item into buckets based on the size of the item, which ultimately sorts the list.
  
## Binary Search Tree
Binary search trees (BST) are a particular type of containers: data structures that store "items" (such as numbers, names etc.) in memory. They allow fast lookup, addition and removal of items, and can be used to implement either dynamic sets of items, or lookup tables that allow finding an item by its key (e.g., finding the phone number of a person by name).
  Our BST uses one class and has insert(val), balance(), depth(), contains(val), and size() methods. When starting the BST, initialize it   with one value ex. Tree(10); the 10 will be the base value of the tree.


## Hash table
A Hash Table a data structure used to implement an associative array, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.
Source: Wikipedia
