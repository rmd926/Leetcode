# 1207. Unique Number of Occurrences (Easy)

## Problem Description
Given an array of integers `arr`, return `true` if the **number of occurrences of each value** in the array is **unique**, or `false` otherwise.

In other words, no two distinct values in the array should have the same frequency.

---

## Examples

### Example 1
**Input:** `arr = [1,2,2,1,1,3]`  
**Output:** `true`  

**Explanation:**  
- The value `1` appears `3` times  
- The value `2` appears `2` times  
- The value `3` appears `1` time  

All occurrence counts are unique.

---

### Example 2
**Input:** `arr = [1,2]`  
**Output:** `false`  

**Explanation:**  
- The value `1` appears `1` time  
- The value `2` appears `1` time  

The occurrence counts are not unique.

---

### Example 3
**Input:** `arr = [-3,0,1,-3,1,1,1,-3,10,0]`  
**Output:** `true`  

**Explanation:**  
The occurrence counts of all values are unique.

---

## Constraints
- `1 <= arr.length <= 1000`
- `-1000 <= arr[i] <= 1000`
