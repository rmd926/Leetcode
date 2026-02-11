# 2540. Minimum Common Value (Easy)

## Problem Description
You are given two integer arrays `nums1` and `nums2`, both sorted in **non-decreasing order**.

Return the **minimum integer** that appears in **both** arrays.  
If there is no common integer between `nums1` and `nums2`, return `-1`.

An integer is considered **common** if it appears at least once in each array.

---

## Examples

### Example 1
**Input:** `nums1 = [1,2,3]`, `nums2 = [2,4]`  
**Output:** `2`

**Explanation:**  
The smallest common element is `2`.

### Example 2
**Input:** `nums1 = [1,2,3,6]`, `nums2 = [2,3,4,5]`  
**Output:** `2`

**Explanation:**  
The common elements are `2` and `3`, and the smallest is `2`.

---

## Constraints
- `1 <= nums1.length, nums2.length <= 10^5`
- `1 <= nums1[i], nums2[j] <= 10^9`
- `nums1` and `nums2` are sorted in non-decreasing order
