# 2161. Partition Array According to Given Pivot (Medium)

## Problem Description
You are given a **0-indexed** integer array `nums` and an integer `pivot`.

Rearrange `nums` such that the following conditions are satisfied:

1. Every element **less than** `pivot` appears **before** every element **greater than** `pivot`.
2. Every element **equal to** `pivot` appears **between** the elements less than and greater than `pivot`.
3. The **relative order** of elements less than `pivot` and the **relative order** of elements greater than `pivot` must be **maintained**.

More formally, let `p_i` and `p_j` be the new positions of the `i`-th and `j`-th elements.  
If `i < j` and both elements are **less than** `pivot` (or both **greater than** `pivot`), then `p_i < p_j`.

Return the array `nums` after the rearrangement.

---

## Examples

### Example 1
**Input:** `nums = [9,12,5,10,14,3,10]`, `pivot = 10`  
**Output:** `[9,5,3,10,10,12,14]`

**Explanation:**
- Elements less than `pivot`: `[9, 5, 3]` (order preserved)
- Elements equal to `pivot`: `[10, 10]`
- Elements greater than `pivot`: `[12, 14]` (order preserved)

### Example 2
**Input:** `nums = [-3,4,3,2]`, `pivot = 2`  
**Output:** `[-3,2,4,3]`

**Explanation:**
- Elements less than `pivot`: `[-3]`
- Elements equal to `pivot`: `[2]`
- Elements greater than `pivot`: `[4, 3]` (order preserved)

---

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^6 <= nums[i] <= 10^6`
- `pivot` is equal to an element in `nums`
