# 2221. Find Triangular Sum of an Array (Medium)

## Problem Description
You are given a 0-indexed integer array `nums`, where `nums[i]` is a digit between `0` and `9` (inclusive).

The **triangular sum** of `nums` is the value of the only element remaining after repeatedly applying the following process:

1. Let `nums` have length `n`.
2. If `n == 1`, stop the process.
3. Otherwise, create a new array `newNums` of length `n - 1`.
4. For each index `i` where `0 <= i < n - 1`, set:
   - `newNums[i] = (nums[i] + nums[i + 1]) % 10`
5. Replace `nums` with `newNums` and repeat from step 1.

Return the triangular sum of `nums`.

---

## Examples

### Example 1
**Input:** `nums = [1,2,3,4,5]`  
**Output:** `8`

**Explanation:**  
The process repeatedly combines adjacent elements modulo `10` until one element remains, which equals `8`.

### Example 2
**Input:** `nums = [5]`  
**Output:** `5`

**Explanation:**  
Since `nums` has only one element, the triangular sum is that element itself.

---

## Constraints
- `1 <= nums.length <= 1000`
- `0 <= nums[i] <= 9`
