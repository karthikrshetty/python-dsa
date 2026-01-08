# 📘 Stack and Queue Implementation (Using Linked List) — Detailed Notes

---

## 1. Shared Building Block: `Node`

```python
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
```

### Purpose

* Represents a single element in both **Stack** and **Queue**
* Forms the linked structure

### Fields

| Field   | Description          |
| ------- | -------------------- |
| `value` | Stores data          |
| `next`  | Pointer to next node |

---

# 🧱 STACK (LIFO — Last In, First Out)

---

## 2. Stack Overview

* Stack follows **LIFO**
* Operations happen only at the **top**
* Implemented using a **singly linked list**

```
TOP → [1] → [2] → [3] → None
```

---

## 3. Stack Initialization

```python
class Stack:
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
```

### Initialization Logic

1. Create a new node
2. Assign it to `top`
3. Set height to `1`

### Invariants

* `top` always points to the most recent element
* `height` reflects number of elements

---

## 4. Print Stack

```python
def print_stack(self):
```

### Algorithm

1. Start from `top`
2. Traverse using `next`
3. Print each value

### Traversal Direction

* From **top → bottom**

### Time Complexity

* **O(n)**

---

## 5. Push — Add Element to Stack

```python
def push(self,value):
```

### Core Idea

* Always insert at the **top**

### Algorithm

1. Create new node
2. If stack is empty:

   * `top = new_node`
3. Else:

   * `new_node.next = top`
   * `top = new_node`
4. Increment height

### Visualization

```
Before: TOP → 2 → 3
After : TOP → 1 → 2 → 3
```

### Time Complexity

* **O(1)**

---

## 6. Pop — Remove Element from Stack

```python
def pop(self):
```

### Core Idea

* Remove and return the **top element**

### Algorithm

1. If stack is empty → return `None`
2. Store `top` in `temp`
3. Move `top` to `top.next`
4. Disconnect `temp.next`
5. Decrement height
6. Return removed node

### Visualization

```
TOP → 1 → 2 → 3
Pop → removes 1
TOP → 2 → 3
```

### Time Complexity

* **O(1)**

---

## 7. Stack Execution Flow (Example)

```text
Initial:        [4]
Push 3:         [3,4]
Push 2:         [2,3,4]
Push 1:         [1,2,3,4]
Pop:            [2,3,4]
```

---

## 8. Stack Edge Cases Handled

* Pop on empty stack → `None`
* Push on empty stack
* Single element pop resets stack correctly

---

# 🚶 QUEUE (FIFO — First In, First Out)

---

## 9. Queue Overview

* Queue follows **FIFO**
* Insert at **rear (last)**
* Remove from **front (first)**

```
FIRST → [50] → [40] → [30] → None ← LAST
```

---

## 10. Queue Initialization

```python
class Queue:
    def __init__(self,value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
```

### Initialization Logic

1. Create new node
2. Assign to both `first` and `last`
3. Set length to `1`

### Invariants

* `first` points to front element
* `last` points to rear element

---

## 11. Print Queue

```python
def print_queue(self):
```

### Algorithm

1. Start from `first`
2. Traverse forward
3. Print each value

### Time Complexity

* **O(n)**

---

## 12. Enqueue — Add Element to Queue

```python
def enqueue(self,value):
```

### Core Idea

* Always insert at the **rear**

### Algorithm

1. Create new node
2. If queue empty:

   * `first = last = new_node`
3. Else:

   * `last.next = new_node`
   * `last = new_node`
4. Increment length

### Visualization

```
Before: 50 → 40
After : 50 → 40 → 30
```

### Time Complexity

* **O(1)**

---

## 13. Dequeue — Remove Element from Queue

```python
def dequeue(self):
```

### Core Idea

* Remove from **front**

### Algorithm

1. If queue empty → return `None`
2. Store `first` in `temp`
3. If only one element:

   * `first = last = None`
4. Else:

   * `first = first.next`
   * Disconnect `temp.next`
5. Decrement length
6. Return removed node

### Visualization

```
50 → 40 → 30
Dequeue → removes 50
40 → 30
```

### Time Complexity

* **O(1)**

---

## 14. Queue Execution Flow (Example)

```text
Initial:        [50]
Enqueue:        [50,40,30,20,10]
Dequeue x2:     [30,20,10]
```

---

## 15. Queue Edge Cases Handled

* Dequeue on empty queue → `None`
* Single element dequeue resets queue
* Enqueue on empty queue works correctly

---

## 16. Complexity Summary

### Stack

| Operation | Time |
| --------- | ---- |
| Push      | O(1) |
| Pop       | O(1) |
| Print     | O(n) |

### Queue

| Operation | Time |
| --------- | ---- |
| Enqueue   | O(1) |
| Dequeue   | O(1) |
| Print     | O(n) |

---

## 17. Key Takeaways

* Stack and Queue are **restricted linked lists**
* Linked list implementation avoids shifting (unlike arrays)
* All core operations run in **constant time**
* Proper pointer updates prevent memory leaks

---