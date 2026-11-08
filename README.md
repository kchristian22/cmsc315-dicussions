# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

* Build a BST
* Insert values recursively
* Search recursively
* Perform in-order traversal
* Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.



Reflection:



The skills and concepts I learned was how to build and traverse a Binary Search Tree using recursion. I would say I was able to gain a deeper understanding of how the BST ordering property allows us to discard half the tree at every step during a search.

My main challenge was visualizing how the recursive \_insert\_recursive method actually rebuilt the tree as the stack unwound. So to overcome it, I drew out the tree on paper and traced lines to exactly where the node.left and node.right pointers were pointing after each recursive call returned. Compared to other data structures, the BST's specific ordering creates massive efficiency gains. Searching an unsorted array or linked list would need O(n) linear time because it's necessary to check every single item. A BST, however, uses its structural order to achieve O(log n) search time by cutting the search space in half at every node.

