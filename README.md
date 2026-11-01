# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

* Insert values into a list
* Delete values from a list
* Search for values in a list
* Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. How do list operations impact performance in real-world applications?



Reflection: 

The skills I ended up learning was how Python lists handle memory management during insertions and deletions. I definitely did get a better grasp and understanding of why inserting an item at the beginning of a list is much slower (O(n)) than appending it to the end (O(1)), mainly to due the fact that Python has to shift all subsequent elements in memory to make room.



The main challenge I faced had to be when I was ensuring the program wouldn't fail when users tried to delete items by using invalid indices. Luckily, I was able to fix it by adding strict boundary checks, like (if index < 0 or index >= len(lst)), to my delete\_at function, which allowed it to safely return None and print a helpful message instead of throwing an IndexError.



In real-world applications, list operations like these would directly determine an app's performance. For example, a social media feed that constantly uploads new posts at the top (index 0) will likely suffer from O(n) performance delays as the list grows. 

