# 2798. Number of Employees Who Met the Target (Easy)

## Problem Description
There are `n` employees in a company, numbered from `0` to `n - 1`.  
Employee `i` has worked `hours[i]` hours.

The company requires each employee to work **at least** `target` hours.

You are given:
- a **0-indexed** array `hours` of length `n` containing non-negative integers
- a non-negative integer `target`

Return the number of employees who worked **at least** `target` hours.

---

## Examples

### Example 1
**Input:** `hours = [0, 1, 2, 3, 4]`, `target = 2`  
**Output:** `3`

**Explanation:**
- Employee 0: 0 hours (does not meet the target)
- Employee 1: 1 hour (does not meet the target)
- Employee 2: 2 hours (meets the target)
- Employee 3: 3 hours (meets the target)
- Employee 4: 4 hours (meets the target)

So, `3` employees meet the target.

### Example 2
**Input:** `hours = [5, 1, 4, 2, 2]`, `target = 6`  
**Output:** `0`

**Explanation:**  
No employee worked at least 6 hours, so the answer is `0`.

---

## Constraints
- `1 <= n == hours.length <= 50`
- `0 <= hours[i], target <= 10^5`
