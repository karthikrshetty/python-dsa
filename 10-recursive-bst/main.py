class Node:
    """
    Node of a Binary Search Tree.

    Each node contains:
    - value : the data stored
    - left  : reference to left child (values < current node)
    - right : reference to right child (values > current node)
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """
    Binary Search Tree (BST) implementation using recursion.

    BST Property:
    - Left subtree contains values strictly less than node
    - Right subtree contains values strictly greater than node
    """

    def __init__(self):
        """
        Initialize an empty BST.
        """
        self.root = None

    def __r_insert(self, current_node, value):
        """
        Recursive helper for insertion.

        Logic:
        1. If current position is empty → create new node.
        2. If value < current node → recurse left.
        3. If value > current node → recurse right.
        4. Return current node to maintain tree linkage.
        """

        # Base case: insert new node here
        if current_node is None:
            return Node(value)

        # Traverse left subtree
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)

        # Traverse right subtree
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)

        # Return unchanged node reference
        return current_node

    def r_insert(self, value):
        """
        Public insert method.

        Logic:
        1. If tree is empty → assign root.
        2. Otherwise → call recursive insert.
        """

        # Case: empty tree
        if self.root is None:
            self.root = Node(value)

        # Recursive insertion
        self.__r_insert(self.root, value)

    def __r_contains(self, current_node, value):
        """
        Recursive search.

        Logic:
        1. If node is None → value not found.
        2. If value matches → return True.
        3. If value greater → search right subtree.
        4. If value smaller → search left subtree.
        """

        if current_node is None:
            return False

        if value == current_node.value:
            return True

        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

        if value < current_node.value:
            return self.__r_contains(current_node.left, value)

    def r_contains(self, value):
        """
        Public search method.
        """
        return self.__r_contains(self.root, value)

    def min_value(self, current_node):
        """
        Find minimum value in a subtree.

        Logic:
        - Minimum value is the leftmost node.
        - Traverse left until no more left child exists.
        """

        while current_node.left is not None:
            current_node = current_node.left

        return current_node.value

    def __delete_node(self, current_node, value):
        """
        Recursive delete operation.

        Logic:
        1. Traverse tree to locate node.
        2. Handle 3 deletion cases:
           a. Leaf node → remove directly
           b. One child → replace with child
           c. Two children → replace with inorder successor
        """

        if current_node is None:
            return None

        # Traverse left
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)

        # Traverse right
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)

        # Node found
        else:
            # Case 1: Leaf node
            if current_node.left is None and current_node.right is None:
                return None

            # Case 2: Only right child
            elif current_node.left is None:
                current_node = current_node.right

            # Case 2: Only left child
            elif current_node.right is None:
                current_node = current_node.left

            # Case 3: Two children
            else:
                # Find inorder successor (smallest in right subtree)
                sub_tree_min = self.min_value(current_node.right)

                # Replace current node value
                current_node.value = sub_tree_min

                # Delete successor node
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)

        return current_node

    def delete_node(self, value):
        """
        Public delete method.

        ⚠ IMPORTANT BUG FIX:
        - The returned root must be reassigned.
        """

        # BUG FIX: Without this, deleting root breaks the tree
        self.root = self.__delete_node(self.root, value)


# ======================================================
# Example Usage / Test Driver
# ======================================================

my_tree = BinarySearchTree()

# Step 1: Insert elements
my_tree.r_insert(47)
my_tree.r_insert(21)
my_tree.r_insert(76)
my_tree.r_insert(18)
my_tree.r_insert(27)
my_tree.r_insert(52)
my_tree.r_insert(82)

# Step 2: Search operations
print("BST Contains 27:")
print(my_tree.r_contains(27))

print("BST Contains 17:")
print(my_tree.r_contains(17))

# Step 3: Structure verification
print("root:", my_tree.root.value)
print("root.left:", my_tree.root.left.value)
print("root.right:", my_tree.root.right.value)

# Step 4: Delete root node (critical test)
my_tree.delete_node(47)

# Step 5: Verify structure after deletion
print("root:", my_tree.root.value)
print("root.left:", my_tree.root.left.value)
print("root.right:", my_tree.root.right.value)
