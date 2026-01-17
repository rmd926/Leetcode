# 771. Jewels and Stones (Easy)

## Problem Description
You are given two strings:
- `jewels`, representing the types of stones that are **jewels**, and
- `stones`, representing the stones you have.

Each character in `stones` represents a type of stone you own.  
Your task is to count how many of the stones you have are also jewels.

**Note:**  
- Letters are **case-sensitive**, so `'a'` is different from `'A'`.
- All characters in `jewels` are unique.

---

## Examples

### Example 1
**Input:**  
`jewels = "aA"`, `stones = "aAAbbbb"`  

**Output:**  
`3`

**Explanation:**  
The stones `'a'` and `'A'` are jewels.  
In `"aAAbbbb"`, there are three such stones.

---

### Example 2
**Input:**  
`jewels = "z"`, `stones = "ZZ"`  

**Output:**  
`0`

**Explanation:**  
None of the stones are jewels.

---

## Constraints
- `1 <= jewels.length, stones.length <= 50`
- `jewels` and `stones` consist of only English letters
- All characters in `jewels` are unique
