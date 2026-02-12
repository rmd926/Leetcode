# 2206. Divide Array Into Equal Pairs (Easy)

## Problem Description
You are given an integer array `nums` consisting of `2 * n` integers.

You need to divide `nums` into `n` pairs such that:
- Each element belongs to **exactly one** pair.
- The two elements in each pair are **equal**.

Return `true` if `nums` can be divided into `n` valid pairs, otherwise return `false`.

---

## Examples

### Example 1
**Input:** `nums = [3,2,3,2,2,2]`  
**Output:** `true`

**Explanation:**  
There are 6 elements, so we need `6 / 2 = 3` pairs.  
One valid pairing is `(2,2)`, `(3,3)`, `(2,2)`.

### Example 2
**Input:** `nums = [1,2,3,4]`  
**Output:** `false`

**Explanation:**  
There is no way to form pairs where both elements in every pair are equal.

---

## Constraints
- `nums.length == 2 * n`
- `1 <= n <= 500`
- `1 <= nums[i] <= 500`
