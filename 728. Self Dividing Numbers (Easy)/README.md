# 728. Self Dividing Numbers (Easy)

## Problem Description
A **self-dividing number** is a number that is divisible by **every digit it contains**.

Rules:
- A self-dividing number **cannot contain the digit `0`**
- Every digit in the number must divide the number evenly

---

## Examples

### Example 1
**Input:** `left = 1`, `right = 22`  
**Output:**  
`[1,2,3,4,5,6,7,8,9,11,12,15,22]`

**Explanation:**  
Each number in the output is divisible by all of its digits.

---

### Example 2
**Input:** `left = 47`, `right = 85`  
**Output:**  
`[48,55,66,77]`

---

## Constraints
- `1 <= left <= right <= 10^4`
