<h1 align="center">TREES</h1>

- Trees are an example of non-linear data structures where each element is connected to more than two adjacent elements creating a hierarchical structure. 
- Trees comprise of nodes whereby a node basically comprises of a data element and a reference to the next node (either the left or right pointer). 

<img src="../../../assets/Trees/TreesTerms.png"/>

## Terminologies in Trees:

1. **Root Node**: The topmost node in a tree.
2. **Parent Node**: A node that has child nodes.
3. **Child Node**: A node that has a parent node.
4. **Leaf Node**: A node that does not have any child nodes.
5. **Siblings**: Nodes that share the same parent node.
6. **Ancestor**: A node that is on the path from the root node to a given node.
7. **Descendant**: A node that is on the path from a given node to a leaf node.
8. **Depth of a Node**: The number of edges from the root node to the given node.
9. **Height of a Node**: The number of edges on the longest path from the given node to a leaf node.
10. **Height of a Tree**: The height of the root node.*

## Types of Trees:
> Based on the number of children each node can have:

- Binary Trees: Each node has at most two children.
- Ternary Trees: Each node has at most three children.
- n-ary Trees (or Generic Trees): Each node can have any number of children.

> Based on the arrangement and structure of nodes:

- Full Binary Tree: Each node has either 0 or 2 children, and all leaves are at the same level.
- Complete Binary Tree: Every level, except possibly the last, is completely filled, and all nodes are as far left as possible.
- Perfect Binary Tree: All internal nodes have exactly two children, and all leaf nodes are at the same level.
- Balanced Binary Tree: The height of the left and right subtrees of any node differ by no more than one. Examples include AVL trees and Red-Black trees.
- Skewed Binary Tree: All nodes have only one child, either left or right.
- Degenerate (or Pathological) Tree: Each parent node has only one associated child node, essentially behaving like a linked list.

> Based on specific properties or functionality:

- Binary Search Tree (BST): A binary tree where the left subtree contains nodes with values less than the node's value, and the right subtree contains nodes with values greater than the node's value.
- Heap: A specialized tree-based data structure where each node satisfies the heap property, commonly used for implementing priority queues.
- Trie (Prefix Tree): A tree structure used for storing a dynamic set of strings or keys, where each node represents a common prefix of its children.
- Segment Tree: A tree data structure used for storing information about intervals or segments of an array.

## Applications of Trees
- Hierarchical Data Storage: Trees are commonly used to represent hierarchical structures such as file systems, organization charts, XML/HTML document structures, and directory structures in operating systems.

- Binary Search Trees (BST): BSTs are used for implementing data structures that require efficient searching, insertion, and deletion operations, such as dictionaries, symbol tables, and database indexing.

- Balanced Trees: Balanced tree structures like AVL trees and Red-Black trees are used in database management systems, where maintaining balanced trees ensures efficient retrieval and manipulation of data.

- Trie (Prefix Tree): Tries are used for implementing dictionary data structures and for efficient searching and prefix matching operations, making them suitable for applications like auto-complete features in text editors and search engines.

- Binary Heap: Binary heaps are used in priority queues and scheduling algorithms, where efficient retrieval of the maximum or minimum element is required.

- Syntax Trees (Parse Trees): Trees are used in compilers and parsing algorithms to represent the syntactic structure of programs or expressions, facilitating analysis and interpretation.

- Decision Trees: Decision trees are used in machine learning and data mining for classification and regression tasks, where they represent a sequence of decisions and outcomes.

- Game Trees: Trees are used to represent the possible moves and outcomes in games like chess, tic-tac-toe, and card games, facilitating game-playing algorithms and artificial intelligence