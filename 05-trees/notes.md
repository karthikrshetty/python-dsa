# Binary Search Tree (BST) – Detailed Notes

## 1. Concept Overview

A **Binary Search Tree (BST)** is a binary tree with the following properties:

* Each node stores **one value**
* Left subtree contains values **less than** the node
* Right subtree contains values **greater than** the node
* No duplicate values allowed

This structure allows **efficient searching and insertion**.

---

## 2. Node Structure

### Node Fields

* `value` → data stored in the node
* `left` → reference to left child
* `right` → reference to right child

### Representation

```
      value
     /     \
  left     right
```

---

## 3. BinarySearchTree Structure

### Tree Fields

* `root` → reference to the root node of the tree

### Initial State

```
root = None
```

---

## 4. Insert Operation

### Goal

Insert a new value into the BST while maintaining BST properties.

---

### Algorithm (Step-by-Step)

1. Create a new node with the given value
2. If the tree is empty:

   * Set `root = new_node`
   * Return `True`
3. Start from the root:

   * If the value already exists → return `False`
   * If value < current node → move to left subtree
   * If value > current node → move to right subtree
4. Insert the node when a `None` position is found
5. Return `True` after insertion

---

### Logical Flow

```
Start at root
│
├─ value == current → reject (duplicate)
│
├─ value < current → go left
│
└─ value > current → go right
```

---

### Time Complexity

* **Average Case**: O(log n)
* **Worst Case** (skewed tree): O(n)

---

## 5. Contains (Search) Operation

### Goal

Check whether a given value exists in the BST.

---

### Algorithm (Step-by-Step)

1. Start from the root
2. Compare target value with current node:

   * If smaller → move left
   * If larger → move right
   * If equal → return `True`
3. If traversal reaches `None`:

   * Value does not exist
   * Return `False`

---

### Logical Flow

```
Start at root
│
├─ value < current → left
├─ value > current → right
└─ value == current → found
```

---

### Time Complexity

* **Average Case**: O(log n)
* **Worst Case**: O(n)

---

## 6. Example Tree Construction

### Insert Order

```
2, 1, 3, 4, 7, 6, 5, 10, 8
```

### Final Tree Shape

```
        2
       / \
      1   3
           \
            4
             \
              7
             / \
            6   10
           /     /
          5     8
```

---

## 7. Search Examples

| Value | Result |
| ----- | ------ |
| 10    | True   |
| 9     | False  |

---

## 8. Key Invariants (Must Always Hold)

* Left child values < parent
* Right child values > parent
* No duplicate values
* Tree is built using **comparison-based traversal**

---

## 9. Common Pitfalls (Avoided)

* ❌ Comparing nodes instead of values
* ❌ Allowing duplicate insertions
* ❌ Forgetting to move traversal pointer
* ❌ Breaking BST ordering rules

---

## 10. Summary

* BST enables **efficient ordered storage**
* Insert and search are both **logarithmic on average**
* Performance depends heavily on **tree balance**
* This implementation uses **iterative traversal** (space-efficient)

---
