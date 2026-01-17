# 682. Baseball Game (Easy)

## Problem Description
You are keeping the scores for a baseball game with unusual rules. At the beginning of the game, you start with an empty record.

You are given a list of strings `operations`, where `operations[i]` is the *i-th* operation applied to the record. Each operation is one of the following:

- An integer `x`: Record a new score of `x`.
- `"+"`: Record a new score that is the **sum of the previous two scores**.
- `"D"`: Record a new score that is **double the previous score**.
- `"C"`: **Invalidate** the previous score, removing it from the record.

Return the **sum of all the scores** on the record after applying all operations.

The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer, and all operations are valid.

---

## Examples

### Example 1
**Input:** `ops = ["5","2","C","D","+"]`  
**Output:** `30`  

**Explanation:**
- `"5"` → record: `[5]`
- `"2"` → record: `[5, 2]`
- `"C"` → record: `[5]`
- `"D"` → record: `[5, 10]`
- `"+"` → record: `[5, 10, 15]`  
Total = `5 + 10 + 15 = 30`

---

### Example 2
**Input:** `ops = ["5","-2","4","C","D","9","+","+"]`  
**Output:** `27`  

**Explanation:**
- `"5"` → `[5]`
- `"-2"` → `[5, -2]`
- `"4"` → `[5, -2, 4]`
- `"C"` → `[5, -2]`
- `"D"` → `[5, -2, -4]`
- `"9"` → `[5, -2, -4, 9]`
- `"+"` → `[5, -2, -4, 9, 5]`
- `"+"` → `[5, -2, -4, 9, 5, 14]`  
Total = `27`

---

### Example 3
**Input:** `ops = ["1","C"]`  
**Output:** `0`  

**Explanation:**
- `"1"` → `[1]`
- `"C"` → `[]`  
Total = `0`

---

## Constraints
- `1 <= operations.length <= 1000`
- `operations[i]` is `"C"`, `"D"`, `"+"`, or a string representing an integer in the range `[-3 * 10^4, 3 * 10^4]`
- For `"+"`, there will always be at least two previous scores on the record
- For `"C"` and `"D"`, there will always be at least one previous score on the record
