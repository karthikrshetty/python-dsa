# 📘 Singly Linked List — Complete Implementation Notes (Python)

## 1. Concept Overview

A **Singly Linked List** is a linear data structure composed of **nodes**, where each node contains:

* **Data (value)**
* **Reference (pointer) to the next node**

Traversal is strictly **forward**.

```
HEAD → Node → Node → Node → None
                      ↑
                     TAIL
```

---

## 2. Node Structure

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
```

### Purpose

Represents an individual element in the linked list.

### Fields

| Field   | Description                              |
| ------- | ---------------------------------------- |
| `value` | Stores data                              |
| `next`  | Reference to next node (None by default) |

---

## 3. LinkedList Initialization

```python
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
```

### Initialization Flow

1. Create a new node
2. Assign it as both `head` and `tail`
3. Set initial length to 1

### Invariant

* `head` always points to first node
* `tail` always points to last node

---

## 4. Append — Insert at End

```python
def append(self, value):
```

### Algorithm

1. Create a new node
2. If list is empty:

   * Set `head` and `tail` to new node
3. Else:

   * `tail.next` → new node
   * Move `tail` → new node
4. Increment length

### Time Complexity

* **O(1)**

---

## 5. Print List

```python
def print_list(self):
```

### Algorithm

1. Start traversal from `head`
2. While node is not `None`:

   * Print value
   * Move to `next`

### Time Complexity

* **O(n)**

---

## 6. Pop — Remove Last Node

```python
def pop(self):
```

### Key Challenge

Singly linked lists do **not** have backward traversal.

### Algorithm

1. If list is empty → return `None`
2. Use two pointers:

   * `temp` → traverses list
   * `pre` → tracks previous node
3. Stop when `temp` reaches last node
4. Update:

   * `tail = pre`
   * `tail.next = None`
5. Decrement length
6. If list becomes empty:

   * `head = tail = None`

### Time Complexity

* **O(n)**

---

## 7. Prepend — Insert at Beginning

```python
def prepend(self, value):
```

### Algorithm

1. Create a new node
2. If list is empty:

   * `head = tail = new_node`
3. Else:

   * `new_node.next = head`
   * `head = new_node`
4. Increment length

### Time Complexity

* **O(1)**

---

## 8. Pop First — Remove Head Node

```python
def pop_first(self):
```

### Algorithm

1. If list is empty → return `None`
2. Store current head
3. Move `head` → `head.next`
4. Disconnect old head
5. Decrement length
6. If list becomes empty:

   * `tail = None`

### Time Complexity

* **O(1)**

---

## 9. Get — Access Node by Index

```python
def get(self, index):
```

### Algorithm

1. Validate index
2. Start from head
3. Move `index` steps forward
4. Return node

### Time Complexity

* **O(n)**

---

## 10. Set Value — Update Node Data

```python
def set_value(self, index, value):
```

### Algorithm

1. Retrieve node using `get(index)`
2. If node exists:

   * Update `value`
3. Return success status

### Time Complexity

* **O(n)**

---

## 11. Insert — Add Node at Index

```python
def insert(self, index, value):
```

### Index Handling

| Case              | Action           |
| ----------------- | ---------------- |
| `index == 0`      | Prepend          |
| `index == length` | Append           |
| Otherwise         | Insert in middle |

### Middle Insertion Algorithm

1. Get node at `index - 1`
2. Point `new_node.next` to `prev.next`
3. Point `prev.next` to `new_node`
4. Increment length

### Time Complexity

* **O(n)**

---

## 12. Remove — Delete Node at Index

```python
def remove(self, index):
```

### Index Handling

| Case                  | Action             |
| --------------------- | ------------------ |
| `index == 0`          | Pop First          |
| `index == length - 1` | Pop                |
| Otherwise             | Remove from middle |

### Middle Removal Algorithm

1. Get previous node
2. Store node to be removed
3. Redirect pointers
4. Disconnect removed node
5. Decrement length

### Time Complexity

* **O(n)**

---

## 13. Reverse — Reverse the Linked List

```python
def reverse(self):
```

### Core Idea

Reverse pointer direction **in-place**.

### Algorithm

1. Swap `head` and `tail`
2. Initialize:

   * `before = None`
   * `temp = old_head`
3. Iterate:

   * `after = temp.next`
   * `temp.next = before`
   * `before = temp`
   * `temp = after`

### Complexity

* **Time:** O(n)
* **Space:** O(1)

---

## 14. Example Execution Flow

```text
Initial:        [1]
Append:         [1,2,3]
Prepend:        [0,1,2,3]
Pop:            [0,1,2]
Insert(2, 8):   [0,1,8,2]
Remove(1):      [0,8,2]
Reverse:        [2,8,0]
```

---

## 15. Complexity Summary

| Operation | Time |
| --------- | ---- |
| Append    | O(1) |
| Prepend   | O(1) |
| Pop       | O(n) |
| Pop First | O(1) |
| Get       | O(n) |
| Insert    | O(n) |
| Remove    | O(n) |
| Reverse   | O(n) |

---

## 16. Key Invariants

* `head` always points to first node
* `tail.next` is always `None`
* `length` accurately reflects number of nodes

---
