# 938. Range Sum of BST (Easy)

## Problem Description
You are given the root node of a **binary search tree (BST)** and two integers `low` and `high`.

Return the **sum of values** of all nodes with a value in the **inclusive range** `[low, high]`.

---

## Examples

### Example 1
**Input:** `root = [10,5,15,3,7,null,18]`, `low = 7`, `high = 15`  
**Output:** `32`

**Explanation:**  
Nodes with values in `[7, 15]` are `7`, `10`, and `15`.  
Sum = `7 + 10 + 15 = 32`.

### Example 2
**Input:** `root = [10,5,15,3,7,13,18,1,null,6]`, `low = 6`, `high = 10`  
**Output:** `23`

**Explanation:**  
Nodes with values in `[6, 10]` are `6`, `7`, and `10`.  
Sum = `6 + 7 + 10 = 23`.

---

## Constraints
- The number of nodes in the tree is in the range `[1, 2 * 10^4]`
- `1 <= Node.val <= 10^5`
- `1 <= low <= high <= 10^5`
- All `Node.val` are unique
