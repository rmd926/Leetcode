# 3280. Convert Date to Binary (Easy)

## Problem Description
You are given a string `date` representing a valid Gregorian calendar date in the format:

- `yyyy-mm-dd`

The date can be converted to its **binary representation** by:
1. Converting the **year**, **month**, and **day** to binary **without leading zeroes**.
2. Writing them back in the format:
   - `year-month-day`

Return the binary representation of `date`.

---

## Examples

### Example 1
**Input:** `date = "2080-02-29"`  
**Output:** `"100000100000-10-11101"`

**Explanation:**  
- `2080` in binary is `100000100000`
- `02` in binary is `10`
- `29` in binary is `11101`  
So the result is `"100000100000-10-11101"`.

### Example 2
**Input:** `date = "1900-01-01"`  
**Output:** `"11101101100-1-1"`

**Explanation:**  
- `1900` in binary is `11101101100`
- `1` in binary is `1`
- `1` in binary is `1`  
So the result is `"11101101100-1-1"`.

---

## Constraints
- `date.length == 10`
- `date[4] == date[7] == '-'` and all other characters are digits
- `date` is a valid Gregorian date between **Jan 1, 1900** and **Dec 31, 2100** (inclusive)
