# 3541. Find Most Frequent Vowel and Consonant (Easy)

## Problem Description
You are given a string `s` consisting of lowercase English letters (`'a'` to `'z'`).

Your task is to:
1. Find the **vowel** (one of `'a'`, `'e'`, `'i'`, `'o'`, `'u'`) with the **maximum frequency** in `s`.
2. Find the **consonant** (all other letters excluding vowels) with the **maximum frequency** in `s`.
3. Return the **sum** of these two maximum frequencies.

### Notes
- If multiple vowels (or consonants) share the same maximum frequency, you may choose **any** one of them.
- If there are **no vowels** or **no consonants** in the string, treat the missing group's maximum frequency as **0**.
- The **frequency** of a letter `x` is the number of times it appears in the string.

---

## Examples

### Example 1
**Input:** `s = "successes"`  
**Output:** `6`

**Explanation:**
- Vowels: `'u'` (1), `'e'` (2) → max vowel frequency = `2`
- Consonants: `'s'` (4), `'c'` (2) → max consonant frequency = `4`
- Result = `2 + 4 = 6`

### Example 2
**Input:** `s = "aeiaeia"`  
**Output:** `3`

**Explanation:**
- Vowels: `'a'` (3), `'e'` (2), `'i'` (2) → max vowel frequency = `3`
- No consonants → max consonant frequency = `0`
- Result = `3 + 0 = 3`

---

## Constraints
- `1 <= s.length <= 100`
- `s` consists of lowercase English letters only
