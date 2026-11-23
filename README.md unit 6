# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

* Insert key-value pairs
* Retrieve values efficiently
* Update existing values
* Remove entries
* Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.



Reflection: 



What primary strengthened my understanding with this assignment was how Python dictionaries work under the hood. I learned that a dictionary is not just a convenient container in Python but an implementation of a hash table. Hash Tables themselves each have a key that runs through a hash function to compute a bucket index, which is why lookups stay O(1) on average even as the table grows. I also learned how collision resolution actually works, in which Python uses open addressing with probing, and deletions leave "tombstone" markers so later lookups don't stop early.



My biggest challenge had to be the edge cases for this assignment and trying to wrap my head around understanding them. Initially I assumed deleting a missing key or looking up an absent key would simply do nothing, but Python raised a KeyError unless I used safe access patterns like .get(key, default) or .pop(key, None). Thankfully, I overcame this by testing each edge case in isolation and documenting the difference in comments.



Collisions in codes normally happen when two distinct keys hash to the same bucket. If they're handled poorly, they turn O(1) lookups into O(n) linear scans, especially as the load factor climbs. Resizing and rehashing keep performance stable, which is why hash tables power reservation systems, caches, and profile lookups so efficiently.



