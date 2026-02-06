# 1748. Sum of Unique Elements (Easy)

## Problem Description
You are given an integer array `nums`.

An element is considered **unique** if it appears **exactly once** in the array.

Return the **sum of all unique elements** in `nums`.

---

## Examples

### Example 1
**Input:** `nums = [1, 2, 3, 2]`  
**Output:** `4`

**Explanation:**  
The unique elements are `[1, 3]`.  
Sum = `1 + 3 = 4`.

### Example 2
**Input:** `nums = [1, 1, 1, 1, 1]`  
**Output:** `0`

**Explanation:**  
There are no unique elements, so the sum is `0`.

### Example 3
**Input:** `nums = [1, 2, 3, 4, 5]`  
**Output:** `15`

**Explanation:**  
All elements are unique.  
Sum = `1 + 2 + 3 + 4 + 5 = 15`.

---

## Constraints
- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`
