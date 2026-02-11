# 81. Search in Rotated Sorted Array II (Medium)

## Problem Description
You are given an integer array `nums` sorted in **non-decreasing order** (duplicates allowed).

Before being passed to your function, `nums` is **rotated** at an unknown pivot index `k` (`0 <= k < nums.length`) such that:

`nums = [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]`

For example, `[0,1,2,4,4,4,5,6,6,7]` might be rotated at pivot index `5` and become:
`[4,5,6,6,7,0,1,2,4,4]`

Given the rotated array `nums` and an integer `target`, return `true` if `target` exists in `nums`, otherwise return `false`.

You should reduce the overall number of operations as much as possible.

---

## Examples

### Example 1
**Input:** `nums = [2,5,6,0,0,1,2]`, `target = 0`  
**Output:** `true`

### Example 2
**Input:** `nums = [2,5,6,0,0,1,2]`, `target = 3`  
**Output:** `false`

---

## Constraints
- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i] <= 10^4`
- `nums` is guaranteed to be rotated at some pivot
- `-10^4 <= target <= 10^4`

---

## Follow Up
This problem is similar to **Search in Rotated Sorted Array**, but `nums` may contain duplicates.

Would duplicates affect the runtime complexity? How and why?
