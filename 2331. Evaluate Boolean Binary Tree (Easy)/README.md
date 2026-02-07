# 2331. Evaluate Boolean Binary Tree (Easy)

## Problem Description
You are given the root of a **full binary tree** with the following rules:

- **Leaf nodes** have a value of `0` or `1`
  - `0` represents `False`
  - `1` represents `True`
- **Non-leaf nodes** have a value of `2` or `3`
  - `2` represents the boolean **OR**
  - `3` represents the boolean **AND**

### Evaluation Rules
- If a node is a **leaf**, its evaluation is its boolean value (`0` → `False`, `1` → `True`).
- Otherwise, evaluate the node’s **two children** and apply the operation indicated by the node’s value:
  - `2` → `left OR right`
  - `3` → `left AND right`

Return the boolean result of evaluating the **root** node.

### Definitions
- A **full binary tree** is a binary tree where every node has either `0` or `2` children.
- A **leaf node** is a node with `0` children.

---

## Examples

### Example 1
**Input:** `root = [2,1,3,null,null,0,1]`  
**Output:** `true`

**Explanation:**
- The `AND` node evaluates to `False AND True = False`
- The `OR` node evaluates to `True OR False = True`
- Final result is `true`

### Example 2
**Input:** `root = [0]`  
**Output:** `false`

**Explanation:**  
The root is a leaf node with value `0`, so it evaluates to `false`.

---

## Constraints
- The number of nodes in the tree is in the range `[1, 1000]`
- `0 <= Node.val <= 3`
- Every node has either `0` or `2` children
- Leaf nodes have a value of `0` or `1`
- Non-leaf nodes have a value of `2` or `3`
