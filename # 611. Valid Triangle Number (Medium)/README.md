# 611. Valid Triangle Number (Medium)

## Problem Description
You are given an integer array `nums`.  
Return the number of **triplets** that can be chosen from `nums` such that the three selected values can represent the side lengths of a **valid triangle**.

A triplet `(a, b, c)` can form a triangle if it satisfies the triangle inequality:
- `a + b > c`
- `a + c > b`
- `b + c > a`

---

## Examples

### Example 1
**Input:** `nums = [2, 2, 3, 4]`  
**Output:** `3`

**Explanation:**  
Valid triplets include:
- `2, 3, 4` (using the first `2`)
- `2, 3, 4` (using the second `2`)
- `2, 2, 3`

### Example 2
**Input:** `nums = [4, 2, 3, 4]`  
**Output:** `4`

---

## Constraints
- `1 <= nums.length <= 1000`
- `0 <= nums[i] <= 1000`
