"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    # Insertion into a Python list shifts all elements at and after the
    # given index to the right to make room for the new item.
    lst.insert(index, value)
    pass


def delete_at(lst, index):
    # Validation is needed to prevent an IndexError from crashing the program itself.
    # Safe deletion checks if the index is within the valid bounds of the list.
    if index < 0 or index >= len(lst):
        return None

    # Deleting an element shifts all subsequent elements to the left to fill the gap.
    return lst.pop(index)


def search_value(lst, value):
    # This is a linear search (O(n) time complexity). Because a Python list
    # does not have keys (like a dictionary), it must scan sequentially from
    # the beginning to the end until it finds a match.
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # INSERTION TESTS
    # ===============================
    print("\n=== INSERTION TESTS ===")
    my_list = [10, 20, 30, 40, 50]
    print(f"Original List: {my_list}")

    # Insert at the beginning (index 0). This is O(n) because all items shift right.
    insert_at(my_list, 0, 5)
    print(f"After inserting 5 at the beginning: {my_list}")

    # Insert in the middle (index 3). Items from index 3 onward shift right.
    insert_at(my_list, 3, 25)
    print(f"After inserting 25 in the middle: {my_list}")

    # Insert at the end (index = len). This is O(1) because nothing needs to shift.
    insert_at(my_list, len(my_list), 60)
    print(f"After inserting 60 at the end: {my_list}")

    # ===============================
    # DELETION TESTS
    # ===============================
    print("\n=== DELETION TESTS ===")

    # Delete from the beginning. All items shift left.
    removed = delete_at(my_list, 0)
    print(f"Removed {removed} from the beginning. Updated list: {my_list}")

    # Delete from the middle. Items after the deleted index shift left.
    removed = delete_at(my_list, 3)
    print(f"Removed {removed} from the middle. Updated list: {my_list}")

    # Delete from the end. This is O(1) because no items need to shift.
    removed = delete_at(my_list, len(my_list) - 1)
    print(f"Removed {removed} from the end. Updated list: {my_list}")


    # ===============================
    # SEARCH TESTS
    # ===============================
    print("\n=== SEARCH TESTS ===")
    search_list = [100, 200, 300, 400, 500]
    print(f"Search List: {search_list}")

    # Search for a value that exists.
    found_index = search_value(search_list, 300)
    print(f"Searching for 300: Found at index {found_index}")

    # Search for a value that does not exist.
    not_found_index = search_value(search_list, 999)
    print(f"Searching for 999: Result is {not_found_index} (Not found)")


    # ===============================
    # EDGE CASES
    # ===============================
    print("\n=== EDGE CASES ===")

    # Edge Case 1: Delete using an invalid index.
    print(f"Attempting to delete at invalid index 10: {delete_at(my_list, 10)}")

    # Edge Case 2: Insert into an empty list.
    empty_list = []
    print(f"Empty list before insertion: {empty_list}")
    insert_at(empty_list, 0, 99)
    print(f"Empty list after inserting 99: {empty_list}")


if __name__ == "__main__":
    main()