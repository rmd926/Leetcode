# 2418. Sort the People (Easy)

## Problem Description
You are given:
- an array of strings `names`
- an array of integers `heights`

Both arrays have the same length `n`, and `heights` contains **distinct positive integers**.

For each index `i`, `names[i]` is the name of the `i`-th person and `heights[i]` is that person's height.

Return the array `names` sorted in **descending order** by the corresponding heights.

---

## Examples

### Example 1
**Input:** `names = ["Mary","John","Emma"]`, `heights = [180,165,170]`  
**Output:** `["Mary","Emma","John"]`

**Explanation:**  
Mary is the tallest (180), followed by Emma (170), then John (165).

### Example 2
**Input:** `names = ["Alice","Bob","Bob"]`, `heights = [155,185,150]`  
**Output:** `["Bob","Alice","Bob"]`

**Explanation:**  
The first Bob is the tallest (185), followed by Alice (155), then the second Bob (150).

---

## Constraints
- `n == names.length == heights.length`
- `1 <= n <= 10^3`
- `1 <= names[i].length <= 20`
- `1 <= heights[i] <= 10^5`
- `names[i]` consists of lowercase and uppercase English letters
- All values in `heights` are distinct
