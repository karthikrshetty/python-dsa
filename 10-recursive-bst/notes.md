# Binary Search Tree (Recursive Implementation)

## 1. Core Concept

A **Binary Search Tree (BST)** is a binary tree with an ordering constraint:

* Left subtree → values **less than** node
* Right subtree → values **greater than** node

This enables efficient:

* Search
* Insert
* Delete operations

---

## 2. Data Structure Invariants

* Each node has at most two children
* BST ordering property:

  ```
  left < node < right
  ```
* No duplicate values (implicitly enforced)
* Recursive structure maintained at all levels
* Root reference always points to tree entry

---

## 3. Internal Representation

```
        47
       /  \
     21    76
    / \   / \
   18 27 52 82
```

* Tree is composed of linked `Node` objects
* Each node holds references to left and right children

---

## 4. Operation Breakdown

### Insertion (`r_insert`)

#### Algorithm

1. Start at root
2. Traverse:

   * Left if smaller
   * Right if larger
3. Insert at first `None` position

#### Strategy

**Recursive descent + backtracking**

---

### Search (`r_contains`)

#### Algorithm

1. Compare with current node
2. Traverse left/right accordingly
3. Stop when found or `None`

---

### Minimum Value (`min_value`)

#### Algorithm

* Traverse left until no further left child
* Return node value

---

### Deletion (`delete_node`)

#### Cases

##### Case 1: Leaf Node

```
Simply remove node
```

##### Case 2: One Child

```
Replace node with its child
```

##### Case 3: Two Children

```
1. Find inorder successor (min in right subtree)
2. Replace node value
3. Delete successor
```

---

## 5. Logical Flow (Mental Model)

```
Insert/Search:
Root → Compare → Go Left/Right → Repeat

Delete:
Locate Node → Apply Case → Rebalance via recursion
```

---

## 6. Example Usage / Test Driver — Execution Trace

### Step 1: Tree Construction

Inserted:

```
47, 21, 76, 18, 27, 52, 82
```

Tree:

```
        47
       /  \
     21    76
    / \   / \
   18 27 52 82
```

---

### Step 2: Search

```
r_contains(27) → True
r_contains(17) → False
```

Validates:

* Successful search
* Failed search path

---

### Step 3: Delete Root (47)

Case:

* Node has **two children**

Process:

1. Find successor → `52`
2. Replace `47 → 52`
3. Delete original `52`

---

### Step 4: Final Tree

```
        52
       /  \
     21    76
    / \     \
   18 27     82
```

---

## 7. Edge Cases

### Handled

* Empty tree insertion
* Search miss
* Deleting leaf node
* Deleting node with one child
* Deleting node with two children
* Deleting root node

### Not Handled

* Duplicate values
* Balancing (unbalanced BST possible)

---

## 8. Bug Analysis

❗ **Critical Bug Identified and Fixed**

### Issue

```python
self.__delete_node(self.root, value)
```

* Return value ignored
* Root not updated when deleted

### Fix

```python
self.root = self.__delete_node(self.root, value)
```

### Impact

* Without fix → incorrect tree after root deletion
* With fix → tree remains valid

---

## 9. Time & Space Complexity

| Operation | Avg      | Worst | Space |
| --------- | -------- | ----- | ----- |
| Insert    | O(log n) | O(n)  | O(n)  |
| Search    | O(log n) | O(n)  | O(n)  |
| Delete    | O(log n) | O(n)  | O(n)  |

---

