# 222. Count Complete Tree Nodes (Easy)

## Problem Description
You are given the root of a **complete binary tree**. Return the **number of nodes** in the tree.

A **complete binary tree** is defined as:
- Every level, except possibly the last, is completely filled.
- All nodes in the last level are as far **left** as possible.
- If the last level is level `h`, it can contain between `1` and `2^h` nodes (inclusive).

You must design an algorithm that runs in **less than O(n)** time complexity.

---

## Examples

### Example 1
**Input:** `root = [1,2,3,4,5,6]`  
**Output:** `6`

### Example 2
**Input:** `root = []`  
**Output:** `0`

### Example 3
**Input:** `root = [1]`  
**Output:** `1`

---

## Constraints
- The number of nodes in the tree is in the range `[0, 5 * 10^4]`
- `0 <= Node.val <= 5 * 10^4`
- The tree is guaranteed to be complete
