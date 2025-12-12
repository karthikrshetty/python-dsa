# -------------------------------
# Singly Linked List Implementation (Cheatsheet)
# -------------------------------

# Node class: represents a single element in the linked list
class Node:
    def __init__(self, value):
        self.value = value   # stores the data
        self.next = None     # pointer to the next node (default: None)


# LinkedList class: manages nodes and provides operations
class LinkedList:
    def __init__(self, value):
        # Initialize the list with one node
        new_node = Node(value)
        self.head = new_node   # first node in the list
        self.tail = new_node   # last node in the list
        self.length = 1        # number of nodes

    # -------------------------------
    # Add node at the end
    def append(self, value):
        new_node = Node(value)
        if self.head is None:  # empty list case
            self.head = new_node
            self.tail = new_node
        else:                  # attach new node at the tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    # -------------------------------
    # Print all values in the list
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # -------------------------------
    # Remove last node (pop)
    def pop(self):
        if self.length == 0:   # empty list
            return None
        
        temp = self.head
        pre = self.head
        # Traverse until the last node
        while temp.next:
            pre = temp
            temp = temp.next
        
        self.tail = pre        # update tail
        self.tail.next = None  # disconnect last node
        self.length -= 1

        # If list becomes empty
        if self.length == 0:
            self.head = None
            self.tail = None

        return temp.value      # return removed node's value

    # -------------------------------
    # Add node at the beginning
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:   # empty list case
            self.head = new_node
            self.tail = new_node
        else:                  # attach before head
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    # -------------------------------
    # Remove first node
    def pop_first(self):
        if self.length == 0:
            return None
        
        temp = self.head
        self.head = self.head.next  # move head forward
        temp.next = None            # disconnect old head
        self.length -= 1

        if self.length == 0:        # if list becomes empty
            self.tail = None
        return temp

    # -------------------------------
    # Get node at specific index
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):      # traverse until index
            temp = temp.next
        return temp

    # -------------------------------
    # Update value at specific index
    def set_value(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False

    # -------------------------------
    # Insert node at specific index
    def insert(self, index, value):
        if index < 0 or index > self.length:   
            return False
        
        if index == 0:
            return self.prepend(value)
        if index == self.length:               
            return self.append(value)
        
        new_node = Node(value)
        temp = self.get(index - 1)             # node before insertion point
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    # -------------------------------
    # Remove node at specific index
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1   
        return temp

    # -------------------------------
    # Reverse the linked list
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = None
        before = None

        # Standard reversal loop
        while temp is not None:
            after = temp.next
            temp.next = before
            before = temp
            temp = after


# -------------------------------
# Example usage
# -------------------------------

# Start with a linked list containing one node [1]
my_linked_list = LinkedList(1)
print("Initial list:")
my_linked_list.print_list()
print("----------------")

# ---- Append & Prepend ----
my_linked_list.append(2)        # [1,2]
my_linked_list.append(3)        # [1,2,3]
my_linked_list.prepend(0)       # [0,1,2,3]
my_linked_list.append(4)        # [0,1,2,3,4]
my_linked_list.append(5)        # [0,1,2,3,4,5]
print("After append & prepend:")
my_linked_list.print_list()
print("----------------")

# ---- Removals ----
my_linked_list.pop()            # removes last → [0,1,2,3,4]
my_linked_list.pop_first()      # removes first → [1,2,3,4]
print("After pop & pop_first:")
my_linked_list.print_list()
print("----------------")

# ---- Update & Insert ----
my_linked_list.set_value(3, 7)  # set index 3 → 7 → [1,2,3,7]
my_linked_list.insert(2, 8)     # insert 8 at index 2 → [1,2,8,3,7]
print("After set_value & insert:")
my_linked_list.print_list()
print("----------------")

# ---- Remove at index ----
removed_node = my_linked_list.remove(1)  # remove index 1 → removes '2'
print(f"Removed node value: {removed_node.value}")
print("After remove at index 1:")
my_linked_list.print_list()
print("----------------")

# ---- Get value at index ----
print(f"Value at index 1: {my_linked_list.get(1).value}")
print("----------------")

# ---- Reverse ----
my_linked_list.reverse()        # reverse list
print("After reverse:")
my_linked_list.print_list()
print("----------------")
