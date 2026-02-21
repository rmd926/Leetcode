# 154. Find Minimum in Rotated Sorted Array II (Hard)

## Problem Description
An array `nums` of length `n` was originally sorted in ascending order and then rotated between `1` and `n` times. For example, `nums = [0,1,4,4,5,6,7]` might become:
- `[4,5,6,7,0,1,4]` if it was rotated 4 times
- `[0,1,4,4,5,6,7]` if it was rotated 7 times

Rotating an array `[a[0], a[1], ..., a[n-1]]` by 1 time results in `[a[n-1], a[0], a[1], ..., a[n-2]]`.

Given the rotated sorted array `nums` that may contain duplicates, return the **minimum element** in the array. You should reduce the overall operation steps as much as possible.

---

## Examples

### Example 1
**Input:** `nums = [1,3,5]`  
**Output:** `1`

### Example 2
**Input:** `nums = [2,2,2,0,1]`  
**Output:** `0`

---

## Constraints
- `n == nums.length`
- `1 <= n <= 5000`
- `-5000 <= nums[i] <= 5000`
- `nums` is sorted and rotated between `1` and `n` times

---

## Follow Up
This problem is similar to **Find Minimum in Rotated Sorted Array**, but `nums` may contain duplicates. Would this affect the runtime complexity? How and why?
