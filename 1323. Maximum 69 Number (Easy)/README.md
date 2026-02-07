# 1323. Maximum 69 Number (Easy)

## Problem Description
You are given a positive integer `num` consisting only of digits `6` and `9`.

You may change **at most one digit**:
- `6` can be changed to `9`
- `9` can be changed to `6`

Return the **maximum** number you can obtain after applying at most one change.

---

## Examples

### Example 1
**Input:** `num = 9669`  
**Output:** `9969`

**Explanation:**  
Possible results by changing one digit:
- Change the 1st digit: `6669`
- Change the 2nd digit: `9969`
- Change the 3rd digit: `9699`
- Change the 4th digit: `9666`  
The maximum is `9969`.

### Example 2
**Input:** `num = 9996`  
**Output:** `9999`

**Explanation:**  
Changing the last digit `6` to `9` gives the maximum result.

### Example 3
**Input:** `num = 9999`  
**Output:** `9999`

**Explanation:**  
No change improves the number, so it is best to keep it as is.

---

## Constraints
- `1 <= num <= 10^4`
- `num` consists only of digits `6` and `9`
