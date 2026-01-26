# Graph — Undirected Adjacency List Implementation

## 1. Core Concept

A **Graph** is a non-linear data structure consisting of:

* **Vertices (nodes)**
* **Edges (connections between vertices)**

This implementation represents an **undirected, unweighted graph** using an **adjacency list**, where each vertex stores a list of its neighboring vertices.

Key characteristics of this implementation:

* Undirected edges
* No edge weights
* No self-imposed constraints on duplicate edges
* Dictionary-based adjacency list

---

## 2. Data Structure Invariants

The following invariants must **always** hold true:

* `adj_list` is a dictionary
* Each key in `adj_list` represents a unique vertex
* Each value is a list of adjacent vertices
* For every edge `(u, v)`:

  * `v` exists in `adj_list[u]`
  * `u` exists in `adj_list[v]`
* No adjacency list contains a vertex that is not present as a key
* Removing a vertex removes **all incident edges**

Violation of any invariant results in a logically inconsistent graph.

---

## 3. Internal Representation

```
adj_list = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
}
```

* Keys → vertices
* Values → neighbors
* Each edge stored **twice** (undirected symmetry)

---

## 4. Graph Operations Overview

### Supported Operations

* Add Vertex
* Add Edge
* Remove Edge
* Remove Vertex
* Print Graph

### Unsupported / Intentionally Omitted

* Edge weights
* Duplicate edge prevention
* Graph traversal (BFS / DFS)
* Directed edges
* Cycle detection

---

## 5. Operation Breakdown

### Add Vertex (`add_vertex`)

#### Purpose

Insert a new vertex into the graph.

#### Algorithm

1. Check if vertex already exists in `adj_list`
2. If not present:

   * Create key with empty list as value
3. Return insertion status

#### Guarantees

* Vertices are unique
* No side effects on existing vertices

---

### Add Edge (`add_edge`)

#### Purpose

Create an undirected connection between two vertices.

#### Algorithm

1. Verify both vertices exist
2. Append `v2` to `v1`’s adjacency list
3. Append `v1` to `v2`’s adjacency list
4. Return success status

#### Important Behavior

* Duplicate edges are allowed
* Self-loops are allowed
* No validation against parallel edges

---

### Remove Edge (`remove_edge`)

#### Purpose

Remove an undirected edge between two vertices.

#### Algorithm

1. Verify both vertices exist
2. Attempt to remove:

   * `v2` from `v1`’s adjacency list
   * `v1` from `v2`’s adjacency list
3. Ignore operation if edge does not exist

#### Error Handling

* Uses `try / except` to suppress `ValueError`
* Graph remains unchanged on failure

---

### Remove Vertex (`remove_vertex`)

#### Purpose

Remove a vertex and all its associated edges.

#### Algorithm

1. Verify vertex exists
2. Iterate over its adjacency list
3. Remove vertex reference from each neighbor
4. Delete vertex entry from `adj_list`

#### Key Property

* Cascading edge cleanup ensures no dangling references

---

### Print Graph (`print_graph`)

#### Purpose

Visualize the current state of the adjacency list.

#### Algorithm

1. Iterate over all vertices
2. Print vertex and its neighbors

#### Notes

* Read-only operation
* Output order depends on dictionary iteration

---

## 6. Logical Flow (Mental Model)

```
Vertex
↓
Dictionary Key
↓
Adjacency List
↓
Neighbor Lookup
↓
Symmetric Edge Maintenance
```

For every mutation:

* Update both endpoints
* Preserve undirected symmetry
* Maintain adjacency list integrity

---

## 7. Example Usage / Test Driver — Execution Semantics

### Step 1: Graph Initialization

```
{}
```

* Empty graph
* No vertices
* No edges

---

### Step 2: Vertex Insertion

```
A, B, C, D
```

State:

```
A → []
B → []
C → []
D → []
```

Validates:

* Multiple vertex insertion
* Empty adjacency lists

---

### Step 3: Edge Insertion

Edges added:

```
A-B, A-C, A-D, B-D, C-D
```

State:

```
A → [B, C, D]
B → [A, D]
C → [A, D]
D → [A, B, C]
```

Validates:

* Undirected symmetry
* High-degree vertex handling
* Multiple neighbors per vertex

---

### Step 4: Vertex Removal (`D`)

State after removal:

```
A → [B, C]
B → [A]
C → [A]
```

Validates:

* Cascading edge removal
* Referential integrity
* Graph consistency after mutation

---

## 8. Edge Cases

### Handled

* Empty graph
* Isolated vertices
* High-degree vertices
* Removing non-existent edges
* Removing vertices with multiple edges

### Not Handled (By Design)

* Duplicate edge prevention
* Edge weight management
* Directed edges
* Graph traversal algorithms

---

## 9. Bug Analysis

✔ No logical or implementation bugs found

Design choices (intentional):

* Duplicate edges allowed
* Self-loops allowed
* No adjacency deduplication

---

## 10. Time & Space Complexity

| Operation     | Time Complexity | Space Impact |
| ------------- | --------------- | ------------ |
| Add Vertex    | O(1)            | O(1)         |
| Add Edge      | O(1)            | O(1)         |
| Remove Edge   | O(deg(v))       | O(1)         |
| Remove Vertex | O(deg(v))       | O(1)         |
| Print Graph   | O(V + E)        | O(1)         |

Where:

* `V` = number of vertices
* `E` = number of edges

---

## 11. Interview Takeaways

* Graph Representation: Adjacency List
* Edge Type: Undirected
* Collision Analogy: Shared neighbors
* Invariant Maintenance is critical
* Vertex removal is the most error-prone operation
* This implementation is **educational, interview-friendly**, and mutation-safe

---
