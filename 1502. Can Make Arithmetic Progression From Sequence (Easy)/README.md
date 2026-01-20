# 1502. Can Make Arithmetic Progression From Sequence (Easy)

## Problem Description
A sequence of numbers is called an **arithmetic progression** if the difference between any two consecutive elements is the same.

Given an integer array `arr`, determine whether the elements of `arr` can be **rearranged** to form an arithmetic progression.

Return `true` if it is possible, otherwise return `false`.

---

## Examples

### Example 1
**Input:** `arr = [3,5,1]`  
**Output:** `true`  

**Explanation:**  
We can reorder the array as `[1,3,5]` (difference `2`) or `[5,3,1]` (difference `-2`), and each consecutive pair has the same difference.

---

### Example 2
**Input:** `arr = [1,2,4]`  
**Output:** `false`  

**Explanation:**  
There is no way to reorder the elements to form an arithmetic progression.

---

## Constraints
- `2 <= arr.length <= 1000`
- `-10^6 <= arr[i] <= 10^6`
