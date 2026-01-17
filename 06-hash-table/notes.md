# Hash Table — Separate Chaining Implementation

## 1. Core Concept

A **Hash Table** stores key–value pairs by converting keys into array indices
using a hash function, enabling fast insertion and lookup.

This implementation uses:
- Fixed-size array
- Separate chaining for collision handling
- String keys

---

## 2. Data Structure Invariants

- `data_map` is a fixed-length list
- Each index contains either:
  - `None`, or
  - A list of `[key, value]` pairs
- All pairs in a bucket share the same hash index
- No resizing or rehashing is performed

---

## 3. Hash Function

### Purpose
Convert a string key into a valid array index.

### Algorithm
1. Initialize `hash = 0`
2. For each character in the key:
   - Convert character to ASCII
   - Multiply by constant (23)
   - Add to hash
   - Apply modulo with table size
3. Return final hash value

### Properties
- Deterministic
- Bounded by table size
- Simple (not cryptographically secure)

---

## 4. Collision Handling

### Strategy: Separate Chaining

- Each array index stores a list
- Multiple keys can exist at the same index
- Collisions do not overwrite existing data

Example:
```

Index 2 → [['bolts', 1400], ['nuts', 1200]]

```

---

## 5. Operation Breakdown

### Insertion (`set_item`)

1. Compute index using hash function
2. If bucket is empty → initialize list
3. Append `[key, value]` to bucket

---

### Search (`get_item`)

1. Compute index using hash function
2. If bucket exists:
   - Linearly scan bucket
3. If key found → return value
4. Else → return `None`

---

### Retrieve All Keys (`keys`)

1. Initialize empty list
2. Traverse entire array
3. Extract keys from each bucket
4. Return collected keys

---

## 6. Logical Flow (Mental Model)

```

Key
↓
Hash Function
↓
Array Index
↓
Bucket (List)
↓
Linear Scan

```

---

## 7. Edge Cases

Handled:
- Key not present
- Multiple collisions
- Empty table

Not handled:
- Duplicate key overwrite
- Dynamic resizing
- Non-string keys

---

## 8. Bug Analysis

✔ No logical or implementation bugs found  
⚠ Duplicate keys are allowed by design

---

## 9. Time & Space Complexity

| Operation | Avg Time | Worst Time | Space |
|---------|----------|------------|-------|
| Insert  | O(1)     | O(n)       | O(n)  |
| Search  | O(1)     | O(n)       | O(1)  |
| Keys    | O(n)     | O(n)       | O(n)  |

`n` = number of key-value pairs

---

## 10. Interview Takeaways

- Collision handling: Separate Chaining
- Hashing: Polynomial rolling hash
- No load-factor optimization
- Educational and interview-friendly implementation
