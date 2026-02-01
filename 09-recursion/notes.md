# 📘 `Function Call Stack & Recursion

## 1. Core Concept

This file demonstrates two closely related concepts:

1. **Function Call Stack**
2. **Recursion**

Both rely on the same underlying runtime mechanism:
the **call stack**, which manages function execution order, local variables, and return addresses.

---

## 2. Call Stack — Fundamental Idea

The **call stack** is a LIFO (Last-In, First-Out) structure used by the runtime to:

* Track active function calls
* Store local variables
* Remember where to return after a function finishes

Each function call:

* Pushes a new stack frame
* Executes
* Pops its frame upon return

---

## 3. Call Stack Invariants

The following rules always hold:

* Only one function executes at a time
* The most recently called function executes first
* A function must complete before its caller resumes
* Stack frames are destroyed after function return

---

## 4. Function Call Chain Example

### Code Segment

```python
funcOne()
```

### Call Flow

```
funcOne
  └── funcTwo
        └── funcThree
```

---

## 5. Step-by-Step Call Stack Execution

### Step 1: `funcOne()` is called

```
Stack:
[ funcOne ]
```

---

### Step 2: `funcOne()` calls `funcTwo()`

```
Stack:
[ funcOne
  funcTwo ]
```

---

### Step 3: `funcTwo()` calls `funcThree()`

```
Stack:
[ funcOne
  funcTwo
  funcThree ]
```

---

### Step 4: `funcThree()` executes

```text
Output: Three
```

* `funcThree()` completes
* Stack frame is popped

```
Stack:
[ funcOne
  funcTwo ]
```

---

### Step 5: `funcTwo()` resumes

```text
Output: Two
```

* `funcTwo()` completes
* Stack frame is popped

```
Stack:
[ funcOne ]
```

---

### Step 6: `funcOne()` resumes

```text
Output: One
```

* `funcOne()` completes
* Stack is empty

---

## 6. Final Output (Call Stack Demo)

```
Three
Two
One
```

---

## 7. Recursion — Core Concept

**Recursion** is a technique where a function calls itself to solve a smaller subproblem.

Every recursive solution must have:

1. **Base Case** — stops recursion
2. **Recursive Case** — reduces problem size

Recursion relies entirely on the call stack.

---

## 8. Factorial — Mathematical Definition

```
factorial(n) = n × factorial(n − 1)
factorial(1) = 1
```

---

## 9. Recursive Algorithm (Factorial)

### Algorithm

1. If `n == 1`, return 1
2. Otherwise:

   * Call `factorial(n - 1)`
   * Multiply result by `n`
3. Return computed value

---

## 10. Factorial Execution Trace (`factorial(4)`)

### Call Expansion (Stack Growth)

```
factorial(4)
→ 4 * factorial(3)
→ 4 * (3 * factorial(2))
→ 4 * (3 * (2 * factorial(1)))
```

---

### Base Case Reached

```
factorial(1) = 1
```

---

### Stack Unwinding (Return Phase)

```
factorial(2) = 2 * 1 = 2
factorial(3) = 3 * 2 = 6
factorial(4) = 4 * 6 = 24
```

---

## 11. Final Output (Recursion Demo)

```
24
```

---

## 12. Edge Cases

### Function Call Stack

Handled:

* Nested function calls
* Implicit returns

---

### Factorial

Handled:

* Positive integers ≥ 1

Not handled (by design):

* `n = 0`
* Negative integers
* Non-integer inputs

---

## 13. Bug Analysis

⚠ **Logical Limitation Identified**

* `factorial(0)` is mathematically valid but not handled
* `factorial(n < 1)` leads to infinite recursion

This is **not a bug**, but an **intentional constraint** based on the provided implementation.

---

## 14. Time & Space Complexity

### Call Stack Example

* Time: **O(n)** (number of function calls)
* Space: **O(n)** (stack depth)

---

### Factorial (Recursive)

| Metric | Complexity        |
| ------ | ----------------- |
| Time   | O(n)              |
| Space  | O(n) (call stack) |

---
