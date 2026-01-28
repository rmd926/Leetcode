# 3536. Maximum Product of Two Digits (Easy)

## Problem Description
You are given a positive integer `n`.

Return the **maximum product** of any **two digits** in `n`.

### Note
- You may use the same digit twice **only if it appears more than once** in `n`.

---

## Examples

### Example 1
**Input:** `n = 31`  
**Output:** `3`

**Explanation:**  
Digits are `[3, 1]`.  
Possible product: `3 * 1 = 3` → maximum is `3`.

### Example 2
**Input:** `n = 22`  
**Output:** `4`

**Explanation:**  
Digits are `[2, 2]`.  
Possible product: `2 * 2 = 4` → maximum is `4`.

### Example 3
**Input:** `n = 124`  
**Output:** `8`

**Explanation:**  
Digits are `[1, 2, 4]`.  
Possible products: `1*2=2`, `1*4=4`, `2*4=8` → maximum is `8`.

---

## Constraints
- `10 <= n <= 10^9`
