# 📘 Doubly Linked List — Complete Implementation Notes (Python)

---

## 1. Concept Overview

A **Doubly Linked List (DLL)** is a linear data structure where each node contains:

* A **value**
* A pointer to the **next node**
* A pointer to the **previous node**

This allows **bidirectional traversal** (forward and backward).

```
None ← [prev | value | next] ⇄ [prev | value | next] ⇄ [prev | value | next] → None
        ↑                                                ↑
       HEAD                                             TAIL
```

---

## 2. Node Structure

```python
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
```

### Fields

| Field   | Description              |
| ------- | ------------------------ |
| `value` | Stores data              |
| `next`  | Pointer to next node     |
| `prev`  | Pointer to previous node |

---

## 3. DoublyLinkedList Initialization

```python
class DoublyLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
```

### Initialization Logic

1. Create a new node
2. Assign it as both `head` and `tail`
3. Set `length = 1`

### Invariant

* `head.prev = None`
* `tail.next = None`

---

## 4. Print List

```python
def print_list(self):
```

### Algorithm

1. Start from `head`
2. Traverse using `next`
3. Print each node’s value

### Time Complexity

* **O(n)**

---

## 5. Append — Insert at End

```python
def append(self,value):
```

### Algorithm

1. Create a new node
2. If list is empty:

   * `head = tail = new_node`
3. Else:

   * `tail.next = new_node`
   * `new_node.prev = tail`
   * `tail = new_node`
4. Increment length

### Pointer Changes

```
Old Tail ⇄ New Node
```

### Time Complexity

* **O(1)**

---

## 6. Pop — Remove Last Node

```python
def pop(self):
```

### Algorithm

1. If list empty → return `None`
2. Store current tail in `temp`
3. If only one node:

   * `head = tail = None`
4. Else:

   * Move `tail` to `tail.prev`
   * `tail.next = None`
   * `temp.prev = None`
5. Decrement length
6. Return removed node

### Advantage over Singly LL

* No traversal required due to `prev` pointer

### Time Complexity

* **O(1)**

---

## 7. Prepend — Insert at Beginning

```python
def prepend(self,value):
```

### Algorithm

1. Create new node
2. If list empty:

   * `head = tail = new_node`
3. Else:

   * `new_node.next = head`
   * `head.prev = new_node`
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

1. If empty → return `None`
2. Store head in `temp`
3. If one node:

   * `head = tail = None`
4. Else:

   * `head = head.next`
   * `head.prev = None`
   * `temp.next = None`
5. Decrement length
6. Return removed node

### Time Complexity

* **O(1)**

---

## 9. Get — Access Node by Index (Optimized)

```python
def get(self,index):
```

### Optimization Strategy

* If index in **first half** → traverse from `head`
* If index in **second half** → traverse from `tail`

### Algorithm

1. Validate index
2. Decide traversal direction
3. Move pointer accordingly
4. Return node

### Time Complexity

* **O(n)** (worst case)
* **O(n/2)** average

---

## 10. Set Value — Update Node Data

```python
def set_value(self,index,value):
```

### Algorithm

1. Retrieve node using `get(index)`
2. If node exists:

   * Update value
3. Return status

### Time Complexity

* **O(n)**

---

## 11. Insert — Add Node at Index

```python
def insert(self,index,value):
```

### ⚠️ Important Notes (Code-Accurate)

```python
if index<0 or index>=self.length:
    return False
```

* This implementation **does not allow insertion at index = length**
* Append must be called explicitly

### Algorithm (Middle Insertion)

1. Create new node
2. Get node at `index-1` → `before`
3. `after = before.next`
4. Rewire pointers:

   * `new_node.prev = before`
   * `new_node.next = after`
   * `before.next = new_node`
   * `after.prev = new_node`
5. Increment length

### Time Complexity

* **O(n)**

---

## 12. Remove — Delete Node at Index

```python
def remove(self,index):
```

### Cases

| Index      | Action           |
| ---------- | ---------------- |
| `0`        | `pop_first()`    |
| `length-1` | `pop()`          |
| Middle     | Pointer rewiring |

### Middle Removal Algorithm

1. Retrieve node at index
2. Connect neighbors:

   * `temp.prev.next = temp.next`
   * `temp.next.prev = temp.prev`
3. Disconnect `temp`
4. Decrement length
5. Return removed node

### Time Complexity

* **O(n)**

---

## 13. Example Execution Flow

```text
Initial:        [1]
Append:         [1,2,3]
Pop:            [1,2]
Prepend:        [0,1,2]
Pop First:      [1,2]
Set Value:      [10,2]
Insert(1,20):   [10,20,2]
Remove(1):      [10,2]
```

---

## 14. Complexity Summary

| Operation | Time |
| --------- | ---- |
| Append    | O(1) |
| Pop       | O(1) |
| Prepend   | O(1) |
| Pop First | O(1) |
| Get       | O(n) |
| Set       | O(n) |
| Insert    | O(n) |
| Remove    | O(n) |

---

## 15. Key Invariants

* `head.prev == None`
* `tail.next == None`
* Each node maintains valid `next` and `prev` links
* `length` reflects total nodes accurately

---

## 16. Advantages over Singly Linked List

* Bidirectional traversal
* Constant-time deletion at tail
* Optimized indexed access

---
