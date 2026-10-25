"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # Appending and popping from the end of a list is 0(1) time complexity.
        self.items = []
        pass

    def push(self, value):
        # LIFO: The last item added is the first one that will be removed.
        self.items.append(value)
        pass

    def pop(self):
        # Removes and returns the last item in the list
        # Edge Case: Handle empty stack smoothly instead of crashing
        if self.is_empty():
            return "Stack is empty. Cannot pop."
        return self.items.pop()


    def peek(self):
        # Returns the top value (the last item in the list) without removing it.
        if self.is_empty():
            return "Stack is empty. Cannot peek."
        return self.items[-1]


    def is_empty(self):
        # Returns True if the list has no items.
        return len(self.items) == 0



class Queue:
    def __init__(self):
        # collections.deque (double-ended queue) is used because it provides
        # 0(1) time complexity for adding/removing from both ends.
        self.items = deque()
        pass

    def enqueue(self, value):
        # Adds value to the BACK of the queue.
        # FIFO: The first item added will be the first one removed.
        self.items.append(value)
        pass

    def dequeue(self):
        # Removes and returns the value from the FRONT of the queue of the queue.
        # Edge Case: Handle empty queue smoothly
        if self.is_empty():
            return "Queue is empty. Cannot dequeue."
        return self.items.popleft()


    def front(self):
        # Returns the front value (the left most item) without removing it.
        if self.is_empty():
            return "Queue is empty. Cannot view front."
        return self.items[0]


    def is_empty(self):
        # Returns True if the queue has no items.
        return len(self.items) == 0



def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.


    print("\n=== STACK DEMO ===")
    stack = Stack()

    print("Adding 4 items to the stack: 'Book A', 'Book B', 'Book C', 'Book D'")
    stack.push("Book A")
    stack.push("Book B")
    stack.push("Book C")
    stack.push("Book D")

    print("Demonstrating LIFO (Last In, First Out):")
    print(f"Popped: {stack.pop()}") # Should be Book D
    print(f"Popped: {stack.pop()}") # Should be Book C


    print("\nTesting Edge Cases:")
    print(f"Peeking at top item: {stack.peek()}")

    # Empty stack test
    empty_stack = Stack()
    print(f"Popping from empty stack: {empty_stack.pop()}")
    print(f"Peeking at empty stack: {empty_stack.peek()}")

    # Single item stack test
    single_stack = Stack()
    single_stack.push("Only Item")
    single_stack.pop()
    print(f"Is single-item stack empty now? {single_stack.is_empty()}")

# ===============================
# QUEUE DEMO
# ===============================
# Requirements:
# 1. Create a Queue object.
# 2. Add at least 4 values to the queue.
# 3. Improve the print statements so they clearly explain what is happening.
# 4. Demonstrate FIFO behavior.
# 5. Show what happens when dequeue() is used on an empty queue.
#
# Edge Cases:
# 6. Show what happens when front() is used on an empty queue.
# 7. Create a queue with only one item, remove it,
#    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO ===")
    queue = Queue()

    print("Adding 4 customers to the line: 'Customer 1', 'Customer 2', 'Customer 3', 'Customer 4'")
    queue.enqueue("Customer 1")
    queue.enqueue("Customer 2")
    queue.enqueue("Customer 3")
    queue.enqueue("Customer 4")

    print("Demonstrating FIFO (First In, First Out):")
    print(f"Dequeued: {queue.dequeue()}") # Should be Customer 1
    print(f"Dequeued: {queue.dequeue()}") # Should be Customer 2

    print("\nTesting Edge Cases:")
    print(f"Viewing front of queue: {queue.front()}")

    # Empty queue test
    empty_queue = Queue()
    print(f"Dequeuing from empty queue: {empty_queue.dequeue()}")
    print(f"Viewing front of empty queue: {empty_queue.front()}")

    # Single item queue test
    single_queue = Queue()
    single_queue.enqueue("Only Customer")
    single_queue.dequeue()
    print(f"Is single-item queue empty now? {single_queue.is_empty()}")


if __name__ == "__main__":
    main()
