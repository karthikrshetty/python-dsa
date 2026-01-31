# 📘 Max Heap Implementation

## 1. Core Concept

A **Max Heap** is a **complete binary tree** where:

* The value at each parent node is **greater than or equal to** the values of its children.
* The **maximum element** is always stored at the root.
* The tree is stored efficiently using an **array**.

This implementation uses:

* Array-based binary heap
* Zero-based indexing
* Explicit bubble-up and sink-down operations

---

## 2. Data Structure Invariants

The following conditions must **always remain true**:

* The heap is a **complete binary tree**
* Heap property:

  ```
  heap[parent] ≥ heap[left_child]
  heap[parent] ≥ heap[right_child]
  ```
* Parent/child index relationships:

  ```
  parent(i)     = (i - 1) // 2
  left_child(i) = 2i + 1
  right_child(i)= 2i + 2
  ```
* Maximum value is always at index `0`

---

## 3. Internal Representation

```
Index:  0   1   2   3   4
Heap : [99, 72, 61, 58, ...]
```

* Tree is **implicit**
* No node objects are used
* Children are derived mathematically

---

## 4. Helper Methods

### `_parent(index)`

Returns index of parent node.

### `_left_child(index)`

Returns index of left child.

### `_right_child(index)`

Returns index of right child.

### `_swap(i, j)`

Exchanges values at two indices to restore heap property.

---

## 5. Operation Breakdown

### Insertion (`insert`)

#### Algorithm

1. Append value to end of heap
2. Compare with parent
3. Swap if value is larger
4. Repeat until heap property is restored

#### Heap Restoration Strategy

**Bubble Up (Percolate Up)**

---

### Removal (`remove`)

#### Algorithm

1. If heap empty → return `None`
2. If one element → pop and return
3. Store root value
4. Move last element to root
5. Sink root down to correct position
6. Return stored max value

#### Heap Restoration Strategy

**Sink Down (Heapify Down)**

---

### Sink Down (`_sink_down`)

#### Algorithm

1. Compare node with left and right children
2. Select the larger child
3. Swap if child is larger
4. Repeat until no violation remains

---

## 6. Logical Flow (Mental Model)

```
Insert:
Value → End of Array → Bubble Up → Heap Restored

Remove:
Root → Replace with Last → Sink Down → Heap Restored
```

---

## 7. Example Usage / Test Driver — Execution Trace

### Initial Insertions

```python
insert(99)
insert(72)
insert(61)
insert(58)
```

Heap:

```
[99, 72, 61, 58]
```

Validates:

* Bubble-up behavior
* Parent dominance

---

### Insert 100

```python
insert(100)
```

Intermediate:

```
[99, 72, 61, 58, 100]
```

After bubble-up:

```
[100, 99, 61, 58, 72]
```

Validates:

* Multiple swaps
* Root replacement

---

### Insert 75

```python
insert(75)
```

Final:

```
[100, 99, 75, 58, 72, 61]
```

Validates:

* Partial bubbling
* Correct subtree ordering

---

### First Remove

```python
remove()
```

Returned:

```
100
```

Heap:

```
[99, 72, 75, 58, 61]
```

Validates:

* Sink-down logic
* Larger-child selection

---

### Second Remove

```python
remove()
```

Returned:

```
99
```

Heap:

```
[75, 72, 61, 58]
```

Validates:

* Heap stability after repeated removals

---

## 8. Edge Cases

Handled:

* Empty heap removal
* Single-element heap removal
* Deep bubble-up
* Deep sink-down

Not handled (by design):

* Heap construction from array (heapify)
* Decrease/increase key
* Duplicate value constraints

---

## 9. Bug Analysis

✔ No logical or implementation bugs found

Design choices:

* Duplicate values allowed
* No size limit
* No comparator abstraction

---

## 10. Time & Space Complexity

| Operation | Time     | Space |
| --------- | -------- | ----- |
| Insert    | O(log n) | O(1)  |
| Remove    | O(log n) | O(1)  |
| Peek      | O(1)     | O(1)  |

Where `n` = number of elements in heap.

---
