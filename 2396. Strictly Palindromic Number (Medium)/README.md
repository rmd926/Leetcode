# 2396. Strictly Palindromic Number (Medium)

## Problem Description
An integer `n` is **strictly palindromic** if, for **every base** `b` in the range **2 to `n - 2` (inclusive)**, the string representation of `n` in base `b` is **palindromic**.

You are given an integer `n`. Return `true` if `n` is strictly palindromic, and `false` otherwise.

A string is **palindromic** if it reads the same forward and backward.

---

## Examples

### Example 1
**Input:** `n = 9`  
**Output:** `false`

**Explanation:**
- In base 2: `9 = 1001` (palindromic)
- In base 3: `9 = 100` (not palindromic)

Since `n` is not palindromic in **every** base from 2 to `n - 2`, return `false`.  
(Note: In bases 4, 5, 6, and 7, `9` is also not palindromic.)

### Example 2
**Input:** `n = 4`  
**Output:** `false`

**Explanation:**
Only base 2 is considered because bases range from 2 to `n - 2 = 2`.
- In base 2: `4 = 100` (not palindromic)

Therefore, return `false`.

---

## Constraints
- `4 <= n <= 10^5`
