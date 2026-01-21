# 1679. Max Number of K-Sum Pairs (Medium)

## Problem Description
You are given an integer array `nums` and an integer `k`.

In one operation, you can choose **two numbers** from the array whose sum equals `k` and **remove both** numbers from the array.

Return the **maximum number of operations** you can perform, where each operation removes a valid pair that sums to `k`.

---

## Examples

### Example 1
**Input:** `nums = [1,2,3,4]`, `k = 5`  
**Output:** `2`

**Explanation:**  
Starting with `nums = [1,2,3,4]`:
- Remove `1` and `4` → `nums = [2,3]`
- Remove `2` and `3` → `nums = []`  
No more pairs sum to `5`, so the maximum number of operations is `2`.

---

### Example 2
**Input:** `nums = [3,1,3,4,3]`, `k = 6`  
**Output:** `1`

**Explanation:**  
Starting with `nums = [3,1,3,4,3]`:
- Remove two `3`s → `nums = [1,4,3]`  
No more pairs sum to `6`, so the maximum number of operations is `1`.

---

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `1 <= k <= 10^9`
