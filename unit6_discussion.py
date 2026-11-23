"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""

"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.
    #
    # How a dictionary behaves like a hash table:
    # A Python dict is backed by a hash table. Each key is passed through
    # a hash function to compute an index (bucket) in an underlying array.
    # The value is stored at that index. On lookup, the same hash function
    # is recomputed, giving O(1) average access time instead of scanning
    # every entry. Python also stores keys in insertion order (3.7+), but
    # the lookup mechanism itself is hash-based.

    print("\n=== INSERT OPERATIONS ===")
    print("TODO: Create a dictionary and add multiple key-value pairs.")

    # Simulating a restaurant reservation system (matching the scenario prompt)
    reservations = {}  # Empty hash table

    # Insert 5+ key-value pairs. Each insert hashes the key to find a bucket.
    reservations["Smith"] = {"party_size": 4, "time": "7:00 PM"}
    reservations["Johnson"] = {"party_size": 2, "time": "7:15 PM"}
    reservations["Garcia"] = {"party_size": 6, "time": "7:30 PM"}
    reservations["Chen"] = {"party_size": 3, "time": "7:45 PM"}
    reservations["Patel"] = {"party_size": 5, "time": "8:00 PM"}

    print(f"Reservation table now holds {len(reservations)} entries:")
    for name, details in reservations.items():
        print(f"  {name}: {details}")

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.
    #
    # Lookup: Python hashes the key ("Garcia"), computes the bucket index,
    # and returns the value stored there — no linear scan required. This is
    # why lookup is O(1) on average.

    print("\n=== LOOKUP OPERATIONS ===")
    print("TODO: Demonstrate successful key lookups.")

    lookup_names = ["Garcia", "Patel"]
    for name in lookup_names:
        # Hash the key -> find bucket -> return value (average O(1))
        details = reservations.get(name)
        print(f"  Lookup '{name}' -> {details}")

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.
    #
    # When an existing key is assigned a new value, Python hashes the key,
    # locates the existing bucket, and overwrites the value. The key is NOT
    # duplicated and the table size does not change — this is an in-place
    # update.

    print("\n=== UPDATE OPERATIONS ===")
    print("TODO: Demonstrate updating an existing key.")

    print("Before update:", reservations["Smith"])
    # Overwrite value for existing key "Smith" (party grew from 4 to 8)
    reservations["Smith"] = {"party_size": 8, "time": "7:00 PM"}
    print("After update: ", reservations["Smith"])
    print(f"Table size unchanged: {len(reservations)} entries")

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.
    #
    # Deleting a key hashes the key, finds its bucket, and marks/removes the
    # entry. Python uses a "dummy" tombstone marker internally so that probe
    # sequences for other keys remain valid — otherwise later lookups could
    # incorrectly stop early.

    print("\n=== DELETE OPERATIONS ===")
    print("TODO: Demonstrate deleting a key-value pair.")

    print(f"Before delete, entries: {list(reservations.keys())}")
    del reservations["Johnson"]  # Remove by key
    print(f"After delete, entries:  {list(reservations.keys())}")
    print(f"Current size: {len(reservations)}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Edge case 1: Lookup a missing key
    # Using .get() returns None (or a default) instead of raising KeyError.
    missing = reservations.get("Nguyen")
    print(f"1. Lookup missing key 'Nguyen' with .get() -> {missing} (no crash)")

    # Edge case 2: Delete a missing key safely
    # pop() with a default avoids KeyError on absent keys.
    removed = reservations.pop("Nguyen", None)
    print(f"2. Safe delete of missing key 'Nguyen' with .pop(default) -> {removed}")

    # Edge case 3: Update a missing key
    # Assigning to a new key inserts it rather than erroring — worth noting
    # because it can silently create unintended entries.
    reservations["Lopez"] = {"party_size": 2, "time": "8:15 PM"}
    print(f"3. Updating missing key 'Lopez' inserted a new entry: {reservations['Lopez']}")

    # Edge case 4: Empty dictionary behavior
    empty = {}
    print(f"4. Empty dict: len={len(empty)}, .get('anything')={empty.get('anything')}")
    print("   Lookups on an empty table return the default; no exception is raised.")


if __name__ == "__main__":
    main()
