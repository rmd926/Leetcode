# 1143. Longest Common Subsequence (Medium)

## Problem Description
You are given two strings `text1` and `text2`.

Return the length of their **longest common subsequence (LCS)**.  
If there is no common subsequence, return `0`.

A **subsequence** of a string is a new string formed from the original string by deleting some characters (possibly none) **without changing the relative order** of the remaining characters.

For example, `"ace"` is a subsequence of `"abcde"`.

A **common subsequence** of two strings is a subsequence that appears in both strings.

---

## Examples

### Example 1
**Input:** `text1 = "abcde"`, `text2 = "ace"`  
**Output:** `3`

**Explanation:**  
The longest common subsequence is `"ace"`, which has length `3`.

### Example 2
**Input:** `text1 = "abc"`, `text2 = "abc"`  
**Output:** `3`

**Explanation:**  
The longest common subsequence is `"abc"`, which has length `3`.

### Example 3
**Input:** `text1 = "abc"`, `text2 = "def"`  
**Output:** `0`

**Explanation:**  
There is no common subsequence, so the result is `0`.

---

## Constraints
- `1 <= text1.length, text2.length <= 1000`
- `text1` and `text2` consist of lowercase English letters only
