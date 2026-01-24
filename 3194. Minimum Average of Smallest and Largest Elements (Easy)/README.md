# 3194. Minimum Average of Smallest and Largest Elements (Easy)

## Problem Description
You have an array of floating point numbers `averages`, which is initially empty.  
You are given an integer array `nums` of length `n`, where `n` is even.

Repeat the following procedure **`n / 2` times**:

1. Remove the **smallest** element `minElement` and the **largest** element `maxElement` from `nums`.
2. Compute the value `(minElement + maxElement) / 2` and append it to `averages`.

After all operations, return the **minimum** value in the array `averages`.

---

## Examples

### Example 1
**Input:** `nums = [7, 8, 3, 4, 15, 13, 4, 1]`  
**Output:** `5.5`

**Explanation:**  
After repeatedly removing the smallest and largest elements and storing their averages, the minimum value in `averages` is `5.5`.

### Example 2
**Input:** `nums = [1, 9, 8, 3, 10, 5]`  
**Output:** `5.5`

**Explanation:**  
The computed averages are `[5.5, 6, 6.5]`, and the minimum is `5.5`.

### Example 3
**Input:** `nums = [1, 2, 3, 7, 8, 9]`  
**Output:** `5.0`

**Explanation:**  
All computed averages are `5`, so the minimum is `5.0`.

---

## Constraints
- `2 <= n == nums.length <= 50`
- `n` is even
- `1 <= nums[i] <= 50`
