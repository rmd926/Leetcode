# 645. Set Mismatch (Easy)

## Problem Description
You are given a set of integers that originally contained all numbers from `1` to `n`. However, due to an error:

- One number is **duplicated** (appears twice)
- One number is **missing** from the set

You are given an integer array `nums` representing the state of the set after the error.

Your task is to find:
1. The number that occurs **twice**
2. The number that is **missing**

Return them as an array `[duplicate, missing]`.

---

## Examples

### Example 1
**Input:** `nums = [1,2,2,4]`  
**Output:** `[2,3]`

**Explanation:**  
- The number `2` appears twice
- The number `3` is missing

---

### Example 2
**Input:** `nums = [1,1]`  
**Output:** `[1,2]`

**Explanation:**  
- The number `1` appears twice
- The number `2` is missing

---

## Constraints
- `2 <= nums.length <= 10^4`
- `1 <= nums[i] <= 10^4`
