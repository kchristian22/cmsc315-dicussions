"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""

def linear_search(lst, target):
    """
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    for index in range(len(lst)):
        if lst[index] == target:
            return index          # found: report position immediately
    return -1                     # exhausted the list: not present


def binary_search(lst, target):
    """
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    # Binary search requires sorted data. Must maintain a "window" [low, high]
    # of indices that could still contain the target.
    low = 0
    high = len(lst) - 1

    while low <= high:
        # Compute the middle of the current window.
        mid = low + (high - low) // 2

        if lst[mid] == target:
            return mid            # found the target at the midpoint

        elif lst[mid] < target:
            # The midpoint is too small. Because the list is sorted,
            # EVERY element at or left of mid is also too small.
            low = mid + 1

        else:  # lst[mid] > target
            high = mid - 1

    return -1          # window collapsed: target is not present

def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    small_data = [3, 7, 11, 15, 19, 23, 27]

    # Linear search scans 0,1,2,3,4,5 -> returns 5.
    # Binary search checks mid=3 (15<23) -> mid=5 (23==23) -> returns 5.
    print(f"Dataset: {small_data}")
    print(f"Search for 23 (present):")
    print(f"  linear_search -> index {linear_search(small_data, 23)}")
    print(f"  binary_search -> index {binary_search(small_data, 23)}")

    # Linear search must examine ALL 7 elements before returning -1.
    # Binary search checks mid=3 (15<20) -> mid=5 (23>20) -> mid=4 (19<20)
    print(f"Search for 20 (absent):")
    print(f"  linear_search -> index {linear_search(small_data, 20)}")
    print(f"  binary_search -> index {binary_search(small_data, 20)}")

    # ===============================
    # LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")

    large_data = list(range(0, 200000, 2))   # 100,000 elements

    target_present = 199998
    target_absent = 199997   # odd number -> guaranteed absent

    print(f"Dataset size: {len(large_data):,} (sorted)")
    print(f"Search for {target_present} (present, worst case for linear):")
    print(f"  linear_search -> index {linear_search(large_data, target_present)}")
    print(f"  binary_search -> index {binary_search(large_data, target_present)}")

    print(f"Search for {target_absent} (absent):")
    print(f"  linear_search -> index {linear_search(large_data, target_absent)}")
    print(f"  binary_search -> index {binary_search(large_data, target_absent)}")

    # Why binary search wins as data grows:
    # Linear search cost grows as n.  Binary search cost grows as log2(n).
    #   n = 10        -> linear <= 10 steps, binary <= 4 steps
    #   n = 1,000     -> linear <= 1,000 steps, binary <= 10 steps
    #   n = 100,000   -> linear <= 100,000 steps, binary <= 17 steps
    #   n = 1,000,000 -> linear <= 1,000,000 steps, binary <= 20 steps
    # Binary search's cost barely changes when the dataset size multiplies,
    # which is why it scales a lot better for larger collections.

    # ===============================
    # EDGE CASE TESTS
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Linear search: the loop body never runs, so it returns -1 immediately.
    # Binary search: high = -1, so the while condition (0 <= -1) is false
    # and the loop is skipped, returning -1. Neither algorithm crashes.
    empty = []
    print(f"Empty list []:")
    print(f"  linear_search(5) -> {linear_search(empty, 5)}  (expected -1)")
    print(f"  binary_search(5) -> {binary_search(empty, 5)}  (expected -1)")

    # Linear search checks index 0 -> returns 0.
    # Binary search: low=0, high=0, mid=0 -> match -> returns 0.
    single = [42]
    print(f"Single-element list [42], searching for 42:")
    print(f"  linear_search -> {linear_search(single, 42)}  (expected 0)")
    print(f"  binary_search -> {binary_search(single, 42)}  (expected 0)")

    # Both algorithms correctly return -1; the window/loop handles it.
    print(f"Single-element list [42], searching for 7:")
    print(f"  linear_search -> {linear_search(single, 7)}  (expected -1)")
    print(f"  binary_search -> {binary_search(single, 7)}  (expected -1)")

    # Linear search finds it in 1 comparison.
    # Binary search will narrow down to index 0 after several midpoints,
    # so for tiny first-position hits linear can actually be faster.
    first_hit = [10, 20, 30, 40, 50]
    print(f"List {first_hit}, searching for 10 (first element):")
    print(f"  linear_search -> {linear_search(first_hit, 10)}  (expected 0)")
    print(f"  binary_search -> {binary_search(first_hit, 10)}  (expected 0)")

    # Linear search must scan all 5 elements (worst case).
    # Binary search still uses only ~log2(5) steps.
    print(f"List {first_hit}, searching for 50 (last element):")
    print(f"  linear_search -> {linear_search(first_hit, 50)}  (expected 4)")
    print(f"  binary_search -> {binary_search(first_hit, 50)}  (expected 4)")


if __name__ == "__main__":
    main()