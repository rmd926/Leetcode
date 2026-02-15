# 1910. Remove All Occurrences of a Substring (Medium)

## Problem Description
Given two strings `s` and `part`, repeatedly perform the following operation on `s` until all occurrences of `part` are removed:

- Find the **leftmost** occurrence of the substring `part` in `s` and remove it.

Return the final string `s` after removing all occurrences of `part`.

A **substring** is a contiguous sequence of characters in a string.

---

## Examples

### Example 1
**Input:** `s = "daabcbaabcbc"`, `part = "abc"`  
**Output:** `"dab"`  

**Explanation:**
- Remove `"abc"` starting at index 2 → `s = "dabaabcbc"`
- Remove `"abc"` starting at index 4 → `s = "dababc"`
- Remove `"abc"` starting at index 3 → `s = "dab"`
No `"abc"` remains.

### Example 2
**Input:** `s = "axxxxyyyyb"`, `part = "xy"`  
**Output:** `"ab"`  

**Explanation:**
- Remove `"xy"` starting at index 4 → `s = "axxxyyyb"`
- Remove `"xy"` starting at index 3 → `s = "axxyyb"`
- Remove `"xy"` starting at index 2 → `s = "axyb"`
- Remove `"xy"` starting at index 1 → `s = "ab"`
No `"xy"` remains.

---

## Constraints
- `1 <= s.length <= 1000`
- `1 <= part.length <= 1000`
- `s` and `part` consist of lowercase English letters
