# 34. Find First and Last Position of Element in Sorted Array (Medium)

## Problem Description
You are given an integer array `nums` sorted in **non-decreasing order** and an integer `target`.

Find the **starting** and **ending** position of `target` in `nums`.

- If `target` is not found, return `[-1, -1]`.
- You must write an algorithm with **O(log n)** runtime complexity.

---

## Examples

### Example 1
**Input:** `nums = [5,7,7,8,8,10]`, `target = 8`  
**Output:** `[3, 4]`

### Example 2
**Input:** `nums = [5,7,7,8,8,10]`, `target = 6`  
**Output:** `[-1, -1]`

### Example 3
**Input:** `nums = []`, `target = 0`  
**Output:** `[-1, -1]`

---

## Constraints
- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `nums` is sorted in non-decreasing order
- `-10^9 <= target <= 10^9`
