<h1 align="center">Tries</h1>

The word "Trie" is an excerpt from the word "retrieval". Trie is a sorted tree-based data-structure that stores the set of strings. It has the number of pointers equal to the number of characters of the alphabet in each node. It can search a word in the dictionary with the help of the word's prefix. For example, if we assume that all strings are formed from the letters 'a' to 'z' in the English alphabet, each trie node can have a maximum of 26 points.

Trie is also known as the digital tree or prefix tree. The position of a node in the Trie determines the key with which that node is connected.
Properties of the Trie for a set of the string:

The diagram below depicts a trie representation for the bell, bear, bore, bat, ball, stop, stock, and stack.
Trie Data Structure

<img src="../../../../assets/Trees/trie-data-structure.png"/>

<h1>Properties of Tries</h1>

- The root node of the trie always represents the null node.
- Each child of nodes is sorted alphabetically.
- Each node can have a maximum of 26 children (A to Z).
- Each node (except the root) can store one letter of the alphabet.


<h2>Basic Operations of Tries</h2>

- There are three operations in the Trie:

1. Insertion of a node
2. Searching a node
3. Deletion of a node



<a href="https://leetcode.com/problems/implement-trie-prefix-tree/">LeetCode Practice Question</a>