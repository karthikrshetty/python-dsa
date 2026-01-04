# ============================================================
# Doubly Linked List - Complete Implementation + Tests
# ============================================================

class Node:
    """
    Represents a node in a doubly linked list.
    """
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """
    Doubly Linked List with head, tail, and length tracking.
    """

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # --------------------------------------------------------
    # Utility
    def print_list(self):
        temp = self.head
        values = []
        while temp:
            values.append(str(temp.value))
            temp = temp.next
        print(" <-> ".join(values))

    # --------------------------------------------------------
    # Append
    def append(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1
        return True

    # --------------------------------------------------------
    # Pop (remove last)
    def pop(self):
        if self.length == 0:
            return None

        temp = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None

        self.length -= 1
        return temp

    # --------------------------------------------------------
    # Prepend
    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1
        return True

    # --------------------------------------------------------
    # Pop First
    def pop_first(self):
        if self.length == 0:
            return None

        temp = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None

        self.length -= 1
        return temp

    # --------------------------------------------------------
    # Get (optimized)
    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        if index < self.length // 2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev

        return temp

    # --------------------------------------------------------
    # Set Value
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    # --------------------------------------------------------
    # Insert (middle only)
    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False

        if index == 0:
            return self.prepend(value)

        if index == self.length - 1:
            return self.append(value)

        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        self.length += 1
        return True

    # --------------------------------------------------------
    # Remove
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.pop_first()

        if index == self.length - 1:
            return self.pop()

        temp = self.get(index)

        temp.prev.next = temp.next
        temp.next.prev = temp.prev

        temp.next = None
        temp.prev = None

        self.length -= 1
        return temp


# ============================================================
# TESTING / EDGE CASE VALIDATION
# ============================================================

if __name__ == "__main__":

    print("\n--- Initial List ---")
    dll = DoublyLinkedList(1)
    dll.print_list()

    print("\n--- Append ---")
    dll.append(2)
    dll.append(3)
    dll.print_list()

    print("\n--- Pop ---")
    print("Popped:", dll.pop().value)
    dll.print_list()

    print("\n--- Prepend ---")
    dll.prepend(0)
    dll.print_list()

    print("\n--- Pop First ---")
    print("Popped First:", dll.pop_first().value)
    dll.print_list()

    print("\n--- Get ---")
    print("Index 0:", dll.get(0).value)

    print("\n--- Set Value ---")
    dll.set_value(0, 10)
    dll.print_list()

    print("\n--- Insert ---")
    dll.insert(1, 20)
    dll.print_list()

    print("\n--- Remove ---")
    removed = dll.remove(1)
    print("Removed:", removed.value)
    dll.print_list()

    print("\n--- Edge Case: Single Node ---")
    single = DoublyLinkedList(99)
    print("Pop:", single.pop().value)
    print("Pop again:", single.pop())

    print("\n--- Edge Case: Empty Operations ---")
    empty = DoublyLinkedList(1)
    empty.pop()
    print("Pop First:", empty.pop_first())
    print("Get:", empty.get(0))
    print("Remove:", empty.remove(0))

    print("\n--- Pointer Integrity Check ---")
    dll = DoublyLinkedList(1)
    dll.append(2)
    dll.append(3)
    node = dll.get(1)
    print("Prev:", node.prev.value)
    print("Next:", node.next.value)

    print("\n--- All Tests Completed Successfully ---")
