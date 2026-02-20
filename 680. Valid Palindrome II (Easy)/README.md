# 680. Valid Palindrome II (Easy)

## Problem Description
You are given a string `s` consisting of lowercase English letters.  
Return `true` if `s` can become a **palindrome** after deleting **at most one** character. Otherwise, return `false`.

A **palindrome** is a string that reads the same forward and backward.

---

## Examples

### Example 1
**Input:** `s = "aba"`  
**Output:** `true`  
**Explanation:** `"aba"` is already a palindrome, so no deletion is needed.

### Example 2
**Input:** `s = "abca"`  
**Output:** `true`  
**Explanation:** Deleting `'c'` makes the string `"aba"`, which is a palindrome.

### Example 3
**Input:** `s = "abc"`  
**Output:** `false`  
**Explanation:** Even after deleting one character, it cannot become a palindrome.

---

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters only
