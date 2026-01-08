# ============================================================
# Node class (shared by Stack and Queue)
# ============================================================

class Node:
    def __init__(self, value):
        # Stores the data of the node
        self.value = value
        
        # Pointer to the next node in the linked list
        self.next = None


# ============================================================
# Stack Implementation (LIFO) using Linked List
# ============================================================

class Stack:
    def __init__(self, value):
        # Create the first node
        new_node = Node(value)
        
        # Top always points to the latest inserted node
        self.top = new_node
        
        # Height tracks number of elements in stack
        self.height = 1

    def print_stack(self):
        # Start traversal from the top
        temp = self.top
        
        # Traverse until the end
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        # Create a new node for the value
        new_node = Node(value)

        # If stack is empty
        if self.height == 0:
            self.top = new_node
        else:
            # Link new node to current top
            new_node.next = self.top
            
            # Move top to new node
            self.top = new_node

        # Increment stack height
        self.height += 1

    def pop(self):
        # If stack is empty, nothing to pop
        if self.height == 0:
            return None

        # Store the current top node
        temp = self.top

        # Move top pointer to next node
        self.top = self.top.next

        # Disconnect popped node from stack
        temp.next = None

        # Decrement stack height
        self.height -= 1

        # Return popped node
        return temp


# ============================================================
# Stack Testing (including edge cases)
# ============================================================

print("---- STACK TEST ----")

my_stack = Stack(4)
my_stack.print_stack()

print("\nPushing elements...")
my_stack.push(3)
my_stack.push(2)
my_stack.push(1)
my_stack.print_stack()

print("\nPopping element...")
popped = my_stack.pop()
print("Popped:", popped.value if popped else None)

print("\nStack after pop:")
my_stack.print_stack()

print("\nPop until empty:")
my_stack.pop()
my_stack.pop()
my_stack.pop()

print("Pop on empty stack:", my_stack.pop())  # Edge case


# ============================================================
# Queue Implementation (FIFO) using Linked List
# ============================================================

class Queue:
    def __init__(self, value):
        # Create the first node
        new_node = Node(value)

        # First points to front of queue
        self.first = new_node
        
        # Last points to rear of queue
        self.last = new_node
        
        # Length tracks number of elements
        self.length = 1

    def print_queue(self):
        # Start traversal from the front
        temp = self.first

        # Traverse until the end
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        # Create a new node
        new_node = Node(value)

        # If queue is empty
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            # Attach new node at the rear
            self.last.next = new_node
            
            # Move last pointer
            self.last = new_node

        # Increment queue length
        self.length += 1

    def dequeue(self):
        # If queue is empty, nothing to remove
        if self.length == 0:
            return None

        # Store the front node
        temp = self.first

        # If only one element exists
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            # Move front pointer
            self.first = self.first.next
            
            # Disconnect dequeued node
            temp.next = None

        # Decrement queue length
        self.length -= 1

        # Return removed node
        return temp


# ============================================================
# Queue Testing (including edge cases)
# ============================================================

print("\n---- QUEUE TEST ----")

my_queue = Queue(50)
my_queue.print_queue()

print("\nEnqueuing elements...")
my_queue.enqueue(40)
my_queue.enqueue(30)
my_queue.enqueue(20)
my_queue.enqueue(10)
my_queue.print_queue()

print("\nDequeuing elements...")
removed = my_queue.dequeue()
print("Dequeued:", removed.value if removed else None)

removed = my_queue.dequeue()
print("Dequeued:", removed.value if removed else None)

print("\nQueue after dequeue:")
my_queue.print_queue()

print("\nDequeue until empty:")
my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()

print("Dequeue on empty queue:", my_queue.dequeue())  # Edge case
