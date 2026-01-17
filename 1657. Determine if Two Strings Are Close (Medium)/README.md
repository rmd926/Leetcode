# 1657. Determine if Two Strings Are Close (Medium)

## Problem Description
Two strings are considered **close** if one string can be transformed into the other using the following operations any number of times:

- **Operation 1:** Swap any two existing characters in the string.  
  - Example: `"abcde"` → `"aecdb"`

- **Operation 2:** Choose two existing characters and transform **all occurrences** of one character into the other, and do the same with the other character.  
  - Example: `"aacabb"` → `"bbcbaa"`  
    (all `'a'` characters become `'b'`, and all `'b'` characters become `'a'`)

You may apply these operations to either string as many times as necessary.

Given two strings `word1` and `word2`, return `true` if `word1` and `word2` are **close**, or `false` otherwise.

---

## Examples

### Example 1
**Input:** `word1 = "abc"`, `word2 = "bca"`  
**Output:** `true`  

**Explanation:**  
You can transform `word1` into `word2` using swap operations:
- `"abc"` → `"acb"`
- `"acb"` → `"bca"`

---

### Example 2
**Input:** `word1 = "a"`, `word2 = "aa"`  
**Output:** `false`  

**Explanation:**  
It is impossible to transform one string into the other because their lengths differ.

---

### Example 3
**Input:** `word1 = "cabbba"`, `word2 = "abbccc"`  
**Output:** `true`  

**Explanation:**  
One possible sequence of operations:
- `"cabbba"` → `"caabbb"` (swap)
- `"caabbb"` → `"baaccc"` (transform)
- `"baaccc"` → `"abbccc"` (transform)

---

## Constraints
- `1 <= word1.length, word2.length <= 10^5`
- `word1` and `word2` contain only lowercase English letters
