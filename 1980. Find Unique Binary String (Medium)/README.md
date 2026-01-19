# 1980. Find Unique Binary String (Medium)

## Problem Description
You are given an array of strings `nums` containing `n` **unique binary strings**, each of length `n`.

Your task is to return **any binary string of length `n`** that **does not appear** in `nums`.

If multiple valid answers exist, you may return **any one** of them.

---

## Examples

### Example 1
**Input:** `nums = ["01","10"]`  
**Output:** `"11"`  

**Explanation:**  
`"11"` does not appear in `nums`.  
`"00"` would also be a valid answer.

---

### Example 2
**Input:** `nums = ["00","01"]`  
**Output:** `"11"`  

**Explanation:**  
`"11"` does not appear in `nums`.  
`"10"` would also be a valid answer.

---

### Example 3
**Input:** `nums = ["111","011","001"]`  
**Output:** `"101"`  

**Explanation:**  
`"101"` does not appear in `nums`.  
`"000"`, `"010"`, `"100"`, and `"110"` would also be valid answers.

---

## Constraints
- `n == nums.length`
- `1 <= n <= 16`
- `nums[i].length == n`
- `nums[i]` consists only of `'0'` and `'1'`
- All strings in `nums` are unique
