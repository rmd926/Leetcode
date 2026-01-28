# 3110. Score of a String (Easy)

## Problem Description
You are given a string `s`.

The **score** of a string is defined as the sum of the **absolute differences** between the ASCII values of every pair of **adjacent characters** in the string.

Formally, the score is:

\[
\sum_{i=0}^{|s|-2} \left| \text{ASCII}(s[i]) - \text{ASCII}(s[i+1]) \right|
\]

Return the score of `s`.

---

## Examples

### Example 1
**Input:** `s = "hello"`  
**Output:** `13`

**Explanation:**  
ASCII values: `'h' = 104`, `'e' = 101`, `'l' = 108`, `'l' = 108`, `'o' = 111`  
Score:
- `|104 - 101| = 3`
- `|101 - 108| = 7`
- `|108 - 108| = 0`
- `|108 - 111| = 3`

Total = `3 + 7 + 0 + 3 = 13`.

### Example 2
**Input:** `s = "zaz"`  
**Output:** `50`

**Explanation:**  
ASCII values: `'z' = 122`, `'a' = 97`  
Score:
- `|122 - 97| = 25`
- `|97 - 122| = 25`

Total = `25 + 25 = 50`.

---

## Constraints
- `2 <= s.length <= 100`
- `s` consists only of lowercase English letters
