class MaxHeap:
    """
    Max Heap implementation using a list (array-based binary heap).

    Heap Property:
    - Every parent node is greater than or equal to its children.
    """

    def __init__(self):
        """
        Initialize an empty heap.
        """
        self.heap = []

    def _left_child(self, index):
        """
        Calculate the index of the left child.

        Formula:
        left_child = 2 * index + 1
        """
        return 2 * index + 1

    def _right_child(self, index):
        """
        Calculate the index of the right child.

        Formula:
        right_child = 2 * index + 2
        """
        return 2 * index + 2

    def _parent(self, index):
        """
        Calculate the index of the parent node.

        Formula:
        parent = (index - 1) // 2
        """
        return (index - 1) // 2

    def _swap(self, index1, index2):
        """
        Swap two elements in the heap by index.
        """
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        """
        Insert a value into the heap.

        Logic:
        1. Append value at the end of the array.
        2. Bubble the value up until heap property is restored.
        """

        # Step 1: Insert value at the end
        self.heap.append(value)

        # Step 2: Track the index of the newly inserted value
        current = len(self.heap) - 1

        # Step 3: Bubble up while heap property is violated
        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def remove(self):
        """
        Remove and return the maximum value (root) from the heap.

        Logic:
        1. Handle empty heap.
        2. Handle single-element heap.
        3. Replace root with last element.
        4. Sink down to restore heap property.
        """

        # Case 1: Empty heap
        if len(self.heap) == 0:
            return None

        # Case 2: Single element heap
        if len(self.heap) == 1:
            return self.heap.pop()

        # Case 3: Multiple elements
        max_value = self.heap[0]

        # Move last element to root
        self.heap[0] = self.heap.pop()

        # Restore heap property
        self._sink_down(0)

        return max_value

    def _sink_down(self, index):
        """
        Restore heap property by sinking the value at index downward.

        Logic:
        1. Compare node with left and right children.
        2. Swap with the larger child if violation occurs.
        3. Repeat until heap property is restored.
        """

        max_index = index

        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            # Compare with left child
            if left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]:
                max_index = left_index

            # Compare with right child
            if right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]:
                max_index = right_index

            # If a swap is needed, perform it
            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                # Heap property is satisfied
                return


# ======================================================
# Example Usage / Test Driver
# ======================================================

myheap = MaxHeap()

myheap.insert(99)
myheap.insert(72)
myheap.insert(61)
myheap.insert(58)

print(myheap.heap)

myheap.insert(100)
print(myheap.heap)

myheap.insert(75)
print(myheap.heap)

myheap.remove()
print(myheap.heap)

myheap.remove()
print(myheap.heap)
