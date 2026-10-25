# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

* Stack (LIFO)
* Queue (FIFO)

## Learning Objectives

* Implement stack operations
* Implement queue operations
* Understand LIFO and FIFO behavior
* Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.



Reflection:

I learned through this unit's discussion on how to practically work with linear data structures in Python and ultimately gained a pretty deeper understanding of how restricting certain data can be accessed, whether it's from one end or two ends, it still enforces specific behavior like LIFO and FIFO. A major challenge I encountered was handling the edge cases, specifically preventing the program from crashing when attempting to remove an item from an empty structure. However, I luckily overcame this by adding is\_empty() checks inside the pop(), dequeue(), peek(), and front() methods so they return a more smoother error message instead of throwing an exception.



Comparing stacks and queues in real-world applications shows the difference of why choosing the right structure matters. Stacks, to me, are perfect for reversing actions or tracking history like browser back buttons, while queues are essential for managing shared resources mostly in chronological order, quite similar to print queues or task scheduling.

