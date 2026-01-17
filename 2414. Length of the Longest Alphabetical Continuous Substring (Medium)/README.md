
# 2414. Length of the Longest Alphabetical Continuous Substring (Medium)

## Problem
An **alphabetical continuous string** is a string consisting of **consecutive letters in the alphabet**.  
In other words, it is any substring of the string:
`"abcdefghijklmnopqrstuvwxyz"`

For example:
- `"abc"` is an alphabetical continuous string
- `"acb"` and `"za"` are **not**

Given a string `s` consisting of **lowercase English letters only**, return the **length of the longest alphabetical continuous substring** of `s`.

---

## Examples

### Example 1
**Input:** `s = "abacaba"`  
**Output:** `2`  

**Explanation:**  
There are 4 distinct alphabetical continuous substrings: `"a"`, `"b"`, `"c"`, and `"ab"`.  
The longest among them is `"ab"`, which has length `2`.

---

### Example 2
**Input:** `s = "abcde"`  
**Output:** `5`  

**Explanation:**  
The entire string `"abcde"` is an alphabetical continuous substring, so the answer is `5`.

---

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of **lowercase English letters only**

