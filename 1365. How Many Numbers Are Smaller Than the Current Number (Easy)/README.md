# 1365. How Many Numbers Are Smaller Than the Current Number (Easy)

## Problem Description
Given an integer array `nums`, for each element `nums[i]`, determine how many numbers in the array are **strictly smaller** than `nums[i]`.

For each index `i`, count the number of indices `j` such that:
- `j != i`
- `nums[j] < nums[i]`

Return the result as an array.

---

## Examples

### Example 1
**Input:** `nums = [8,1,2,2,3]`  
**Output:** `[4,0,1,1,3]`

**Explanation:**  
- For `nums[0] = 8`, there are four smaller numbers: `1, 2, 2, 3`
- For `nums[1] = 1`, there are no smaller numbers
- For `nums[2] = 2`, there is one smaller number: `1`
- For `nums[3] = 2`, there is one smaller number: `1`
- For `nums[4] = 3`, there are three smaller numbers: `1, 2, 2`

---

### Example 2
**Input:** `nums = [6,5,4,8]`  
**Output:** `[2,1,0,3]`

---

### Example 3
**Input:** `nums = [7,7,7,7]`  
**Output:** `[0,0,0,0]`

---

## Constraints
- `2 <= nums.length <= 500`
- `0 <= nums[i] <= 100`
