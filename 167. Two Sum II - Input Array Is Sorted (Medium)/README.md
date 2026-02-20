# 167. Two Sum II - Input Array Is Sorted (Medium)

## Problem Description
You are given a **1-indexed** integer array `numbers` that is already sorted in **non-decreasing order**, and an integer `target`.

Find two numbers such that they add up to `target`. Let these two numbers be `numbers[index1]` and `numbers[index2]` where:

- `1 <= index1 < index2 <= numbers.length`

Return the indices `[index1, index2]` as an integer array of length 2.

Additional rules:
- There is **exactly one solution**.
- You **may not** use the same element twice.
- Your solution must use **constant extra space**.

---

## Examples

### Example 1
**Input:** `numbers = [2,7,11,15]`, `target = 9`  
**Output:** `[1,2]`  
**Explanation:** `2 + 7 = 9`, so return indices `[1, 2]`.

### Example 2
**Input:** `numbers = [2,3,4]`, `target = 6`  
**Output:** `[1,3]`  
**Explanation:** `2 + 4 = 6`, so return indices `[1, 3]`.

### Example 3
**Input:** `numbers = [-1,0]`, `target = -1`  
**Output:** `[1,2]`  
**Explanation:** `-1 + 0 = -1`, so return indices `[1, 2]`.

---

## Constraints
- `2 <= numbers.length <= 3 * 10^4`
- `-1000 <= numbers[i] <= 1000`
- `numbers` is sorted in non-decreasing order
- `-1000 <= target <= 1000`
- The tests are generated such that there is exactly one solution
