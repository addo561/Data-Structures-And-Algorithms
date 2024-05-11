# ALGORITHMS.

1. **Sorting Algorithms**:
   - **Bubble Sort**: Imagine sorting a deck of cards by repeatedly swapping adjacent cards if they're in the wrong order.
     Example: `[5, 3, 8, 1, 2]` becomes `[1, 2, 3, 5, 8]`.
   - **Selection Sort**: Pick the smallest element and swap it with the first element, then pick the second smallest and swap it with the second element, and so on.
     Example: `[5, 3, 8, 1, 2]` becomes `[1, 2, 3, 5, 8]`.
   - **Insertion Sort**: Imagine sorting playing cards in your hand, where you pick one card at a time and insert it into its correct position.
     Example: `[5, 3, 8, 1, 2]` becomes `[1, 2, 3, 5, 8]`.
   - **Merge Sort**: Divide the array into halves, sort each half, and then merge them back together.
     Example: `[5, 3, 8, 1, 2]` becomes `[1, 2, 3, 5, 8]`.
   - **Quick Sort**: Pick a 'pivot', partition the array into elements smaller and larger than the pivot, then recursively sort the partitions.
     Example: `[5, 3, 8, 1, 2]` becomes `[1, 2, 3, 5, 8]`.
   - **Heap Sort**: Build a max-heap from the array, repeatedly extract the maximum element from the heap and rebuild the heap.
     Example: `[5, 3, 8, 1, 2]` becomes `[1, 2, 3, 5, 8]`.

2. **Searching Algorithms**:
   - **Linear Search**: Go through each element of the array one by one until finding the target.
   - **Binary Search**: Divide and conquer approach; repeatedly halve the search space until finding the target.

3. **Dynamic Programming**:
   - **Fibonacci Sequence**: Each number is the sum of the two preceding ones.
   - **Longest Common Subsequence (LCS)**: Find the longest subsequence present in given two sequences of characters.
   - **Knapsack Problem**: Given items with certain weights and values, determine the maximum value that can be carried in a knapsack of a given capacity.
   - **Coin Change Problem**: Determine the number of ways to make change for a given amount of money.

4. **Graph Algorithms**:
   - **Depth-First Search (DFS)**: Explore as far as possible along each branch before backtracking.
   - **Breadth-First Search (BFS)**: Explore all the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.
   - **Dijkstra's Algorithm**: Find the shortest path between nodes in a graph.
   - **Bellman-Ford Algorithm**: Find the shortest path from a single source vertex to all other vertices.
   - **Floyd-Warshall Algorithm**: Find shortest paths in a weighted graph with positive or negative edge weights (but with no negative cycles).
   - **Prim's Algorithm**: Find a minimum spanning tree for a weighted undirected graph.
   - **Kruskal's Algorithm**: Find a minimum spanning tree for a connected weighted graph.

5. **String Algorithms**:
   - **Longest Common Subsequence (LCS)**: Find the longest subsequence present in given two sequences of characters.
   - **Longest Palindromic Subsequence**: Find the longest subsequence of a string that is also a palindrome.
   - **Knuth-Morris-Pratt Algorithm (KMP)**: Efficient string searching algorithm that searches for occurrences of a "word" within a main "text" string.
   - **Rabin-Karp Algorithm**: A string-searching algorithm that uses hashing to find any one of a set of pattern strings in a text.

6. **Tree Algorithms**:
   - **Binary Tree Traversal**: Visiting each node in a binary tree in a specific order (preorder, inorder, postorder).
   - **Binary Search Tree (BST)** operations: Insertion, deletion, and searching in a binary search tree.
   - **Lowest Common Ancestor (LCA)**: Find the lowest common ancestor of two nodes in a binary tree.
   - **Trie (Prefix Tree)**: An efficient information retrieval data structure used for storing and retrieving strings.

7. **Backtracking Algorithms**:
   - **N-Queens Problem**: Place N queens on an N×N chessboard so that no two queens threaten each other.
   - **Subset Generation**: Generate all possible subsets of a set.
   - **Permutations**: Generate all possible permutations of a sequence.
   - **Sudoku Solver**: Solve a Sudoku puzzle by filling the empty cells with the correct numbers.

These are simplified explanations with examples to give you a basic understanding of each algorithm's purpose and how it works.

ALL OTHER ALGORITHMS WILL BE ADDED SOON(+ IMPLEMENTATION).


DATA STURCTURES



1. **Arrays**: A collection of elements stored at contiguous memory locations. Elements can be accessed using an index. Arrays have constant-time access to elements, but insertion and deletion may require shifting elements, resulting in a time complexity of O(n).

2. **Linked Lists**: Elements are stored in nodes where each node points to the next node in the sequence. Linked lists support efficient insertion and deletion operations (O(1)) compared to arrays. However, accessing an element at a specific index requires traversing the list, resulting in O(n) time complexity.

3. **Stacks**: A Last In, First Out (LIFO) data structure where elements are added and removed from the same end, called the top. Operations include push (add an element to the top) and pop (remove the top element). Stacks can be implemented using arrays or linked lists.

4. **Queues**: A First In, First Out (FIFO) data structure where elements are added at the rear and removed from the front. Operations include enqueue (add an element to the rear) and dequeue (remove an element from the front). Like stacks, queues can be implemented using arrays or linked lists.

5. **Trees**: A hierarchical data structure consisting of nodes connected by edges. The top node is called the root, and each node has zero or more child nodes. Trees can be binary (each node has at most two children) or n-ary (each node can have multiple children).

6. **Binary Trees**: A special type of tree where each node has at most two children. Variants include binary search trees (BST), where the left child is less than the parent and the right child is greater, ensuring efficient search, insertion, and deletion operations with a time complexity of O(log n) in balanced trees.

7. **Graphs**: A non-linear data structure consisting of nodes (vertices) and edges that connect these nodes. Graphs can be directed (edges have a direction) or undirected (edges have no direction). Graphs can be represented using adjacency matrices or adjacency lists.



**Types of Binary Trees:**

1. **Binary Search Trees (BST)**: As mentioned earlier, in a BST, each node has at most two children, and for every node:
   - The left child's value is less than the parent's value.
   - The right child's value is greater than the parent's value.
   BSTs enable efficient searching, insertion, and deletion operations with an average time complexity of O(log n) for balanced trees.

2. **AVL Trees**: A self-balancing binary search tree where the heights of the two child subtrees of any node differ by at most one. This ensures that the tree remains balanced, maintaining O(log n) time complexity for basic operations.

3. **Red-Black Trees**: Another type of self-balancing binary search tree. In a red-black tree, each node is colored either red or black, and it must satisfy certain properties that ensure the tree remains balanced. Red-black trees also provide O(log n) time complexity for basic operations.

**Depth-First Search (DFS):**

DFS is an algorithm for traversing or searching tree or graph data structures. It starts at a root node and explores as far as possible along each branch before backtracking. There are several variants of DFS, including:
- **Pre-order DFS**: Visit the current node, then recursively visit the left subtree, and finally the right subtree.
- **In-order DFS**: Recursively visit the left subtree, then the current node, and finally the right subtree. In binary search trees, in-order DFS visits nodes in ascending order.
- **Post-order DFS**: Recursively visit the left subtree, then the right subtree, and finally the current node.

**Breadth-First Search (BFS):**

BFS is an algorithm for traversing or searching tree or graph data structures. It starts at a root node and explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level. BFS uses a queue data structure to keep track of nodes to visit. It guarantees the shortest path between the starting node and any other reachable node in an unweighted graph.

Understanding these types of binary trees and traversal algorithms provides a deeper insight into data structure manipulation and graph traversal techniques.




CODES WILL BE UPDATED SOON
