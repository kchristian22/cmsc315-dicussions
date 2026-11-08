"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).
"""


class Node:
    def __init__(self, value):
        # Store the node's value and initialize references
        # to the left and right child nodes as None.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # Initialize an empty Binary Search Tree.
        # The root is the top-most node, starting as None.
        self.root = None

    def insert(self, value):
        """
        Insert a value into the BST.
        """
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        Implement recursive BST insertion.
        """
        if node is None:
            return Node(value)

        # BST Rule: Smaller values go left, larger values go right.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        # If the value is equal, ignore duplicates in this basic implementation.
        return node

    def search(self, value):
        """
        Search for a value in the BST.
        """
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        Implement recursive BST search.
        """
        # Base cases: reached the bottom (not found) or found the value.
        if node is None:
            return False
        if node.value == value:
            return True

        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def inorder(self):
        """
        Return a list containing the values from an in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        Implement in-order traversal.
        """
        if node is not None:
            # 1. Visit Left Subtree
            self._inorder_recursive(node.left, values)

            # 2. Visit Current Node
            values.append(node.value)

            # 3. Visit Right Subtree
            self._inorder_recursive(node.right, values)

        # This traversal strictly follows
        # the BST rule: Left (smaller) -> Root -> Right (larger).


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TREE CONSTRUCTION
    # ===============================
    print("\n=== TREE CONSTRUCTION ===")
    bst = BST()
    values_to_insert = [50, 30, 70, 20, 40, 60, 80]

    print(f"Inserting values: {values_to_insert}")
    for val in values_to_insert:
        bst.insert(val)

    # To find 80 only check 50 -> 70 -> 80, need to be checked
    # ignoring the entire left side of the tree.

    # ===============================
    # IN-ORDER TRAVERSAL
    # ===============================
    print("\n=== IN-ORDER TRAVERSAL ===")
    sorted_values = bst.inorder()
    print(f"In-order traversal results: {sorted_values}")

    # ===============================
    # SEARCH TESTS
    # ===============================
    print("\n=== SEARCH TESTS ===")

    # Search for existing values
    print(f"Searching for 40 (exists): {bst.search(40)}")
    print(f"Searching for 80 (exists): {bst.search(80)}")

    # Search for non-existing values
    print(f"Searching for 25 (does not exist): {bst.search(25)}")
    print(f"Searching for 100 (does not exist): {bst.search(100)}")

    # ===============================
    # EDGE CASES
    # ===============================
    print("\n=== EDGE CASES ===")

    # Edge Case 1: Traversing an empty tree
    empty_bst = BST()
    print(f"Traversing empty tree: {empty_bst.inorder()}")

    # Edge Case 2: Searching an empty tree
    print(f"Searching in empty tree: {empty_bst.search(10)}")

    # Edge Case 3: Inserting duplicate values
    print("\nInserting a duplicate value (50) into the original tree...")
    bst.insert(50) 
    print(f"Tree after duplicate insertion: {bst.inorder()} (No duplicate added)")


if __name__ == "__main__":
    main()