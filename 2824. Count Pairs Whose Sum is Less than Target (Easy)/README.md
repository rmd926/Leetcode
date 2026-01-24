# 2824. Count Pairs Whose Sum is Less than Target (Easy)

## Problem Description
You are given a **0-indexed** integer array `nums` of length `n` and an integer `target`.

Return the number of pairs `(i, j)` such that:

- `0 <= i < j < n`
- `nums[i] + nums[j] < target`

In other words, count how many index pairs have a sum **strictly less than** `target`.

---

## Examples

### Example 1
**Input:** `nums = [-1, 1, 2, 3, 1]`, `target = 2`  
**Output:** `3`  

**Explanation:** The valid pairs are:
- `(0, 1)` because `nums[0] + nums[1] = 0 < 2`
- `(0, 2)` because `nums[0] + nums[2] = 1 < 2`
- `(0, 4)` because `nums[0] + nums[4] = 0 < 2`  

Pair `(0, 3)` is not counted because `nums[0] + nums[3] = 2` is **not** strictly less than `2`.

### Example 2
**Input:** `nums = [-6, 2, 5, -2, -7, -1, 3]`, `target = -2`  
**Output:** `10`  

**Explanation:** The valid pairs are:
- `(0, 1)` because `-6 + 2 = -4 < -2`
- `(0, 3)` because `-6 + (-2) = -8 < -2`
- `(0, 4)` because `-6 + (-7) = -13 < -2`
- `(0, 5)` because `-6 + (-1) = -7 < -2`
- `(0, 6)` because `-6 + 3 = -3 < -2`
- `(1, 4)` because `2 + (-7) = -5 < -2`
- `(3, 4)` because `-2 + (-7) = -9 < -2`
- `(3, 5)` because `-2 + (-1) = -3 < -2`
- `(4, 5)` because `-7 + (-1) = -8 < -2`
- `(4, 6)` because `-7 + 3 = -4 < -2`

---

## Constraints
- `1 <= nums.length == n <= 50`
- `-50 <= nums[i], target <= 50`
