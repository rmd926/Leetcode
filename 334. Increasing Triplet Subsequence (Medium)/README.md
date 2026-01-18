# 334. Increasing Triplet Subsequence (Medium)

## Problem Description
Given an integer array `nums`, return `true` if there exists a triple of indices `(i, j, k)` such that:

- `i < j < k`
- `nums[i] < nums[j] < nums[k]`

If no such indices exist, return `false`.

---

## Examples

### Example 1
**Input:** `nums = [1,2,3,4,5]`  
**Output:** `true`  
**Explanation:** Any triplet with `i < j < k` is valid.

### Example 2
**Input:** `nums = [5,4,3,2,1]`  
**Output:** `false`  
**Explanation:** No increasing triplet subsequence exists.

### Example 3
**Input:** `nums = [2,1,5,0,4,6]`  
**Output:** `true`  
**Explanation:** One valid triplet is `(1, 4, 5)` because  
`nums[1] = 1 < nums[4] = 4 < nums[5] = 6`.

---

## Constraints
- `1 <= nums.length <= 5 * 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`

---

## Follow Up
Can you implement a solution that runs in `O(n)` time and uses `O(1)` extra space?
