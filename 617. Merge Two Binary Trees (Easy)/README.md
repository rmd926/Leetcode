# 617. Merge Two Binary Trees (Easy)

## Problem Description
You are given two binary trees `root1` and `root2`.

When overlapping the two trees:
- Some nodes may overlap (both trees have a node at the same position).
- Some nodes may not overlap (one tree has a node while the other has `null`).

Merge the two trees into a new binary tree using the following rules:
- If two nodes overlap, the value of the merged node is the **sum** of the two node values.
- If only one node exists (the other is `null`), use the **non-null** node directly.

The merging process must start from the **root nodes** of both trees.

Return the merged tree.

---

## Examples

### Example 1
**Input:**  
`root1 = [1,3,2,5]`  
`root2 = [2,1,3,null,4,null,7]`  

**Output:**  
`[3,4,5,5,4,null,7]`

### Example 2
**Input:**  
`root1 = [1]`  
`root2 = [1,2]`  

**Output:**  
`[2,2]`

---

## Constraints
- The number of nodes in both trees is in the range `[0, 2000]`
- `-10^4 <= Node.val <= 10^4`
