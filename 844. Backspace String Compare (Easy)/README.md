# 844. Backspace String Compare (Easy)

## Problem Description
Given two strings `s` and `t`, return `true` if they are equal when both are typed into empty text editors. The character `'#'` represents a backspace.

A backspace deletes the character immediately before it (if any). If a backspace is applied when the text is empty, the text remains empty.

---

## Examples

### Example 1
**Input:** `s = "ab#c"`, `t = "ad#c"`  
**Output:** `true`  
**Explanation:** Both `s` and `t` become `"ac"`.

### Example 2
**Input:** `s = "ab##"`, `t = "c#d#"`  
**Output:** `true`  
**Explanation:** Both `s` and `t` become `""`.

### Example 3
**Input:** `s = "a#c"`, `t = "b"`  
**Output:** `false`  
**Explanation:** `s` becomes `"c"` while `t` becomes `"b"`.

---

## Constraints
- `1 <= s.length, t.length <= 200`
- `s` and `t` contain only lowercase English letters and `'#'`

---

## Follow Up
Can you solve the problem in `O(n)` time and `O(1)` extra space?
