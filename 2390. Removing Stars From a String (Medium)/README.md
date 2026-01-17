# 2390. Removing Stars From a String (Medium)

## Problem Description
You are given a string `s` that contains lowercase English letters and the star character `'*'`.

In one operation, you can:
1. Choose a `'*'` in `s`.
2. Remove the closest **non-star** character to its **left**, and also remove the `'*'` itself.

After performing all possible operations until no stars remain, return the resulting string.

### Notes
- The input is generated such that the operation is **always possible**.
- The resulting string is guaranteed to be **unique**.

---

## Examples

### Example 1
**Input:** `s = "leet**cod*e"`  
**Output:** `"lecoe"`  

**Explanation (left to right removals):**
- Remove `'t'` and the 1st `'*'`: `"lee*cod*e"`
- Remove `'e'` and the 2nd `'*'`: `"lecod*e"`
- Remove `'d'` and the 3rd `'*'`: `"lecoe"`
No stars remain, so return `"lecoe"`.

---

### Example 2
**Input:** `s = "erase*****"`  
**Output:** `""`  

**Explanation:**  
All characters are removed, so the result is an empty string.

---

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters and `'*'`
- The operation described above can always be performed on `s`
