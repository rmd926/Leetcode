# 1441. Build an Array With Stack Operations (Medium)

## Problem Description
You are given an integer array `target` and an integer `n`.

You start with an **empty stack** and have access to a **stream of integers from `1` to `n`** (in increasing order). You can perform the following two operations on the stack:

- **"Push"**: Push the next integer from the stream onto the stack.
- **"Pop"**: Remove the integer at the top of the stack.

You must use these operations to make the elements in the stack (from bottom to top) **exactly equal to `target`**, following these rules:

1. If the stream is not empty, you may read the next integer and **push** it onto the stack.
2. If the stack is not empty, you may **pop** the top element.
3. If at any moment the stack matches `target`, you must **stop all operations** and **stop reading from the stream**.

Return the list of stack operations needed to build `target`.  
If there are multiple valid answers, return **any** of them.

---

## Examples

### Example 1
**Input:** `target = [1,3]`, `n = 3`  
**Output:** `["Push","Push","Pop","Push"]`

**Explanation:**
- Push `1` → stack = `[1]`
- Push `2` → stack = `[1,2]`
- Pop `2`  → stack = `[1]`
- Push `3` → stack = `[1,3]`

---

### Example 2
**Input:** `target = [1,2,3]`, `n = 3`  
**Output:** `["Push","Push","Push"]`

**Explanation:**
- Push `1` → `[1]`
- Push `2` → `[1,2]`
- Push `3` → `[1,2,3]`

---

### Example 3
**Input:** `target = [1,2]`, `n = 4`  
**Output:** `["Push","Push"]`

**Explanation:**
- Push `1` → `[1]`
- Push `2` → `[1,2]`
- The stack now equals `target`, so we stop.
- Reading `3` or `4` is not allowed.

---

## Constraints
- `1 <= target.length <= 100`
- `1 <= n <= 100`
- `1 <= target[i] <= n`
- `target` is strictly increasing
