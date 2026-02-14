# 1015. Smallest Integer Divisible by K (Medium)

## Problem Description
Given a positive integer `k`, find the length of the smallest positive integer `n` such that:

- `n` is divisible by `k`
- `n` contains only the digit `'1'` (for example: `1`, `11`, `111`, `1111`, ...)

Return the **length** of `n`. If no such integer exists, return `-1`.

**Note:** The value of `n` may be too large to fit in a 64-bit signed integer.

---

## Examples

### Example 1
**Input:** `k = 1`  
**Output:** `1`  

**Explanation:**  
The smallest valid number is `n = 1`, which has length `1`.

### Example 2
**Input:** `k = 2`  
**Output:** `-1`

**Explanation:**  
No number made only of digit `1` can be divisible by `2`.

### Example 3
**Input:** `k = 3`  
**Output:** `3`

**Explanation:**  
The smallest valid number is `n = 111`, which has length `3`.

---

## Constraints
- `1 <= k <= 10^5`
