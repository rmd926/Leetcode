# 238. Product of Array Except Self (Medium)

## Problem
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of **all the elements of `nums` except `nums[i]`**.

You must write an algorithm that:
- Runs in **O(n)** time
- Does **not** use the division operation

The product of any prefix or suffix of `nums` is guaranteed to fit in a **32-bit integer**.

---

## Examples

### Example 1
**Input:** `nums = [1,2,3,4]`  
**Output:** `[24,12,8,6]`

### Example 2
**Input:** `nums = [-1,1,0,-3,3]`  
**Output:** `[0,0,9,0,0]`

---

## Constraints
- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- The input is generated such that `answer[i]` fits in a **32-bit integer**

---

## Follow Up
Can you solve the problem using **O(1)** extra space complexity?  
(The output array does not count as extra space for space complexity analysis.)
