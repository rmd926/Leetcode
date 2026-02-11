# 881. Boats to Save People (Medium)

## Problem Description
You are given an array `people` where `people[i]` is the weight of the `i`-th person, and an integer `limit` representing the maximum weight a boat can carry.

You have an infinite number of boats, and each boat can carry:
- **at most two people**, and
- the **sum of their weights** must be **at most `limit`**.

Return the **minimum number of boats** needed to carry every person.

---

## Examples

### Example 1
**Input:** `people = [1,2]`, `limit = 3`  
**Output:** `1`

**Explanation:**  
One boat can carry both people: `(1, 2)`.

### Example 2
**Input:** `people = [3,2,2,1]`, `limit = 3`  
**Output:** `3`

**Explanation:**  
An optimal assignment is: `(1,2)`, `(2)`, `(3)`.

### Example 3
**Input:** `people = [3,5,3,4]`, `limit = 5`  
**Output:** `4`

**Explanation:**  
Each person must go alone: `(3)`, `(3)`, `(4)`, `(5)`.

---

## Constraints
- `1 <= people.length <= 5 * 10^4`
- `1 <= people[i] <= limit <= 3 * 10^4`
