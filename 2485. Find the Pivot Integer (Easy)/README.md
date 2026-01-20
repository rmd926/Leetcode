# 2485. Find the Pivot Integer (Easy)

## Problem Description
Given a positive integer `n`, find an integer `x` such that the **sum of all integers from `1` to `x` (inclusive)** is equal to the **sum of all integers from `x` to `n` (inclusive)**.

Return the pivot integer `x`.  
If no such integer exists, return `-1`.

It is guaranteed that there will be **at most one pivot integer** for the given input.

---

## Examples

### Example 1
**Input:** `n = 8`  
**Output:** `6`  

**Explanation:**  
`
1 + 2 + 3 + 4 + 5 + 6 = 21
6 + 7 + 8 = 21
`
So, `6` is the pivot integer.

---

### Example 2
**Input:** `n = 1`  
**Output:** `1`  

**Explanation:**  

`1 = 1`

Thus, `1` is the pivot integer.

---

### Example 3
**Input:** `n = 4`  
**Output:** `-1`  

**Explanation:**  
There is no integer `x` such that the sums on both sides are equal.

---

## Constraints
- `1 <= n <= 1000`
```
