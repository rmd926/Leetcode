# 2000. Reverse Prefix of Word (Easy)

## Problem Description
You are given a **0-indexed** string `word` and a character `ch`.

Reverse the segment of `word` that starts at index `0` and ends at the index of the **first occurrence** of `ch` (**inclusive**).

- If `ch` does **not** exist in `word`, do nothing.
- Return the resulting string after applying the operation (if any).

**Example:**  
If `word = "abcdefd"` and `ch = "d"`, the first `'d'` occurs at index `3`.  
Reverse `word[0..3]` → `"dcba"` and keep the rest unchanged → `"dcbaefd"`.

---

## Examples

### Example 1
**Input:** `word = "abcdefd"`, `ch = "d"`  
**Output:** `"dcbaefd"`

**Explanation:**  
The first occurrence of `'d'` is at index `3`.  
Reverse the substring from index `0` to `3` (inclusive), resulting in `"dcbaefd"`.

### Example 2
**Input:** `word = "xyxzxe"`, `ch = "z"`  
**Output:** `"zxyxxe"`

**Explanation:**  
The first occurrence of `'z'` is at index `3`.  
Reverse the substring from index `0` to `3` (inclusive), resulting in `"zxyxxe"`.

### Example 3
**Input:** `word = "abcd"`, `ch = "z"`  
**Output:** `"abcd"`

**Explanation:**  
The character `'z'` does not appear in `word`, so no changes are made.

---

## Constraints
- `1 <= word.length <= 250`
- `word` consists of lowercase English letters
- `ch` is a lowercase English letter
