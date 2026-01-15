# ============================================================
# Node class for Binary Search Tree
# ============================================================

class Node:
    def __init__(self, value):
        # Value stored in the node
        self.value = value

        # Pointer to left child (values < current node)
        self.left = None

        # Pointer to right child (values > current node)
        self.right = None


# ============================================================
# Binary Search Tree (BST) Implementation
# ============================================================

class BinarySearchTree:
    def __init__(self):
        # Root of the BST (initially empty)
        self.root = None

    def insert(self, value):
        """
        Inserts a value into the BST.
        Returns True if insertion is successful.
        Returns False if duplicate value is found.
        """

        new_node = Node(value)

        # Case 1: Empty tree
        if self.root is None:
            self.root = new_node
            return True

        # Start traversal from the root
        temp = self.root

        while True:
            # Duplicate value check
            if new_node.value == temp.value:
                return False

            # Go left if value is smaller
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left

            # Go right if value is larger
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        """
        Searches for a value in the BST.
        Returns True if found, otherwise False.
        """

        temp = self.root

        # Traverse until node is found or tree ends
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True

        return False


# ============================================================
# BST Testing (including structure and search cases)
# ============================================================

print("---- BST INSERTION TEST ----")

my_tree = BinarySearchTree()

# Insert values
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)
my_tree.insert(4)
my_tree.insert(7)
my_tree.insert(6)
my_tree.insert(5)
my_tree.insert(10)
my_tree.insert(8)

# Root and immediate children validation
print("Root:", my_tree.root.value)
print("Root Left:", my_tree.root.left.value)
print("Root Right:", my_tree.root.right.value)

print("\n---- BST SEARCH TEST ----")

print("Contains 10:", my_tree.contains(10))  # Expected: True
print("Contains 9:", my_tree.contains(9))    # Expected: False
