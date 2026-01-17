# 724. Find Pivot Index (Easy)

## Problem Description
Given an array of integers `nums`, calculate the **pivot index** of the array.

The **pivot index** is the index where the **sum of all the numbers strictly to the left** of the index is equal to the **sum of all the numbers strictly to the right** of the index.

- If the index is at the **left edge** of the array, then the left sum is considered `0` because there are no elements to the left.
- Similarly, if the index is at the **right edge**, the right sum is considered `0`.

Return the **leftmost pivot index**.  
If no such index exists, return `-1`.

---

## Examples

### Example 1
**Input:** `nums = [1,7,3,6,5,6]`  
**Output:** `3`  

**Explanation:**  
The pivot index is `3`.
- Left sum = `1 + 7 + 3 = 11`
- Right sum = `5 + 6 = 11`

---

### Example 2
**Input:** `nums = [1,2,3]`  
**Output:** `-1`  

**Explanation:**  
There is no index where the left sum equals the right sum.

---

### Example 3
**Input:** `nums = [2,1,-1]`  
**Output:** `0`  

**Explanation:**  
The pivot index is `0`.
- Left sum = `0` (no elements to the left)
- Right sum = `1 + (-1) = 0`

---

## Constraints
- `1 <= nums.length <= 10^4`
- `-1000 <= nums[i] <= 1000`

---

## Note
This problem is the same as **LeetCode 1991: Find the Middle Index in Array**.
