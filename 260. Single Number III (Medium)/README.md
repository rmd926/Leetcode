# 260. Single Number III (Medium)

## Problem
Given an integer array `nums`, **exactly two** elements appear **only once**, and all the other elements appear **exactly twice**.  
Return the two elements that appear only once. You may return the answer in **any order**.

You must write an algorithm that:
- Runs in **linear time**: `O(n)`
- Uses **constant extra space**: `O(1)`

---

## Examples

### Example 1
**Input:** `nums = [1,2,1,3,2,5]`  
**Output:** `[3,5]`  
**Explanation:** `[5,3]` is also a valid answer.

### Example 2
**Input:** `nums = [-1,0]`  
**Output:** `[-1,0]`

### Example 3
**Input:** `nums = [0,1]`  
**Output:** `[1,0]`

---

## Constraints
- `2 <= nums.length <= 3 * 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`
- Each integer in `nums` appears **exactly twice**, except for **two** integers which appear **once**
