# 2215. Find the Difference of Two Arrays (Easy)

## Problem Description
Given two **0-indexed integer arrays** `nums1` and `nums2`, return a list `answer` of size `2` where:

- `answer[0]` is a list of all **distinct integers** in `nums1` that are **not present** in `nums2`.
- `answer[1]` is a list of all **distinct integers** in `nums2` that are **not present** in `nums1`.

The integers in each list may be returned in **any order**.

---

## Examples

### Example 1
**Input:**  
`nums1 = [1,2,3]`, `nums2 = [2,4,6]`  

**Output:**  
`[[1,3],[4,6]]`

**Explanation:**  
- In `nums1`, the value `2` appears in `nums2`, but `1` and `3` do not. Therefore, `answer[0] = [1,3]`.  
- In `nums2`, the value `2` appears in `nums1`, but `4` and `6` do not. Therefore, `answer[1] = [4,6]`.

---

### Example 2
**Input:**  
`nums1 = [1,2,3,3]`, `nums2 = [1,1,2,2]`  

**Output:**  
`[[3],[]]`

**Explanation:**  
- In `nums1`, the value `3` does not appear in `nums2`. Although it appears twice in `nums1`, it is included **only once** because the result must contain distinct values.  
- Every integer in `nums2` appears in `nums1`, so `answer[1] = []`.

---

## Constraints
- `1 <= nums1.length, nums2.length <= 1000`
- `-1000 <= nums1[i], nums2[i] <= 1000`
