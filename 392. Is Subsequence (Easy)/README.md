# 392. Is Subsequence (Easy)

## Problem
Given two strings `s` and `t`, return `true` if `s` is a **subsequence** of `t`, or `false` otherwise.

A **subsequence** of a string is a new string formed from the original string by deleting some (possibly none) characters **without changing the relative order** of the remaining characters.

- `"ace"` is a subsequence of `"abcde"`
- `"aec"` is **not** a subsequence of `"abcde"`

---

## Examples

### Example 1
**Input:** `s = "abc"`, `t = "ahbgdc"`  
**Output:** `true`

### Example 2
**Input:** `s = "axc"`, `t = "ahbgdc"`  
**Output:** `false`

---

## Constraints
- `0 <= s.length <= 100`
- `0 <= t.length <= 10^4`
- `s` and `t` consist only of lowercase English letters

---

## Follow Up
Suppose there are many incoming strings `s`, such as  
`s₁, s₂, ..., sₖ` where `k ≥ 10^9`, and you want to check each one to see whether it is a subsequence of the same string `t`.

In this scenario, how would you change your algorithm to improve efficiency?
