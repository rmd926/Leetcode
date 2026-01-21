# 198. House Robber (Medium)

## Problem Description
You are a professional robber planning to rob houses along a street. Each house contains a certain amount of money. However, there is a security system in place:

- **You cannot rob two adjacent houses on the same night**, or the police will be alerted.

Given an integer array `nums`, where `nums[i]` represents the amount of money in the `i`-th house, return the **maximum amount of money** you can rob without triggering the alarm.

---

## Examples

### Example 1
**Input:** `nums = [1,2,3,1]`  
**Output:** `4`

**Explanation:**  
Rob house 1 (money = 1) and house 3 (money = 3).  
Total = `1 + 3 = 4`.

---

### Example 2
**Input:** `nums = [2,7,9,3,1]`  
**Output:** `12`

**Explanation:**  
Rob house 1 (money = 2), house 3 (money = 9), and house 5 (money = 1).  
Total = `2 + 9 + 1 = 12`.

---

## Constraints
- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 400`
