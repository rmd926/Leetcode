# 383. Ransom Note (Easy)

## Problem Description
Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed using the letters from `magazine`, or `false` otherwise.

Each letter in `magazine` can be used **at most once** in `ransomNote`.

---

## Examples

### Example 1
**Input:** `ransomNote = "a"`, `magazine = "b"`  
**Output:** `false`

---

### Example 2
**Input:** `ransomNote = "aa"`, `magazine = "ab"`  
**Output:** `false`

---

### Example 3
**Input:** `ransomNote = "aa"`, `magazine = "aab"`  
**Output:** `true`

---

## Constraints
- `1 <= ransomNote.length, magazine.length <= 10^5`
- `ransomNote` and `magazine` consist only of lowercase English letters
