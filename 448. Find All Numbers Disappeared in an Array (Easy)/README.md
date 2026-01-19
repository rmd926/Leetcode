# 448. Find All Numbers Disappeared in an Array (Easy)

## Problem Description
Given an integer array `nums` of length `n`, where each element `nums[i]` is in the range `[1, n]`, some numbers may appear **twice** while others appear **once**.

Your task is to return **all the integers in the range `[1, n]` that do not appear in `nums`**.

---

## Examples

### Example 1
**Input:** `nums = [4,3,2,7,8,2,3,1]`  
**Output:** `[5,6]`

**Explanation:**  
The numbers `1` through `8` should appear, but `5` and `6` are missing.

---

### Example 2
**Input:** `nums = [1,1]`  
**Output:** `[2]`

**Explanation:**  
The number `2` does not appear in the array.

---

## Constraints
- `n == nums.length`
- `1 <= n <= 10^5`
- `1 <= nums[i] <= n`

---

## Follow Up
Can you solve the problem in `O(n)` time complexity **without using extra space**?  
You may assume that the returned list does **not** count as extra space.
